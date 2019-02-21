import scrapy
from novel_scrapy.items import NovelMenuItem


class bqgMenuSpider(scrapy.Spider):  # 需要继承scrapy.Spider类
    name = 'bqg_menu'  # 定义蜘蛛名
    allowed_domains = ["https://www.qu.la"]
    start_urls = ['https://www.qu.la/']

    def parse(self, response):
        nav = response.css('#wrapper .nav li a')  # 书籍类别
        for v in nav:  # 循环获取每一条名言里面的：名言内容、作者、标签
            item = NovelMenuItem()
            # tags = v.css('.tags .tag::text').extract()  # 提取标签
            # tags = ','.join(tags)  # 数组转换为字符串
            # fileName = '%s-语录.txt' % autor  # 定义文件名,如：木心-语录.txt
            item['book_type'] = v.css('::text').extract()
            yield item