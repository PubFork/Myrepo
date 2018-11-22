# -*- coding: utf-8 -*-
import pymongo
import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TaobaoPipeline(object):
    def __int__(self):
        self.conn=sqlite3.connect(taobao.sqlite3)
        self.cu=self.conn.cursor()
    def process_item(self, item, spider):
        sql='insert into infos(url) values({})'.format(item['url'])
        self.cu.execute(sql)
        self.conn.commit()

        return item
    def close_spider(self):
        self.conn.close()