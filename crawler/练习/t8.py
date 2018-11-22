import requests

url = "https://www.oschina.net/"

# headers = {
# 'Host': 'www.oschina.net',
# 'Connection': 'keep-alive',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Referer': 'https://www.oschina.net/home/login?goto_page=https%3A%2F%2Fwww.oschina.net%2F',
# 'Accept-Encoding': 'gzip, deflate, sdch, br',
# 'Accept-Language': 'zh-CN,zh;q=0.8',
# 'Cookie': '_user_behavior_=aa577301-2a2f-4346-b90a-02c2517db162; aliyungf_tc=AQAAAGejBhSCsQ4A2F29G7UkIM+PnJM3; _reg_key_=StnMwLrDzC6t9nfW9u31; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1539155274,1540347824,1540348427,1540350420; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1540363044; oscid=lue7caauFgahZsGGvzVSdEwyOIorEEMFM%2Bct8wSG%2Fy4gy94qK5eSaDoaXwEAI75nXKpM29W6z8jVerCHV4fvE%2F%2BATkOqs3Yq7Yptz3SUkmr8jb0T%2F3uEHDWxAPr76QqO8VGfktKnAfGAIn8KXBtLIZxbib71HxYv'
# }
headers={
    
}
response = requests.request("GET", url, headers=headers)

print(response.text)
filename = 'C:/test.html'
with open(filename,'w',encoding="utf-8") as f:
    f.write(response.text)
    f.flush()



































