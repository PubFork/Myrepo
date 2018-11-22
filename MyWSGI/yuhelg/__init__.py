from yuhelg.Web import YuHeLg
from wsgiref.simple_server import make_server
import json

index = YuHeLg.Router()
python = YuHeLg.Router("/python")

YuHeLg.register(index)
YuHeLg.register(python)

@index.get("^/$")
def browse_root(ctx,request:YuHeLg.Request):
    res = YuHeLg.Response()
    res.status_code = 200
    res.content_type = 'text/html'
    res.charset = 'utf-8'
    html = '<h1>欢迎访问</h1>'.encode('utf-8')
    res.body = html
    return res

@python.router("/{name:str}")
@python.get("/{id:int}")
def browse_python(ctx,request:YuHeLg.Request):
    res = YuHeLg.Response()
    res.status_code = 200
    res.charset = 'utf-8'
    res.content_type = 'text/html'
    html = '<h1>欢迎学习yuhelg教育</h1>'.encode('utf-8')
    res.body = html
    return res

@python.register_preinterceptor
def show_prefix(ctx,request:YuHeLg.Request):
    print(1,"prefix = {}".format(ctx.router.prefix))
    return request

@YuHeLg.register_preinterceptor
def show_headers(ctx,request:YuHeLg.Request):
    print(2,request.path)
    print(3,request.headers)
    return request

def jsonify(**kwargs):
    content = json.dumps(kwargs)
    return YuHeLg.Response(content,"200 OK",content_type="application/json",charset="utf-8")

@YuHeLg.register_psotinterceptor
def showjson(ctx,request:YuHeLg.Request,response:YuHeLg.Response):
    body = request.body.decode()
    return jsonify(body=body)


if __name__ == '__main__':
    IP = '127.0.0.1'
    PORT = 8899
    server = make_server(IP, PORT, YuHeLg())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()