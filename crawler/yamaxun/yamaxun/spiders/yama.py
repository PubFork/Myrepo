# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yamaxun.items import YamaxunItem
import re
from scrapy.http import Request
import requests

class YamaSpider(CrawlSpider):
    name = 'yama'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://www.amazon.cn/']
    header={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }
    def start_requests(self):
        yield Request('http://www.amazon.cn/',headers=self.header)

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def start_requests(self):
        return [Request('http://www.amazon.cn/',headers=self.header)]

    def parse_item(self, response):
        try:
            pat='https://www.amazon.cn/dp/(.*?)/ref=.*?'
            a=re.compile(pat).findall(response.url)
            if len(a)==1:
                link='https://www.amazon.cn/dp/'+str(a[0])
                i = YamaxunItem()
                i['price'] = response.xpath('/html/body/div[2]/div/div[7]/div[6]/div[11]/div/table/tbody/tr[1]/td[2]/text()').extract()
                i['comment'] = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()
                print(i['price']+i['comment'])
                yield i
            else:
                pass
        except Exception as e:
            print(e)

        # try:
        #     thisurl=response.url
        #     pat='https://www.amazon.cn/dp/(.*?)//ref=.*?'
        #     x=re.compile(pat).findall(thisurl)
        #     if(x):
        #         thisid=re.compile(pat).findall(thisurl)[0]
        #         print(thisid)
        #         # i = JdstoreItem()
        #         # i['title'] = response.xpath('//html/head/title').extract()[0]
        #         # i['content'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
        #         # i['shopname'] = response.xpath('//a[@clstag="shangpin|keycount|product|dianpuname1"]/@title').extract()[0]
        #         # comment_url='https://club.jd.com/comment/productCommentSummaries.action?referenceIds={}'.format(str(thisid))
        #         # price_url='https://p.3.cn/prices/mgets?skuIds=J_{}'.format(str(thisid))
        #         # data = requests.get(comment_url).text
        #         # data1 = requests.get(price_url).text
        #         # i['comment'] = re.search('"CommentCountStr":"(.*?)"', data, re.S).group(1)
        #         # i['goodrate'] = re.search('"GoodRateShow":(.*?),', data, re.S).group(1)
        #         # i['price'] = re.search('"p":"(.*?)"', data1, re.S).group(1)
        #         # return i
        #         # i['link'] = response.xpath('//div[@class="p-name"]/a/@href"]').extract()
        #         # i['sales'] = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()
        #         # if len(i['title']) and len(i['content']) and i['shopname'] and i['goodrate'] and i['price'] and i['comment']:
        #         #     print( i['title']+"\n"+i['shopname']+"\n"+i['content']+"\n"+i['comment']+"\n"+i['goodrate']+"\n"+i['price']+"\n\n" )
        #         # else:
        #         #     print('buquan')
        #     else:
        #         pass
        # except Exception as e:
        #     print(e)