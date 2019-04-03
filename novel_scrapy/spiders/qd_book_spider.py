import scrapy
import re
from novel_scrapy.common.font_num import FontToNum
from novel_scrapy.items import NovelBookItem


class QdSpider(scrapy.Spider):
    name = 'qd'
    allowed_domains = ["www.qidian.com"]
    start_urls = ['https://www.qidian.com/']

    def __init__(self):
        self.ftn = FontToNum()
        self.camp = ''
        self.lines = ''
        line = 'class="update.*?span.*?span class=".*?>(.*?)</span>.*?'
        for s in range(1, 21):
            self.lines += line
        self.lines = r'.*?' + self.lines

    def parse(self, response):
        goto_finish = 'https:' + response.css('.main-nav-wrap ul li:nth-child(4) a::attr(href)').get()
        if goto_finish is not None:
            return scrapy.Request(goto_finish, callback=self.get_finish_info)

    def get_finish_info(self, response):
        wrap = response.css('.all-book-list ul li')
        re_txt = response.text
        reg = re.match(self.lines, re_txt, re.M | re.S)
        next = response.css('.lbf-pagination-item-list li:last-child a::attr(href)').extract()[0]
        for item in range(len(wrap)):
            nb_item = NovelBookItem()
            i = wrap[item]
            style_font = i.css('.update span style::text').extract()  # 反爬字体图标
            ttf_file = re.match(r'.*url\(\'(.*?)\'\).*?url\(\'(.*?)\'\).*?url\(\'(.*?)\'\).*', style_font[0])
            self.camp = self.ftn.get_gesources(ttf_file.group(3))
            # dd = i.css('.update span span::text').extract()  # 解析出来是框框 所以需要使用正则去匹配
            # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
            nb_item['font_num'] = float(self.ftn.execute(reg.group(item + 1), self.camp))
            nb_item['book_name'] = i.css('.book-mid-info h4 a::text').extract()[0]
            nb_item['author_name'] = i.css('.book-mid-info .author .name::text').extract()[0]
            nb_item['book_type'] = i.xpath('./div[2]/p[1]/a[2]/text()').get()
            nb_item['classify_1'] = i.xpath('./div[2]/p[1]/a[2]/text()').get()
            nb_item['classify_2'] = i.xpath('./div[2]/p[1]/a[3]/text()').get()
            nb_item['book_status'] = i.xpath('./div[2]/p[1]/span/text()').get()
            nb_item['intro'] = i.xpath('./div[2]/p[2]/text()').get()
            yield nb_item

        if next is not None:
            yield scrapy.Request('http://' + next, callback=self.get_finish_info)
