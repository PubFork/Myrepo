# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class GanjiSpider(CrawlSpider):
    name = 'ganji'
    allowed_domains = ['ganji.com']
    start_urls = ['http://www.bj.ganji.com']

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }
    # def start_requests(self):
    #     return [Request('http://bj.ganji.com/zhaopin/',callback=self.parse_item,headers=self.header)]

    def parse_item(self, response):
        pat='http://bj.ganji.com/(.*?)x.htm'
        tag=re.compile(pat).findall(response.url)
        print(tag)
        # if tag:
        #     i = {}
        #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #     #i['name'] = response.xpath('//div[@id="name"]').extract()
        #     #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i