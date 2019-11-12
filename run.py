import sys
import os
import time
from scrapy.cmdline import execute
from scrapy import cmdline

# os.system("scrapy crawl ip")
# time.sleep(5)
# os.system("scrapy crawl qd")

# name = 'bqg'  # 去bqg 爬取所有的书籍名称
# name = 'bqg_book_status'  # 去bqg 更新数据的具体详情
name = 'bqg_book_chapter_whole'  # 去bqg 根据url 爬取完本 章节
# cmd = 'scrapy crawl {0} -s JOBDIR=crawls/bqg-1'.format(name)
cmd = 'scrapy crawl {0} '.format(name)
cmdline.execute(cmd.split())
