# -*- coding: utf-8 -*-

from novel_scrapy.middlewares.resource import PROXIES
from novel_scrapy.common.db import DBHelp
import random
import requests
from novel_scrapy.common.get_proxy import get_proxy


class RandomProxy(object):
    @classmethod
    def process_request(cls, request, spider):
        # db = DBHelp()
        # proxy = random.choice(PROXIES)
        # cursor = db.sdb.cursor()
        # cursor.execute(
        #     'select * from scrapy_proxys where score = 10 ORDER BY RAND() LIMIT 1')
        # data = cursor.fetchone()
        # cursor.close()
        # proxy = str(data[1]) + ":" + str(data[2])
        # print(proxy)
        proxy = get_proxy().get_ip()
        request.meta['proxy'] = 'http://%s' % proxy
        print("request.meta['proxy']:----------", request.meta['proxy'])
