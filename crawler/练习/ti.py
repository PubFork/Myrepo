# from urllib.request import urlopen
#
# #打开一个URL返回一个响应文件，类文件对象
# response = urlopen('http://www.bing.com')
# print(response.closed)
#
# with response:
#     print(type(response))
#     print(response.status,response.reason)
#     print(response.geturl())
#     print(response.info())
#     print(response.read())
#
# print(response.closed)

#urlopen方法虽然能传递url和data这样的数据，不能构造HTTP的请求，例如useragent，这时需要使用Resquest
from urllib.request import urlopen,Request
import random
import ssl
url = 'https://www.12306.cn/mormhweb/'

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/57.0.2987.133 Safari/537.36",# chrome,
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version/5.0.1 Safari/537.36", # safafi,
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", # Firefox
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" # IE
]

ua = random.choice(ua_list)#pick one
#使用连接池
import urllib3
with urllib3.PoolManager() as http:
    response = http.request("GET",url,headers={"User-Agent",ua})

# request = Request(url)
# request.add_header("User-Agent",ua)
#
# context = ssl._create_unverified_context()
# response = urlopen(request,timeout=20,context=context)#url 和 request对象都可以传入
#



# with response:
#     print(response.geturl())
#     print(response.status)
#     print(response.info())
#     print(response.reason)
#
# print(request.get_header("User-agent"))
# print("user-agent".capitalize())