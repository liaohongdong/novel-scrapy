# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
import codecs
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import NovelMenuItem


class NovelScrapyPipeline(object):

    def __init__(self):
        self.db = DBHelp()

    # @classmethod
    # def from_settings(cls, settings):
    #     dbargs = dict(
    #         host=settings['MYSQL_HOST'],
    #         db=settings['MYSQL_DBNAME'],
    #         user=settings['MYSQL_USER'],
    #         passwd=settings['MYSQL_PASSWD'],
    #         port=settings['MYSQL_PORT'],
    #         charset='utf8',
    #         cursorclass=pymysql.cursors.DictCursor,
    #         use_unicode=True,
    #     )
    #     dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
    #     return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item, NovelMenuItem):
            d = self.db.dbpool.runInteraction(self.db.bqg_menu, item, spider)  # 调用插入的方法
        else:
            log.msg("-------------------出错了  item不匹配-------------------")
        d.addErrback(self.db.handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    # def bqg_menu(self, conn, item, spider):
    # log.msg("````bqg_menu start```")
    # conn.execute('insert ignore into `scrapy_menu` (`book_type`) values (%s)', (item['book_type']))
    # log.msg("````bqg_menu end```")

    # def _handle_error(self, failue, item, spider):
    # print('-------------------报错了-------------------')
    # print(failue)
