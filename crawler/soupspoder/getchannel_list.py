from bs4 import BeautifulSoup
import requests

def get_channel(url):
    host_url = 'http://bj.58.com'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    channel_name = soup.select('#ymenu-side > ul > li > ul > li > b > a')
    channel_list = []
    for channel in channel_name:
        channel_url = channel.get('href')
        link = host_url + channel_url
        channel_list.append(link)
    return channel_list





if __name__ == '__main__':
    host_url = 'http://bj.58.com'
    url='http://bj.58.com/sale.shtml'
    get_channel(url)