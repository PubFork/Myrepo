import random
from urllib.request import Request,urlopen
from urllib.parse import urlencode
import simplejson
import json


ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/57.0.2987.133 Safari/537.36",# chrome,
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version/5.0.1 Safari/537.36", # safafi,
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", # Firefox
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" # IE
]


url = 'http://httpbin.org/post'
request = Request(url)
request.add_header('User-Agent',random.choice(ua_list))

data = urlencode({'name':'张三,@=/&*','age':'18'})

response = urlopen(request,data=data.encode())
with response:
    # with open(r'C:\Users\Administrator\Desktop\temp\bing.html','wb') as f:
    html = response.read()
    text = simplejson.loads(html)
    print(text)
    print(text.get('headers'))

'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0%E7%83%AD%E9%97%A8'