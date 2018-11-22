# -*- coding: utf-8 -*
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiciPipeline(object):
    def __int__(self):
        self.conn=pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mydatas')
    def process_item(self, item, spider):
        # DBKWARGS=spider.settings.get("DBKWARGS")
        # conn=pymysql.connect(**DBKWARGS)
        # sql="insert into proxy(IP,Port,Speed,Site,Surtime) values(item['ip'],item['port'],item['speed'],item['site'],item['surtime'])"
        # conn.query(sql)
        # conn.close()
        return item
