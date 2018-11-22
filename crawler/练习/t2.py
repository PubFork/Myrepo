import random
from urllib.request import Request,urlopen
from urllib.parse import urlencode

keyword = input("搜所关键字>>>:")
data = urlencode({'q':keyword})

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/57.0.2987.133 Safari/537.36",# chrome,
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko)Version/5.0.1 Safari/537.36", # safafi,
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", # Firefox
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" # IE
]


url = 'http://www.bing.com/search?{}'.format(data)
request = Request(url)
request.add_header('User-Agent',random.choice(ua_list))

response = urlopen(request,timeout=20)
with response:
    with open(r'C:\Users\Administrator\Desktop\temp\bing.html','wb') as f:
        f.write(response.read())

