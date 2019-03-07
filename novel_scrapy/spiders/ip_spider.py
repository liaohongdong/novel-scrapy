# http://www.data5u.com/free/gnpt/index.shtml
import scrapy, os
from novel_scrapy.items import IpItem


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = [" www.data5u.com"]
    start_urls = ['http://www.data5u.com/free/gnpt/index.shtml']

    def parse(self, response):
        items = response.xpath('/html/body/div[5]/ul/li[2]/ul[@class=\'l2\']')
        str = ''
        str0 = 'PROXIES = [\n'
        str1 = ''
        str2 = ']\n'
        for index in range(len(items)):
            str0 += '    \'' + items[index].css('span li::text').get() + ':' + items[index].css(
                'span:nth-child(2) li::text').get() + '\',\n'
        str = str0 + str1 + str2
        print(str)
        with open(os.getcwd() + '\\novel_scrapy\\middlewares\\resource.py', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # for ii in range(len(lines)):
            #     print(lines[ii], ii)
            # print(lines[78])
            # print(lines[79])
            # f.close()

        with open(os.getcwd() + '\\novel_scrapy\\middlewares\\resource.py', 'r+', encoding='utf-8') as ff:
            ff.seek(7776)
            ff.truncate()
            # for line in range(len(lines)):
            #     if line == 78:
            #         print(lines[line])
            #         break
            ff.write(str)
            f.close()
            ff.close()
