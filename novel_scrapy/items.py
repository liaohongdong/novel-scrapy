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


class NovelBookItem(scrapy.Item):
    book_name = scrapy.Field()
    book_type = scrapy.Field()
    classify_1 = scrapy.Field()
    classify_2 = scrapy.Field()
    font_num = scrapy.Field()
    book_status = scrapy.Field()
    author_name = scrapy.Field()
    intro = scrapy.Field()


class MNovelBookItem(scrapy.Item):
    book_name = scrapy.Field()
    book_type = scrapy.Field()
    classify_1 = scrapy.Field()
    classify_2 = scrapy.Field()
    font_num = scrapy.Field()
    book_status = scrapy.Field()
    author_name = scrapy.Field()
    intro = scrapy.Field()


class IpItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()


class BqgBookItem(scrapy.Item):
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    book_img = scrapy.Field()
    # book_type = scrapy.Field()
    # classify_1 = scrapy.Field()
    # classify_2 = scrapy.Field()
    # font_num = scrapy.Field()
    # book_status = scrapy.Field()
    author_name = scrapy.Field()
    intro = scrapy.Field()


class BqgBookStatusItem(scrapy.Item):
    id = scrapy.Field()
    book_type = scrapy.Field()
    book_status = scrapy.Field()
    last_time = scrapy.Field()
    last_chapter = scrapy.Field()
