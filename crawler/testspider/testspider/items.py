# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    rate = scrapy.Field()
    count = scrapy.Field()

    def __repr__(self):
        return "{} {}".format(self.__class__.__name__,dict(self))
