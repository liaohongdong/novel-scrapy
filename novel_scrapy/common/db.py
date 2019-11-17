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
        sdb = pymysql.connect(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            database=settings['MYSQL_DBNAME'],
            port=settings['MYSQL_PORT']
        )
        self.dbpool = dbpool
        self.sdb = sdb
        self.escape = pymysql.escape_string

    def connect(self):
        return self.dbpool
