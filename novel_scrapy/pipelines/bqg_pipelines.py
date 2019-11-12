from scrapy import log
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import BqgBookItem


class BqgPipelines(object):

    def __init__(self):
        self.db = DBHelp()

    def process_item(self, item, spider):
        if isinstance(item, BqgBookItem):
            d = self.db.dbpool.runInteraction(self.bqg_book, item, spider)  # 调用插入的方法
        else:
            log.msg("-------------------出错了  item不匹配-------------------")
        d.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def bqg_book(self, conn, item, spider):
        log.msg("````qd_book_name start```")
        conn.execute('insert ignore into `scrapy_book` '
                     '(`book_name`, `book_url`, `book_img`, `author_name`, `intro`)'
                     ' values (%s, %s, %s, %s, %s)',
                     (item['book_name'],
                      item['book_url'],
                      item['book_img'],
                      item['author_name'],
                      item['intro']))
        log.msg("````qd_book_name end```")

    def _handle_error(self, failue, item, spider):
        print('-------------------报错了-------------------')
        print(failue)
