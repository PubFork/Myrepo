from getchannel_list import get_channel
from multiprocessing import Pool
from parsing_page import parsepage


def get_link_from(channel):
        for page in range(0, 101):
            parsepage(channel,page)

if __name__ == '__main__':
    url = 'http://bj.58.com/sale.shtml'
    channel_list=get_channel(url)
    pool=Pool()
    pool.map(get_link_from,channel_list)