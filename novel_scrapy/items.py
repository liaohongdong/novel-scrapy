# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()


class NovelMenuItem(scrapy.Item):
    book_type = scrapy.Field()
    book_id = scrapy.Field()
