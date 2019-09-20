import requests
import json
import pprint
import time


class GetProxy(object):
    @classmethod
    def get_proxy(cls):
        # yield requests.get("http://39.108.115.177:5000/get/").content
        return requests.get("http://39.108.115.177:5000/get/").content
        # return requests.get(
        #     'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=47232&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')

    @classmethod
    def delete_proxy(cls, proxy):
        requests.get("http://39.108.115.177:5000/delete/?proxy={}".format(proxy))

    @classmethod
    def get_ip(cls):
        html = ''
        proxy = ''
        retry_count = 2
        proxy = cls.get_proxy()
        # for id in proxy:
        #     print(id, 2)
        if proxy == b'no proxy!':
            time.sleep(60)
            cls.get_ip()
        else:
            while retry_count > 0:
                try:
                    html = requests.get('http://httpbin.org/ip',
                                        proxies={"http": "{}".format(bytes.decode(proxy))},
                                        timeout=5
                                        )
                    if html and html.status_code == 200:
                        print('html ===>', html, bytes.decode(proxy))
                        return bytes.decode(proxy)
                except Exception as e:
                    print('get_proxy: ===> ', e)
                    retry_count -= 1
                    if retry_count == 0:
                        cls.delete_proxy(bytes.decode(proxy))
                        time.sleep(1.5)
                        cls.get_ip()
            # if html and html.status_code == 200:
            #     return bytes.decode(proxy)


if __name__ == '__main__':
    ddd = GetProxy().get_ip()
    print(ddd)
