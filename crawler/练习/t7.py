import requests
from jsonpath import jsonpath
import json


ua = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75Safari/537.36"
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

with requests.request("GET",url,headers={'User-Agent':ua}) as res:
    text = res.text
    js = json.loads(text)
    print(js)

    rs1 = jsonpath(js,'$..title')
    print(1,rs1)

    rs2 = jsonpath(js,'$..subjects[?(@.rate > "8")]')
    print(2,rs2)

    rs3 = jsonpath(js,'$..subjects[?(@.rate > "8")].rate')
    print(2,rs3)