import scrapy
from novel_scrapy.common.db import DBHelp
from novel_scrapy.items import BqgBookChapterWhole
from novel_scrapy.common.LogHandler import Loghandler

log = Loghandler("bqgBookChapterWholeSpider")


class bqgBookChapterWholeSpider(scrapy.Spider):
    name = 'bqg_book_chapter_whole'
    allowed_domains = ["m.qu.la"]
    start_urls = ['https://m.qu.la/booklist/']
    db = DBHelp()
    cursor = db.sdb.cursor()
    start_id = 0
    initUrlId = ""  # 书籍路径
    results = ""

    def __init__(self):
        res = self.executeSql("SELECT * FROM `novel_scrapy`.`scrapy_book_whole` LIMIT " + str(self.start_id) + ",1")
        if res[3]:
            self.initUrlId = self.getOriginUrl(res[3])
            self.start_urls[0] = self.start_urls[0] + self.initUrlId + ".html"
            self.start_id = int(self.start_id) + 1

    def executeSql(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def getOriginUrl(self, urls):  # 返回书本的id
        return urls.split("/")[2]

    # def update(self, book_url, cid):
    #     update_sql = "UPDATE scrapy_book_whole SET cid=" + cid + " WHERE book_url = " + book_url
    #     pass

    def parse(self, response):
        content = response.css("div#chapterlist.directoryArea")
        pArr = content.css("p")
        first = pArr.css("a::attr(href)").extract()[0]
        if first == "#bottom":
            pArr = pArr[1:len(pArr)]

        for item in pArr:
            data = BqgBookChapterWhole()
            chapter_url = item.css("a::attr(href)").extract()[0]
            chapter_name = item.css("a::text").get()
            data["cid"] = self.initUrlId
            data["chapter_url"] = chapter_url
            data["chapter_name"] = chapter_name
            yield data

        try:
            next_res = self.executeSql(
                "SELECT * FROM `novel_scrapy`.`scrapy_book_whole` LIMIT " + str(self.start_id) + ",1")
            if next_res[3]:
                self.initUrlId = self.getOriginUrl(next_res[3])
                self.start_urls[0] = self.start_urls[0] + self.initUrlId + ".html"
                self.start_id = int(self.start_id) + 1
                yield scrapy.Request(self.start_urls[0], callback=self.parse, dont_filter=True)
        except Exception as e:
            log.info(e)
