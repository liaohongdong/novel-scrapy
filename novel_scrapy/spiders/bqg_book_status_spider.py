import scrapy
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import BqgBookStatusItem
from novel_scrapy.common.LogHandler import Loghandler

log = Loghandler("bqgBookStatusSpider")


class bqgBookStatusSpider(scrapy.Spider):
    name = 'bqg_book_status'
    allowed_domains = ["m.qu.la"]
    start_urls = ['https://m.qu.la']
    db = DBHelp()
    cursor = db.sdb.cursor()
    start_id = 231619

    def parse(self, response):
        select_sql = "SELECT * FROM `novel_scrapy`.`scrapy_book` WHERE `id` = '" + str(self.start_id) + "'"
        try:
            self.cursor.execute(select_sql)
            results = self.cursor.fetchone()
            if results is None:
                return
            if len(results) is not None:
                data = BqgBookStatusItem()
                content = response.css('#synopsisArea_detail .synopsisArea_detail')
                pArr = content.css("p")
                if len(pArr) > 0:
                    book_type = pArr[1].css("::text").get().replace("\n", "").split("：")[1]
                    book_status = pArr[2].css("::text").get().replace("\n", "").split("：")[1]
                    last_time = pArr[3].css("::text").get().replace("\n", "").split("：")[1]
                    # last_chapter = pArr[4].css("a::text").get().strip()
                    last_chapter = pArr[4].css("a::text").get()
                    book_status = (0, 1)[book_status == "连载"]
                    # print(book_type, last_time, last_chapter, book_status)

                    data["id"] = int(results[0] - 1)  # sql第一次查出来的id是1 跳过第一页 第二次查出来是2 此时获取的是第一页的数据 所以存数据库id要-1
                    data["book_type"] = str(book_type)
                    data["book_status"] = str(book_status)
                    data["last_time"] = str(last_time)
                    data["last_chapter"] = str(last_chapter)
                    yield data

                self.start_id = int(self.start_id) + 1
                yield scrapy.Request(self.start_urls[0] + results[2], callback=self.parse, dont_filter=True)
        except Exception as e:
            log.info(e)
