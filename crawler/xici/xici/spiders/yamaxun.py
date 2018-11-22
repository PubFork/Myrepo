# -*- coding: utf-8 -*-
import scrapy
from xici.items import XiciItem
from scrapy.http import Request
import re



class XicispiderSpider(scrapy.Spider):
    name = 'yama'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }
    start_urls={'https://www.amazon.cn'}

    def parse(self, response):
        '''解析每一个url返回的rasponse'''
        goods_lists = re.findall('"url":"(.*?)"',response.text)
        links=[]
        for goods_list in goods_lists:
            if "desktop" not in goods_list:
                link='https://www.amazon.cn'+goods_list
                links.append(link)
            elif "dp" in goods_list:
                link = 'https://www.amazon.cn' + goods_list
                links.append(link)
            else:
                pass
            yield Request(link,callback=self.page,headers=self.header)

    def page(self,response):
        links = response.xpath('//a/@href').extract()
        for link in links:
            print(link)
            if "dp" in link.split('/'):
                print(link)