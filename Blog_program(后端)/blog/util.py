import json
from yuhelg import YuHeLg

#处理json格式的内容
def jsonify(statue=200,**kwargs):
    content = json.dumps(kwargs)
    response = YuHeLg.Response()
    response.content_type = 'application/json'
    response.status_code = statue
    response.charset = 'utf-8'
    response.body = "{}".format(content).encode()
    return response

def vaildate(d:dict,name:str,type_func,default,func):
    try:
        result = type_func(d.get(name,default))
        result = func(result,default)
    except:
        result = default
    return result