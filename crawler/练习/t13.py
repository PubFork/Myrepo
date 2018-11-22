#有序集合的应用
import redis

r = redis.Redis('192.168.0.18')

r.zadd('mboard','yellow',1,'rolling in the deep',1,"happy",1,'just the way you are',1)
r.zadd('mboard','eye of the tigger',1,'billie jean',1,'say you say me',1,'payphone',1)
r.zadd('mboard','my heart will go on',1,'when you believe',1,'hero',1)

r.zincrby('mboard','yellow',50)
r.zincrby('mboard','rolling in the deep',60)
r.zincrby('mboard','my heart will go on',60.8)
r.zincrby('mboard','when you believe',70)
r.zincrby('mboard','say you say me',70.9)

allmusic = r.zrange('mboard',0,-1,withscores=True)
print(type(allmusic))
for m in allmusic:
    print(m)

print('欧美排行榜')
musicboard = r.zrevrange('mboard',0,9,withscores=True)
for i ,m in enumerate(musicboard):
    print(i+1,*m)

r.zadd('blog','今天天气不错',1407000000)
r.zadd('blog','今天学习redis',1450000000)
r.zadd('blog','学习redis',1560000000)

print(r.zrevrange('blog',1,2))

r.zadd('bk:it:01','java',50,'redis',20,'hadoop',40)
r.zadd('bk:it:02','java',70,'redis',30,'hadoop',20)
r.zadd('bk:it:03','java',20,'redis',30,'hadoop',5)

r.zunionstore('bk:it:01-03',('bk:it:01','bk:it:02','bk:it:03'),aggregate='MAX')
print(r.zrange('bk:it:01-03',0,-1,withscores=True))