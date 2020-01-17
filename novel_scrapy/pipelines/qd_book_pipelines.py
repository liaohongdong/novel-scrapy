from scrapy import log
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import NovelBookItem


class QdBookPipeline(object):

    def __init__(self):
        self.db = DBHelp()

    def process_item(self, item, spider):
        if isinstance(item, NovelBookItem):
            d = self.db.dbpool.runInteraction(self.qd_book_name, item, spider)  # 调用插入的方法
        else:
            log.msg("-------------------出错了  item不匹配-------------------")
        d.addErrback(self.db.handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def qd_book_name(self, conn, item, spider):
        log.msg("````qd_book_name start```")
        conn.execute('insert ignore into `scrapy_book` '
                     '(`book_name`, `book_type`, `classify_one`, `classify_two`, `font_num`, `book_status`, `author_name`, `intro`)'
                     ' values (%s, %s, %s, %s, %s, %s, %s, %s)',
                     (item['book_name'],
                      item['book_type'],
                      item['classify_one'],
                      item['classify_two'],
                      item['font_num'],
                      item['book_status'],
                      item['author_name'],
                      item['intro']))
        log.msg("````qd_book_name end```")

    def _handle_error(self, failue, item, spider):
        print('-------------------报错了-------------------')
        print(failue)
