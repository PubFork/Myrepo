# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import FirstItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    #spider上定义配置信息
    custom_settings = {
        "filename":r"C:\Users\Administrator\Desktop\Python网络班学习资料\02-Python配套PPT\26Python-爬虫\books.josn"
    }

    def parse(self, response:HtmlResponse):
        subjects = response.xpath('//li[@class="subject-item"]')
        for subject in subjects:
            title = subject.css('div.info h2 a::text').extract()
            rate = subject.xpath('.//span[@class="rating_nums"]/text()').extract_first() #如果需要8分以上加一个re（'^8.*'）
            item = FirstItem()
            item['title'] = title[0].strip()
            item['rate'] = rate
            yield item