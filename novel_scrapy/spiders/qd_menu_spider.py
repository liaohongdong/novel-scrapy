import scrapy


class qdSpider(scrapy.Spider):
    name = 'qd'
    allowed_domains = ["www.qidian.com"]
    start_urls = ['https://www.qidian.com/']

    def parse(self, response):
        goto_finish = 'https:' + response.css('.main-nav-wrap ul li:nth-child(4) a::attr(href)').get()
        if goto_finish is not None:
            return scrapy.Request(goto_finish, callback=self.get_finish_info)

    def get_finish_info(self, response):
        print(response.css('title::text').get())
        print("--------------------")
