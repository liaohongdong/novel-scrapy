# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  # 导入seetings配置


class DBHelp():
    def __init__(self):
        settings = get_project_settings()  # 获取settings配置，设置需要的信息
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
        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    def handle_error(self, failue, item, spider):
        print('-------------------报错了-------------------')
        print(failue)

    # TODO 这个可以分离出去
    def bqg_menu(self, conn, item, spider):
        log.msg("````bqg_menu start```")
        conn.execute('insert ignore into `scrapy_menu` (`book_type`) values (%s)', (item['book_type']))
        log.msg("````bqg_menu end```")
