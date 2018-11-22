# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from redis import Redis
import json
import pymongo

class FirstPipeline(object):
    def __init__(self):#全局设置
        print('~~~~~~~~~~~~~init~~~~~~~~~~~~~~~~~')

    def open_spider(self,spider):
        print("{}........".format(spider))
        print(spider.settings['filename'])
        self.file = open(spider.settings['filename'],'w',encoding='utf-8')
        self.file.write('[\n')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item))+',\n')
        return item

    def close_spider(self,spider):
        self.file.write(']')
        self.file.close()
        print('{}==============='.format(spider))
