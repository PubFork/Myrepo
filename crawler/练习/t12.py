import redis

r = redis.Redis(host="192.168.0.18",port=6379,db=1)
r.setbit(20180101,1,1)
r.setbit(20180102,30,1)

r.setbit(20180103,100,1)
r.setbit(20180101,300,1)

r.bitop('or','20180101-06',20180101,20180102,20180103)
print(r.bitcount('20180101-06'))
#
# for i in range(1,365,5):
#     r.setbit('u3',i,1)
#
# for i in range(1,365,2):
#     r.setbit('u4',i,1)
#
# userlist = r.keys('u*')
#
# Au = []
# Nau = []
# for u in userlist:
#     logincount = r.bitcount(u)
#     if logincount>100:
#         Au.append((u,logincount))
#     else:
#         Nau.append((u,logincount))
#
#
# for l in Au:
#     print(l[0].decode()+' is a Active User.'+str(l[1]))
#
# for l in Nau:
#     print(l[0].decode()+' is not a Active User.'+str(l[1]))