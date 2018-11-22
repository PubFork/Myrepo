# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import RedisspiderItem
from scrapy_redis.spiders import RedisCrawlSpider

class DoubanbookSpider(RedisCrawlSpider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    #        = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        comment = '//div[@class="comment-item"]//span[@class="short"]/text()'
        reviews = response.xpath(comment).extract()
        for review in reviews:
            item = RedisspiderItem()
            print(review.strip())
            item['comment'] = review.strip()
            yield item
