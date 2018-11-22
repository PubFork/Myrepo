# -*- coding: utf-8 -*-
import scrapy
import re
from novel.items import NovelItem

class NoveldescSpider(scrapy.Spider):
    name = 'noveldesc'
    allowed_domains = ['17k.com']
    start_urls = ['http://www.17k.com']

    def parse_home_page(self, response):
        links=response.xpath("//div[@class='Nav']/div/a/@href").extract()
        for url in links:
            yield scrapy.Request(url,callback=self.get_novel_channel_url)

    def get_novel_channel_url(self,response):
        novelurls = response.xpath("//ul[@class='BOX Top1']/li/a/@href").extract()
        for url in novelurls:
            pat = "http://www.17k.com/book/(.*?).html"
            id=re.compile(pat).findall(url)
            if len(id):
                dece_url='http://www.17k.com/list/{}.html'.format(id[0])
                yield scrapy.Request(dece_url,callback=self.get_novel_page_url)

    def get_novel_page_url(self,response):
        novelurls=response.xpath("//dl[@class='Volume']/dd/a/@href").extract()
        for url in novelurls:
            desc_url="http://www.17k.com{}".format(url)
            yield scrapy.Request(desc_url, callback=self.parse_page_infos)


    def parse_page_infos(self,response):
        item=NovelItem()
        item['noveldetailes'] = response.xpath('//div[@class="p"]/text()').extract()
        item['title'] = response.xpath('//div[@class="readAreaBox content"]/h1/text()').extract()
        yield item





