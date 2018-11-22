from bs4 import BeautifulSoup
import requests
import pymongo
import getchannel_list
import time
import random
from selenium import webdriver

client=pymongo.MongoClient('localhost',27017)
infos_tab=client['infos_tab']
sheet_58infos=infos_tab['sheet_58infos']

# proxy_list=[
#     'http://111.1.32.51:8088',
#     'http://106.120.108.163:3128',
#     'http://110.84.129.27:8888'
# ]
# proxy_ip=random.choice(proxy_list)
# proxies={'http':proxy_ip}

# def getweb(link):
#     driver = webdriver.PhantomJS()
#     driver.get(link)
#     url = driver.current_url
#     print(url)
#     item_link=url.split('?')[0]
#     print(item_link)
#     sheet_58infos.insert_one({'url': item_link})

def get_links_from(channel,page,who_sells=0):
    page_url='{}{}/pn{}/'.format(channel,str(who_sells),str(page))
    wb_data=requests.get(page_url)
    time.sleep(2)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            # #     url = link.get('href').split('?')[1]
            # #     if 'szqLIL08PH98' in url:
            #         pass
            #     else:
            #         url=link.get('href')
            if 'detail' not in item_link:
            #         getweb(url)
                pass
            else:
                sheet_58infos.insert_one({'url': item_link})
            # return urls
    else:
        # It's the last page !
        pass


def get_item_info_from(url,data=none):
    wb_data=requests.get(url)

    if wb_data.status_code==404:
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        data={
            'title':soup.title.text.strip(),
            'price':soup.select('span.price.c_f50')[0].text.strip(),
            'pub_data':soup.select('li.time')[0].text.strip().split(' ')[0],
            'area':soup.select('span.c_25d>a')[0].text.strip(),
            'url':url

        }
        print(data)


if __name__ == '__main__':
    url='http://bj.58.com/sale.shtml'
    links=getchannel_list.get_channel(url)
    for channel in links:
        for page in range(0, 101):
            parsepage(channel,page)