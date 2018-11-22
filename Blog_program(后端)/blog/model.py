from sqlalchemy import Column, create_engine, String, BigInteger, Integer, ForeignKey, DateTime
from sqlalchemy import UniqueConstraint,PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT,TINYINT
import config

#基类
Base = declarative_base()

#实体类
class User(Base):
    __tablename__ = 'user'

    id  = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    name = Column(String(48),nullable=False)
    email = Column(String(64),nullable=False,unique=True)
    password = Column(String(128),nullable=False)

    def __repr__(self):
        return "<User id = {} name = {} email = {}>".format(self.id,self.name,self.email)


class Post(Base):
    __tablename__ = 'post'

    id  = Column(BigInteger,primary_key=True,autoincrement=True)
    title = Column(String(255),nullable=False)
    author_id = Column(Integer,ForeignKey("user.id"),nullable=False)
    postdate = Column(DateTime,nullable=False)
    hits = Column(BigInteger,nullable=True,default=0,index=True)

    author = relationship("User")
    content = relationship("Content",uselist=False)

    def __repr__(self):
        return "<User id = {} title = {} postdate = {}>".format(self.id,self.title,self.postdate)


class Content(Base):
    __tablename__ = 'content'

    id  = Column(BigInteger,ForeignKey("post.id"),primary_key=True)
    content = Column(LONGTEXT,nullable=True)

    def __repr__(self):
        return "<User id = {} content = {}>".format(self.id,self.content[:20])

class Dig(Base):
    __tablename__ = "dig"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('user.id'),nullable=False,index=True)
    post_id = Column(BigInteger,ForeignKey("post.id"),nullable=False,index=True)
    state = Column(TINYINT,nullable=False)
    pubdate = Column(DateTime,nullable=True)

    __table_args__ = (
        UniqueConstraint("user_id","post_id",name="unq_user_post"),
    )

    user = relationship("User")

    def __repr__(self):
        return "<User id = {} state = {}>".format(self.id,self.state)

class Tag(Base):
    __tablename__ = "tag"

    id = Column(BigInteger,primary_key=True,autoincrement=True)
    tag = Column(String(16),nullable=False,unique=True)

class Post_tag(Base):
    __tablename__ = "post_tag"

    post_id = Column(BigInteger, ForeignKey("post.id"), nullable=False)
    tag_id = Column(BigInteger,ForeignKey('tag.id'),nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('post_id',"tag_id"),
    )

    post = relationship("Post")
    tag = relationship("Tag")

    def __repr__(self):
        return "<User id = {} state = {}>".format(self.post_id,self.tag_id)

#连接数据库
engine = create_engine(config.URL, echo=config.DATABASE_DEBUG)

#创建删除表
def create_all():
    Base.metadata.create_all(engine)

def drop_all():
    Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
