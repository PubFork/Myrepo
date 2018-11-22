# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from JDstore.items import JdstoreItem
import re
from scrapy.http import Request
import requests

class JdgoodsSpider(CrawlSpider):
    name = 'ganji2'
    allowed_domains = ['ganji.com']
    # start_urls = ['https://www.jd.com/']
    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )
    header={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }
    def start_requests(self):
        return [Request('http://www.bj.ganji.com',headers=self.header)]

    def parse_item(self, response):
        try:
            thisurl = response.url
            pat = 'http://bj.ganji.com/(.*?).htm'
            tag = re.compile(pat).findall(thisurl)
            print(tag)
            # thisurl=response.url
            # pat='https://item.jd.com/(.*?).html'
            # x=re.compile(pat).findall(thisurl)
            # if(x):
            #     thisid=re.compile(pat).findall(thisurl)[0]
            #     i = JdstoreItem()
            #     i['title'] = response.xpath('//html/head/title').extract()[0]
            #     # print(i['title'] )
            #     i['content'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
            #     # print(i['content'])
            #     i['shopname'] = response.xpath('//a[@clstag="shangpin|keycount|product|dianpuname1"]/@title').extract()[0]
            #     # print(i['shopname'])
            #     comment_url='https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}'.format(str(thisid))
            #     price_url='https://p.3.cn/prices/mgets?callback=jQuery5488277&type=1&area=1_72_4137_0&pdtk=&pduid=1510968015061901022163&pdpin=&pin=null&pdbp=0&skuIds=J_{}&ext=11000000&source=item-pc'.format(str(thisid))
            #     # print(price_url)
            #     data = requests.get(comment_url,headers=self.header).text
            #     data1 = requests.get(price_url,headers=self.header).text
            #     i['comment'] = re.search('"CommentCountStr":"(.*?)"', data, re.S).group(1)
            #     # print(i['comment'])
            #     i['goodrate'] = re.search('"GoodRateShow":(.*?),', data, re.S).group(1)
            #     # print(i['goodrate'])
            #     i['price'] = re.search('"p":"(.*?)"', data1, re.S).group(1)
            #     if len(['title']) and len(i['content']) and len(i['shopname']) and len(i['comment']) and len(i['goodrate']) and len(i['price']):
            #         yield i
            #     else:
            #         pass
            # else:
            #     pass
        except Exception as e:
            print("报错为:s%"%e)