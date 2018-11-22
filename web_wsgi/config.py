from webob.dec import wsgify
from webob import Response,Request

class Routes:
    def browse_root(request:Request):
        res = Response()
        res.status_code = 200
        res.content_type = 'text/html'
        res.charset = 'utf-8'
        html = '<h1>欢迎访问</h1>'.encode('utf-8')
        res.body = html
        return res

    def browse_python(request:Request):
        res = Response()
        res.status_code = 200
        res.charset = 'utf-8'
        res.content_type = 'text/html'
        html = '<h1>欢迎学习yuhelg教育</h1>'.encode('utf-8')
        res.body = html
        return res

