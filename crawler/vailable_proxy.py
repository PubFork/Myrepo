# encoding = utf8
import time
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import socket
import requests
import re
from concurrent.futures.thread import ThreadPoolExecutor


class GetIp():
    def __init__(self):
        self.User_Agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        self.verify_url = "http://myip.ipip.net/"
        self.urls = []
        self.proxy = []

    #创建url
    def create_urls(self,n):
        for i in range(n):
            url = 'http://www.xicidaili.com/nn/' + str(i)
            self.urls.append(url)
        return self.urls

    #获取代理ip
    def get_proxy_ip(self,n):
        proxies = {'http': 'http://125.70.13.77:8080'}
        for url in self.create_urls(n):
            try:
                html = requests.get(url,headers={'User-Agent':self.User_Agent},proxies=proxies).text
                soup = BeautifulSoup(html,'lxml')
                print(soup)
                for ip in soup.find_all('tr'):
                    tds = ip.find_all("td")
                    print(tds)
                    ip_temp = ":".join([tds[1].contents[0],tds[2].contents[0]])
                    self.proxy.append(ip_temp)
                    print('get ip ')
            except Exception as e:
                print(e)
                continue
        return self.proxy

    #验证获得的代理IP地址是否可用
    def verify_ip(self,proxies):
        with open("E:\ip.txt", "w") as f:
            socket.setdefaulttimeout(3)
            for proxy in proxies:
                try:
                    proxy_temp = {"http": "http://{}".format(proxy.strip())}
                    res = requests.get(self.verify_url,proxies=proxy_temp,timeout=2)
                    if re.compile('^当前').search(res.text):
                        f.write("http://"+proxy + '\n')
                        print('success.........')
                except Exception as e:
                    continue



if __name__ == '__main__':
    getip = GetIp()
    proxies = getip.get_proxy_ip(2)
    getip.verify_ip(proxies)


