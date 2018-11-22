# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from xici.items import XiciItem
import time
import random

class XicispiderSpider(scrapy.Spider):
    name = 'xicispider'
    allowed_domains = ['xicaidaili.com']
    # start_urls = ['http://www.xicaidaili.com/']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }

    def start_requests(self):
        '''初始url请求返回reponse给解析函数'''
        for i in range(1,664):
            url='http://www.xicidaili.com/nt/'+str(i)
            yield Request(url,headers=self.header,callback=self.parse)

    def parse(self, response):
        '''解析每一个url返回的rasponse'''
        ip_list = response.xpath('//table[@id="ip_list"]/tr')
        pre_item = XiciItem()
        for ip in ip_list[1:]:
            pre_item['ip'] = ip.xpath('td[2]/text()')[0].extract()
            pre_item['port'] = ip.xpath('td[3]/text()')[0].extract()
            pre_item['speed'] = ip.xpath('td[7]/div/@title')[0].extract()
            pre_item['site'] = ip.xpath('string(td[4]/a/text())').extract()[0].strip()
            pre_item['surtime'] = ip.xpath('td[9]/text()')[0].extract()
            print(pre_item)
        return pre_item


