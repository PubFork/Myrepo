import config

from wsgiref import simple_server

from yuhelg import YuHeLg
from handler import user, post

if __name__ == '__main__':
    #Application
    application = YuHeLg()

    #注册Application中
    YuHeLg.register(user.user_router)
    YuHeLg.register(post.post_router)

    #ＷＳＧＩ　Ｓｅｒｖｅｒ
    server = simple_server.make_server(config.WSIP, config.WSPORT, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()
