from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from queue import Queue
import requests
import logging
import threading
import time

#设定打印日志级别
FORMAT = '%(actime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

#创建url
#https://news.cnblogs.com/n/page/2/
Base_Url = 'https://news.cnblogs.com'
Name_Page = '/n/page/'

#使用池，以后可以使用第三方消息队列
urls = Queue() #url队列
htmls = Queue() #响应数据队列
outputs = Queue() #结果输出队列

event = threading.Event()

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}

def create_urls(start,end,step=1):
    for i in range(start,end+1,step):
        urls.put("{}{}{}/".format(Base_Url,Name_Page,i))
    print('url 创建完成')

#获取页面数据
def crawler():
    while not event.is_set():
        try:
            url = urls.get(True,1)
            with requests.get(url,headers=headers) as f:
                htmls.put(f.text)
        except Exception as e:
            # logging.info(e)
            pass

#解析页面元素
def parse():
    while not event.is_set():
        try:
            html = htmls.get(True,1)
            soup = BeautifulSoup(html,'lxml')
            diggs = soup.select('div.diggit > span')
            for digg in diggs:
                textq = digg.get('id')
                print(textq)
            titles = soup.select('div.content > h2 a')
            for title in titles:
                text = title.text
                val = text,Base_Url+title.get('href')
                outputs.put(val)
        except Exception as e:
            # logging.info(e)
            pass

#持久化线程函数
def save(path):
    with open(path,'a+') as f:
        while not event.is_set():
            try:
                text,url = outputs.get(True,1)
                f.write("{} {}\n".format(text,url))
                f.flush()
            except Exception as e:
                # logging.info(e)
                pass


#线程池
executor = ThreadPoolExecutor(10)
executor.submit(create_urls,1,10)
executor.submit(parse)
executor.submit(save,'C:/data/blogs.txt')

for i in range(7):
    executor.submit(crawler)

#终止条件
while True:
    inp = input(">>>")
    if inp =='quit':
        event.set()
        print('closing...')
        time.sleep(4)
        break
