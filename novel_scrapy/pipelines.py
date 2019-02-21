# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
import pymysql
import pymysql.cursors
import codecs
from twisted.enterprise import adbapi


class NovelScrapyPipeline(object):

    def __init__(self, dbpool):
        print('=======2')
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        print('=======1')
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        print('=======3')
        d = self.dbpool.runInteraction(self._conditional_insert, item, spider)  # 调用插入的方法
        log.msg("-------------------连接好了-------------------")
        d.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def _conditional_insert(self, conn, item, spider):
        print('=======4')
        log.msg("-------------------打印-------------------")
        conn.execute("insert into `book` (`name`) values(%s)", (item['name']))
        log.msg("-------------------一轮循环完毕-------------------")

    def _handle_error(self, failue, item, spider):
        print('=======5')
        print(failue)
