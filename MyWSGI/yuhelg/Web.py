from webob.dec import wsgify
from webob import Response,Request
from webob import exc
import re

#字典转为属性类
class Dictobj():
    def __init__(self,d):
        if isinstance(d,dict):
            self.__dict__['_dict'] = d
        else:
            self.__dict__['_dict'] = d

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError("Attribute {} not found".format(item))

    def __setattr__(self, key, value):
        raise NotImplementedError

class Context(dict):
    def __getattr__(self, item):
        try:
            return self[item]
        except:
            raise AttributeError("Attrinute {} Not Found".format(item))

    def __setattr__(self, key, value):
        self[key] = value

class Supcontext(Context):
    def __init__(self, globalcontext: Context = None):
        super().__init__()
        self.relate(globalcontext)

    def relate(self, globalcontext: Context = None):
        self.globalcontext = globalcontext

    def __getattr__(self, item):
        if item in self.keys():
            return self[item]
        return self.globalcontext[item]

#路由匹配
class _Router:
    pattern = re.compile("/(\{([^{}:]+:[+-]?[^{}:]*)\})")
    s1 = '/pu/{name:str}/{id:int}'
    s2 = '/pu/xxxx/{id:}/yyy'
    s3 = '/st/xxx/512335'
    s4 = '/st/{name:}/dsd/{id:aaa}'

    TYPEPATTRENS = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',
        'any': r'.+'
    }

    TYPECAST = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }
    #转换格式：/{id:int} => /(?P<id>[+-]?\\d+)
    def transform(self,kv: str):
        name, _, type = kv.strip("/{}").partition(':')
        return '/(?P<{}>{})'.format(name, self.TYPEPATTRENS.get(type, '\w+')), name, self.TYPECAST.get(type, str)

    #解析src转换格式：/{id:int} => /(?P<id>[+-]?\\d+),返回正则表达式和列表
    def _parse(self,src: str):
        start = 0
        res = ''
        translator = {}
        while True:
            matcher = self.pattern.search(src, start)
            if matcher:
                res += matcher.string[start:matcher.start()]
                tmp = self.transform(matcher.string[matcher.start():matcher.end()])
                res += tmp[0]
                translator[tmp[1]] = tmp[2]
                start = matcher.end()
            else:
                break

        if res:
            return res, translator
        else:
            return src, translator

    def __init__(self,prefix:str=""):
        self._prefix = prefix #一级目录
        self._routetable  = [] #三元组

        #拦截器
        self.pre_interceptor = []
        self.post_interceptor = []

        #上下文
        self.ctx = Supcontext()

    def prefix(self):
        return self._prefix

    #将请求与路径，handler绑定一起
    def router(self, path, *method):
        def wrapper(fn):
            pattern,translator = self._parse(path)
            self._routetable.append((method, re.compile(pattern),translator, fn))
            return fn
        return wrapper

    #handler前的拦截器注册函数
    def register_preinterceptor(self,fn):
        self.pre_interceptor.append(fn)
        return fn

    # handler后的拦截器注册函数
    def register_psotinterceptor(self,fn):
        self.post_interceptor.append(fn)
        return fn

    def get(self, pattern):
        return self.router(pattern, "GET")

    def post(self,pattern):
        return self.router(pattern, "POST")

    def head(self,pattern):
        return self.router(pattern, "HEAD")

    def match(self,ctx,request:Request) -> Response:
        if not request.path.startswith(self._prefix):
            return None

        #进行请求拦截
        for fn in self.pre_interceptor:
            request = fn(self.ctx,request)

        for method,pattern,translator, handler in self._routetable:
            if not method or request.method.upper() in method:
                matcher  = pattern.match(request.path.replace(self._prefix,"",1))
                if matcher:
                    newdict = {}
                    for k,v in  matcher.groupdict().items():
                        print(k,v)
                        newdict[k] = translator[k](v)
                    request.vars = Dictobj(newdict)
                    res = handler(self.ctx,request)
                    # 进行响应拦截
                    # for fn in self.post_interceptor:
                    #     request = fn(self.ctx, request)

                    return res



class YuHeLg:

    #类属性暴漏
    Router = _Router
    Response = Response
    Request = Request

    #全局上下文管理
    ctx = Context()
    def __init__(self,**kwargs):
        self.ctx.app = self
        for k,v in kwargs:
            self.ctx[k] = v

    # 前缀开头的所有Router对象
    ROUTETABLE = []

    #拦截器
    PRE_INTERCEPTOR = []
    POST_INTERCEPTOR = []

    # handler前的拦截器注册函数
    @classmethod
    def register_preinterceptor(cls,fn):
        cls.PRE_INTERCEPTOR.append(fn)
        return fn

    # handler后的拦截器注册函数
    @classmethod
    def register_psotinterceptor(cls,fn):
        cls.POST_INTERCEPTOR.append(fn)
        return fn

    # 注册函数
    #为Router 关联全局上下文
    @classmethod
    def register(cls,router:Router):
        router.ctx.relate(cls.ctx)
        router.ctx.router = router
        cls.ROUTETABLE.append(router)


    @wsgify
    def __call__(self, request:Request) -> Response:
        for fn in self.PRE_INTERCEPTOR:
            request = fn(self.ctx,request)

        for router in self.ROUTETABLE:
            response = router.match(self.ctx,request)

            for fn in self.POST_INTERCEPTOR:
                response = fn(self.ctx, request,response)

            if response:
                return response
        raise exc.HTTPNotFound(body="<h1>页面走丢了</h1>")

# index = _Router()
# python = _Router("/python")
#
# YuHeLg.register(index)
# YuHeLg.register(python)
#
# @index.get("^/$")
# def browse_root(ctx:Context,request:Request):
#     res = Response()
#     res.status_code = 200
#     res.content_type = 'text/html'
#     res.charset = 'utf-8'
#     html = '<h1>欢迎访问</h1>'.encode('utf-8')
#     res.body = html
#     return res
#
# @python.router("/{name:str}")
# @python.get("/{id:int}")
# def browse_python(ctx:Context,request:Request):
#     res = Response()
#     res.status_code = 200
#     res.charset = 'utf-8'
#     res.content_type = 'text/html'
#     html = '<h1>欢迎学习yuhelg教育</h1>'.encode('utf-8')
#     res.body = html
#     return res
#
# @python.register_preinterceptor
# def show_prefix(ctx:Context,request:Request):
#     print(1,"prefix = {}".format(ctx.router.prefix))
#     return request
#
# @YuHeLg.register_preinterceptor
# def show_headers(ctx:Context,request:Request):
#     print(2,request.path)
#     print(3,request.headers)
#     return request
#
#
