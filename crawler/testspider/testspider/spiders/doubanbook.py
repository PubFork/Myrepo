# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TestspiderItem
from scrapy.http.response.html import HtmlResponse

class DoubanbookSpider(CrawlSpider):
    # handle_httpstatus_list = [301, 302]
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    custom_settings = {
        "filename": r"C:\Users\Administrator\Desktop\Python网络班学习资料\02-Python配套PPT\26Python-爬虫\books1.josn"
    }

    def parse_item(self, response:HtmlResponse):
        for subject in response.xpath('//li[@class="subject-item"]'):
            item = TestspiderItem()
            item['title'] = subject.css('div.info h2 a::text')[0].extract().strip()
            item['rate'] = subject.xpath('.//span[@class="rating_nums"]/text()').extract_first()
            item['count'] = subject.xpath('.//span[@class="pl"]/text()')[0].extract().strip().strip('(,)')
            yield item


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['ipip.net']
    start_urls = ['https://myip.ipip.net/']

    def parse(self, response):
        text = response.text
        print(text)