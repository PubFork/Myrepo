# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        self.fp=open('douban.txt','a',encoding='utf-8')
    def process_item(self, item, spider):
        for i in len(item['mvname']):
            self.fp.write(item['mvname'][i]+'\n'+item['mvinfo'][i]+'\n'+item['direct'][i]+'\n'+item['rating_num'][i]+'\n'+item['mvlink'][i]+"\n\n")
        return item
        self.fp.close()

