import datetime
import config
from util import jsonify
from yuhelg.Web import YuHeLg
from model import User,session
from webob import exc
import jwt
import bcrypt


#用户路由要注册
user_router = YuHeLg.Router("/user")

#验证装饰器
def authenticate(fn):
    def wrapper(ctx,request):
        try:
            jwtstr = request.headers.get('jwt')
            print(jwtstr)
            payload = jwt.decode(jwtstr, config.AUTHORIZE_SECRET, algorithms=['HS256'])

            #是否过期
            if (datetime.datetime.now().timestamp()-payload.get('timestamp')) > config.EXPIRED:
                raise exc.HTTPUnauthorized()
            user = session.query(User).filter(User.id == payload.get('user_id',None)).first()
            if (user is None):
                raise exc.HTTPUnauthorized
            request.user = user
        except Exception as e:
            print(e)
            raise exc.HTTPUnauthorized()
        return fn(ctx,request)
    return wrapper

#生成token
def gen_token(user_id):
    return jwt.encode({"user_id":user_id,
                       "timestamp":int(datetime.datetime.now().timestamp())
                       }, config.AUTHORIZE_SECRET, algorithm='HS256').decode()

@user_router.post("/reg")
def register(ctx,request:YuHeLg.Request):
    payload = request.json #email,pwd,name
    email = payload.get("email")

    #验证邮箱是否唯一
    if session.query(User).filter(User.email == email).first() is not None:
        raise exc.HTTPConflict("{} already exists".format(email))

    user = User()
    try:
        user.name = payload.get("name")
        user.email = payload.get("email")
        user.password = bcrypt.hashpw(payload.get("password").encode(), bcrypt.gensalt())

    except Exception as e:
        print(e)
        exc.HTTPBadRequest()

    session.add(user)

    try:
        session.commit()
        res = jsonify(user={
            'id': user.id,
            'name': user.name
        }, token=gen_token(user.id))
        print(res)
        return res
    except:
        session.rollback()
        raise exc.HTTPInternalServerError()



@user_router.post("/login")
@authenticate
def login(ctx,request:YuHeLg.Request):
    payload = request.json
    email = payload.get('email')
    user = session.query(User).filter(User.email == email).first()

    if user and bcrypt.checkpw(payload.get('password').encode(), user.password.encode()):
        return jsonify(user={
            'id':user.id,
            'name':user.name,
            'email':user.email
        },token=gen_token(user.id))
    else:
        raise exc.HTTPUnauthorized()


