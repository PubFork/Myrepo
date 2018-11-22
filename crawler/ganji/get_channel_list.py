from bs4 import BeautifulSoup
import requests
import pymongo

client=pymongo.MongoClient('localhost',27017)
infos_tab=client['infos_tab']
sheet_GJurls=infos_tab['sheet_GJurls']

def get_channel(url):
    host_url = 'http://bj.ganji.com'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    channel_name = soup.select('dl.fenlei dt a')
    channel_list = []
    for channel in channel_name:
        channel_url = channel.get('href')
        link = host_url + channel_url
        channel_list.append(link)
        sheet_GJurls.insert_one({"url":link})
    return channel_list





if __name__ == '__main__':
    host_url = 'http://bj.ganji.com'
    url='http://bj.ganji.com/wu/'
    get_channel(url)