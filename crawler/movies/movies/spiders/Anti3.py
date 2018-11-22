# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class Anti3Spider(RedisCrawlSpider):
    name = 'Anti3'
    allowed_domains = ['iqiyi.com']
    # start_urls = ['http://iqiyi.com/']
    # https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.0.0&authcookie=null&business_type=17&content_id=1056394800&hot_size=10&last_id=&page=1&page_size=40
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
