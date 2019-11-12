import scrapy
from novel_scrapy.items import BqgBookItem
import pprint


class bqgSpider(scrapy.Spider):  # 需要继承scrapy.Spider类
    name = 'bqg'  # 定义蜘蛛名
    allowed_domains = ["m.qu.la"]
    # start_urls = ['https://m.qu.la']
    start_urls = ['https://m.qu.la']

    def parse(self, response):
        # classify = response.css('nav.smallNav a')  # 获取分类
        # ify = classify[0].css('::attr(href)').extract()[0]  # 分类
        # whole = classify[3].css('::attr(href)').extract()[0]  # 全本
        #
        # if len(classify) > 0 and ify != "":
        # yield scrapy.Request(self.start_urls[0] + ify, callback=self.loop)
        yield scrapy.Request(self.start_urls[0] + '/wapsort/0_23154.html', callback=self.loop)

    def loop(self, response):
        arr = response.css('.recommend div#main .hot_sale')  # 拿到当页所有书籍
        for item in arr:
            data = BqgBookItem()
            book_name = item.css('a p.title::text').get().strip().replace('\n', '')
            book_url = item.css('a::attr(href)').extract()[0]  # 书籍url
            book_img = item.css('a img::attr(data-original)').extract()[0]  # 书籍图片
            author = item.css('a p.author::text').get().strip().replace('\n', '').split("：")[1]
            intro = item.css('p.review::text')[1].get().strip().split("简介：")[1]
            data['book_name'] = book_name
            data['book_url'] = book_url
            data['book_img'] = book_img
            data['author_name'] = author
            data['intro'] = intro
            yield data

        try:
            page = response.css('.recommend p.page #nextPage')
            if len(page) > 0:
                url = page.css('::attr(href)').extract()[0]  # 跳转url
                yield scrapy.Request(self.start_urls[0] + url, callback=self.loop)
        except Exception as e:
            print(e)
