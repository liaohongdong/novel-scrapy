import sys
import os
import time
from scrapy.cmdline import execute
from scrapy import cmdline

# os.system("scrapy crawl ip")
# time.sleep(5)
# os.system("scrapy crawl qd")

name = 'qd'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
