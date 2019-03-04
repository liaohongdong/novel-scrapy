import scrapy
import io
import sys
import os
import re
from fontTools.ttLib import TTFont
from novel_scrapy.common.font_num import FontToNum
from io import BytesIO
from pprint import pprint


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
        for item in range(len(wrap)):
            i = wrap[item]
            style_font = i.css('.update span style::text').extract()  # 反爬字体图标
            ttf_file = re.match(r'.*url\(\'(.*?)\'\).*?url\(\'(.*?)\'\).*?url\(\'(.*?)\'\).*', style_font[0])
            self.camp = self.ftn.get_gesources(ttf_file.group(3))
            # dd = i.css('.update span span::text').extract()  # 解析出来是框框 所以需要使用正则去匹配
            # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
            font_num = self.ftn.execute(reg.group(item+1), self.camp)
            print(font_num)
