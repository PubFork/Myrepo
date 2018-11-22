# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from qsbk.items import QsbkItem
from scrapy.selector import Selector
import time

class QoushiSpider(CrawlSpider):
    name = 'qoushi'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/']
    def start_requests(self):
        ua={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
        yield scrapy.Request('http://qiushibaike.com/',headers=ua)
        time.sleep(10)


    rules = (
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = QsbkItem()
        selector=Selector(response)
        i['content'] = selector.xpath('//*[@id="single-next-link"]/div/text()').extract()
        # i['link'] = response.xpath('//div[@id="qiushi_tag_120320318"]/@href').extract()
        # i['data'] = response.xpath('//i[@class="number"]').extract()
        print(i['content'])
        return i
        time.sleep(10)
