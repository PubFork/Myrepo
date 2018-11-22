# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QsbkPipeline(object):
    def __init__(self):
        self.fp=open(r'C:\Users\Administrator\PycharmProjects\untitled\1.txt','a')

    def process_item(self, item, spider):
        self.fp.write(item['content'])
        # for i in len(item['content']):
        #     print(item['content'][i])
        #     # print(item['link'][i])
        #     # print(item['data'][i])
        return item
    def close_spider(self):
        self.fp.close()