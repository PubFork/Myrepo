# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class YamaxunPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='jd')

    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='localhost',
            user="root",
            passwd="123456",
            db='jd',
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

        cursor = conn.cursor()
        with conn.cursor() as cursor:
            price = item['price']
            comment = item['comment']
            sql_2 = "insert into ysw(sales,title) values(%s, %s);"
        try:
            cursor.execute(sql_2, (price, comment))
            conn.commit()
        except Exception as e:
            print(e)

        return item
