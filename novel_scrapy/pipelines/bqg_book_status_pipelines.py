from novel_scrapy.common.LogHandler import Loghandler
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import BqgBookStatusItem
import pymysql

log = Loghandler("BqgBookStatusPipelines")

class BqgBookStatusPipelines(object):

    def __init__(self):
        self.db = DBHelp()

    def process_item(self, item, spider):
        if isinstance(item, BqgBookStatusItem):
            d = self.db.dbpool.runInteraction(self.bqg_book, item, spider)  # 调用插入的方法
        else:
            log.info("-------------------BqgBookStatusPipelines出错了  item不匹配-------------------")
        d.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def bqg_book(self, conn, item, spider):
        log.info("````BqgBookStatusPipelines start```")
        update_sql = "UPDATE `novel_scrapy`.`scrapy_book` SET" \
                     " `book_type` = '{book_type}'," \
                     " `book_status` = '{book_status}'," \
                     " `last_chapter` = '{last_chapter}'," \
                     " `last_time` = '{last_time}'" \
                     " WHERE `id` = {id}".format(
            id=int(item['id']),
            book_type=str(item["book_type"]),
            book_status=str(item["book_status"]),
            last_time=str(item["last_time"]),
            last_chapter=pymysql.escape_string(item["last_chapter"]),
        )

        log.info(update_sql)
        conn.execute(update_sql)
        log.info("````BqgBookStatusPipelines end```")

    def _handle_error(self, failue, item, spider):
        print('-------------------BqgBookStatusPipelines报错了-------------------')
        print(failue)
