from novel_scrapy.common.LogHandler import Loghandler
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import BqgBookChapterWhole
import pymysql

log = Loghandler("BqgBookStatusPipelines")


class BqgBookChapterWholePipelines(object):

    def __init__(self):
        self.db = DBHelp()

    def process_item(self, item, spider):
        if isinstance(item, BqgBookChapterWhole):
            d = self.db.dbpool.runInteraction(self.bqg_chapter_whole, item, spider)  # 调用插入的方法
        else:
            log.info("-------------------BqgBookChapterWholePipelines出错了  item不匹配-------------------")
        d.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def bqg_chapter_whole(self, conn, item, spider):
        log.info("````bqg_chapter_whole start```")
        sql = "INSERT IGNORE INTO  `scrapy_chapter_whole` " \
              "(`cid`, `chapter_name`, `chapter_url`) values " \
              "( '{cid}', '{chapter_name}', '{chapter_url}' )".format(
            cid=item["cid"],
            chapter_name=self.db.escape(str(item["chapter_name"])),
            chapter_url=self.db.escape(str(item["chapter_url"]))
        )
        log.info(sql)
        conn.execute(sql)
        log.info("````BqgBookChapterWholePipelines end```")

    def _handle_error(self, failue, item, spider):
        print('-------------------BqgBookChapterWholePipelines报错了-------------------')
        print(failue)
