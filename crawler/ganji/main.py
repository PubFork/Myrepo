from multiprocessing import Pool
from parsing_page import get_page_urls
from ganji.get_channel_list import get_channel
import pymongo
from bs4 import BeautifulSoup
import requests
import re


client=pymongo.MongoClient('localhost',27017)
infos_tab=client['infos_tab']
sheet_GJinfos=infos_tab['sheet_GJinfos']
sheet_GJLinks=infos_tab['sheet_GJLinks']
sheet_GJurls=infos_tab['sheet_GJurls']

def getLinks():
    links=[item['link'] for item in sheet_GJLinks.find()]
    return links

def get_item_info_from(url,data=None):
    print("----开始收集商品----")
    # page_urls = [item['link'] for item in sheet_GJLinks.find()]
    pat='http://bj.ganji.com/.*?/(.*?).htm'

    # for url in page_urls:
    try:
        tag=re.compile(pat).findall(url)
        if len(tag)>0:
            wb_data=requests.get(url)
            soup=BeautifulSoup(wb_data.text,'lxml')
            title=soup.title.text.strip()
            price = soup.select(" ul li i.f22.fc-orange.f-type")[0].text
            contact = soup.select("ul li span.phoneNum-style")[0].text.strip()
            pub_data=soup.select("li i.pr-5")[0].text.strip().split(" ")[0]
            area=list(map(lambda x:x.text.strip(),soup.select("ul.det-infor li:nth-of-type(2) a")))
            data={
            'title':title,
            'pub_data':pub_data,
            'area':area,
            'page_url':url
            }
            sheet_GJinfos.insert_one(data)
            print('插入数据')
        else:
            pass
    except Exception as e:
       print(e)

    print('----收集完成----')

if __name__ == '__main__':
    url = 'http://bj.ganji.com/wu/'
    get_channel(url)
    page_urls=[item['url'] for item in sheet_GJurls.find()]
    for url in page_urls[1:]:
        try:
            links=get_page_urls(url)
        except IndexError:
            pass
    pool=Pool()
    links=getLinks()
    pool.map(get_item_info_from,links)