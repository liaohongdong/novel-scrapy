# -*- coding: utf-8 -*-

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from novel_scrapy.middlewares.resource import USER_AGENT_LIST

import random

from scrapy import signals

from novel_scrapy.common.LogHandler import Loghandler

log = Loghandler('CustomUserAgent', file=False)


class CustomUserAgent(UserAgentMiddleware):
    def __init__(self):
        print('CustomUserAgent')

    def process_request(self, request, spider):
        spider.logger.info('1110 CustomUserAgent Spider process_request: {0}, {1}'.format(request))
        ua = random.choice(USER_AGENT_LIST)
        request.headers.setdefault('User-Agent', ua)

    def process_response(self, request, response, spider):
        spider.logger.info('1110 CustomUserAgent Spider process_exception: {0}, {1}'.format(request, response))
        return response

    def process_exception(self, request, exception, spider):
        spider.logger.info('1114 CustomUserAgent Spider process_exception: {0}, {1}'.format(request, exception))
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    @classmethod
    def from_crawler(cls, crawler):
        log.info('CustomUserAgent Spider from_crawler: {}'.format(crawler))
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        spider.logger.info('CustomUserAgent Spider process_spider_input: {}'.format(response))
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        spider.logger.info('CustomUserAgent Spider process_spider_output: {}'.format(result))
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        spider.logger.info('CustomUserAgent Spider process_spider_exception: {}'.format(response))
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        spider.logger.info('CustomUserAgent Spider process_start_requests: {}'.format(start_requests))
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('CustomUserAgent Spider opened: %s' % spider.name)
