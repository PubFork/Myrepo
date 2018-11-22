# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ..items import TaobaoItem
import random


class ChannlSpider(CrawlSpider):
    name = 'channl'
    allowed_domains = ['taobao.com']
    # start_urls = ['http://taobao.com/']
    proxies = [
        'HTTP://114.226.128.202:6666',
        'HTTP://27.40.151.127:61234',
        'HTTP://121.40.80.159:808',
    ]
    proxy = random.choice(proxies)

    header={
        'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request('http://taobao.com/',headers=self.header,meta={'proxes':self.proxy})
    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item=TaobaoItem()
        pat='https://item.taobao.com/item.htm.*?'
        tag=re.compile(pat).findall(response.url)
        if tag:
            item['url']=response.url
            print(item['url'])
        else:
            print('buzhuzai')