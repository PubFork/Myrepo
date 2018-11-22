import requests
from lxml import etree

ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
url = 'https://movie.douban.com/'

response = requests.request("GET",url,headers={"User-Agent":ua})
with response:
    web_text = response.text
    html = etree.HTML(web_text)
    title = html.xpath("//li [@class='title']/a/text()")
    print(title)