"""
该模块实现了post业务
title,author_id,postdate
"""
import math
import re

from model import Content, Post, session, Dig, Tag, Post_tag
from yuhelg import YuHeLg
from handler import user
from webob import exc
from util import jsonify, vaildate
import datetime
from model import Post,User

#路由
post_router = YuHeLg.Router("/post")

#发布
@post_router.post("/pub")
@user.authenticate
def pub(ctx,request:YuHeLg.Request):
    payload = request.json
    post = Post()
    try:
        post.title = payload.get("title")
        post.author_id = request.user.id
        post.postdate = datetime.datetime.now()
        cont = Content()
        cont.content = payload.get("content")
        post.content = cont
        tags = payload["tags"]
    except Exception as e:
        print(e)
        raise exc.HTTPBadRequest()

    taglist = re.split('[\s,]',tags)
    for tag in taglist:
        t = session.query(Tag).filter(Tag.tag == tag).first()
        if t is None:
            t = Tag()
            t.tag = tag
            session.add(t)
        pt = Post_tag()
        pt.tag = t
        pt.post = post
        session.add(pt)

    session.add(post)
    try:
        session.commit()
        return jsonify(post_id=post.id)
    except:
        session.rollback()
        raise exc.HTTPInternalServerError()

#查看单个博文
@post_router.get('/{id:int}')
def get(ctx,request:YuHeLg.Request):
    post_id = request.vars.id
    try:
        post = session.query(Post).filter(Post.id==post_id).one()
        post.hits +=1
        session.add(post)
        try:
            session.commit()
        except:
            session.rollback()

        #处理tags
        pts = session.query(Post_tag).filter(Post_tag.post_id == post_id).limit(10).all()
        tags = " ".join([pt.tag.tag for pt in pts])

        buryinfo, diginfo = get_digs_or_burys(post_id)
        return jsonify(post={
            'post_id':post.id,
            'title':post.title,
            'author':post.author.name,
            'postdate':post.postdate.timestamp(),
            'content':post.content.content,
            'hits':post.hits
        },diginfo=diginfo,buryinfo=buryinfo,tags=tags)
    except Exception as e:
        print(e)
        raise exc.HTTPNotFound()


def get_digs_or_burys(post_id):
    # 赞踩总数
    dig_query = session.query(Dig).filter(Dig.post_id == post_id)
    dig_count = dig_query.filter(Dig.state == 1).count()
    dig_list = dig_query.filter(Dig.state == 1).order_by(Dig.pubdate.desc()).limit(10).all()
    bury_count = dig_query.filter(Dig.state == 0).count()
    bury_list = dig_query.filter(Dig.state == 0).order_by(Dig.pubdate.desc()).limit(10).all()
    diginfo = {"count": dig_count, "user": [{"id": x.user_id, "name": x.user.name} for x in dig_list]}
    buryinfo = {"count": bury_count, "user": [{"id": x.user_id, "name": x.user.name} for x in bury_list]}
    return buryinfo, diginfo


@post_router.get('/')
@post_router.get('/user/{id:int}')
def list(ctx,request:YuHeLg.Request):
    page = vaildate(request.params,"page",int,1,lambda x,y:x if x >0 and x<101 else y)
    size = vaildate(request.params,"size",int,20,lambda x,y:x if x >0 and x<101 else y)

    #size 这里是运行浏览器端改变的，但是要控制范围。也可以不让浏览器端改变

    query = session.query(Post)
    try:
        user_id = vaildate({"user_id":request.vars.id},"user_id",int,-1,lambda x,y:x if x >0 else y )
    except:
        user_id = -1

    if user_id>0:
        query = query.filter(Post.author_id == user_id)

    try:
        count = query.count()
        posts = query.order_by(Post.id.desc()).limit(size).offset((page-1)*size).all() #offset偏移量丛集开始取

        return jsonify(posts=[{
            "post_id":post.id,
            "title":post.title
        } for post in posts],
        page_infos={
            "page":page,
            "size":size,
            "count":count,
            "pages":math.ceil(count/size)
        })
    except Exception as e:
        print(e)
        raise exc.HTTPInternalServerError()

#踩赞
def dig_or_bury(user_id,post_id,value=1):
    dig = Dig()
    dig.user_id = user_id
    dig.post_id = post_id
    dig.state = value
    dig.pubdate = datetime.datetime.now()
    session.add(dig)
    try:
        session.commit()
        return jsonify()
    except:
        session.rollback()
        return jsonify(500)

@post_router.put("/dig/{id:int}")
@user.authenticate
def dig(ctx,request:YuHeLg.Request):
    dig_or_bury(request.user.id,request.vars.id,1)

@post_router.put("/bury/{id:int}")
@user.authenticate
def bury(ctx,request:YuHeLg.Request):
    dig_or_bury(request.user.id,request.vars.id,0)