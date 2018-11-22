# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
import time

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        i = QsbkItem()
        i['content'] = response.xpath('//div[@class="content"]/span/text()').extract()
        # i['link'] = response.xpath('//div[@id="qiushi_tag_120320318"]/@href').extract()
        # i['data'] = response.xpath('//i[@class="number"]').extract()
        print(i['content'])
        return i
