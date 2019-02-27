import sys
import os
import time
from scrapy.cmdline import execute

os.system("scrapy crawl ip")
time.sleep(5)
os.system("scrapy crawl qd")
