from bs4 import BeautifulSoup
import requests
import pymongo
import random
import re

client=pymongo.MongoClient('localhost',27017)
infos_tab=client['infos_tab']
sheet_GJdetails=infos_tab['sheet_GJdetails']
sheet_GJurls=infos_tab['sheet_GJurls']
sheet_GJLinks=infos_tab['sheet_GJLinks']

proxy_list=[
    'http://120.24.216.39:60443',
    'http://49.79.193.212:61234',
    'http://39.77.108.13:8118'
]
proxy_ip=random.choice(proxy_list)
proxies={'http':proxy_ip}


def get_page_urls(channel):
    print("----开始收集商品连接----")
    i = 1
    flag = False
    links = []
    for i in range(1, 200):
        url = channel+"/o"+str(i)+"/"
        pat = 'http://bj.ganji.com/(.*?)/.*?/'
        tag = re.compile(pat).findall(url)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        test = soup.select('ul li a span')
        if wb_data.status_code == 404:
            print('cuowu')
        else:
            for text in test:
                if '下一页' in text:
                    url1 = soup.select("td.t a.t")
                    for url in url1:
                        a=url.get('href')
                        if tag[0] in str(a):
                            link = url.get('href')
                            links.append(link)
                            sheet_GJLinks.insert_one({"link":link})
                            print('插入连接')
                        else:
                            print('meiyou')
                    flag = True
                else:
                    url = channel+"/o"+str(i+1)+"/"
                    wb_data = requests.get(url)
                    soup = BeautifulSoup(wb_data.text, 'lxml')
                    test = soup.select('ul li a span')
                    url1 = soup.select("td.t a.t")
                    for url in url1:
                        if tag[0] in str(url):
                            link = url.get('href')
                            sheet_GJLinks.insert_one({"link": link})
                            links.append(link)
                            print('插入连接')
                    flag=False

            if flag == True:
                i += 1
            else:
                break
    return links
    print('----收集完成----')

if __name__ == '__main__':
    page_urls=[item['url'] for item in sheet_GJurls.find()]
    for url in page_urls[1:]:
        try:
            links=get_page_urls(url)
        except IndexError:
            pass
    get_item_info_from()