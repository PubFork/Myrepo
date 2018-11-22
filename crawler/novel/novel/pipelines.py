# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelPipeline(object):
    def process_item(self, item, spider):
        with open(item['title']+".txt",'a',encoding='utf-8') as fp:
            count=0
            for text in item['noveldetailes']:
                count+=1
                print('正在写入{}文章中的第{}行'.format(item['title'],count))
                fp.write(text.strip())
        return item
