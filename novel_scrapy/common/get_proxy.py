import requests
import pprint


class get_proxy():
    @classmethod
    def get_proxy(cls):
        return requests.get("http://39.108.115.177:5010/get/").content

    @classmethod
    def delete_proxy(cls, proxy):
        requests.get("http://39.108.115.177:5010/delete/?proxy={}".format(proxy))

    @classmethod
    def get_ip(cls):
        html = ''
        proxy = ''
        while True:
            retry_count = 3
            proxy = cls.get_proxy()
            # print(proxy)
            while retry_count > 0:
                try:
                    # 使用代理访问
                    html = requests.get('http://www.baidu.com', timeout=1,
                                        proxies={"http": "http://{}".format(bytes.decode(proxy))})
                    if html != '' and html.status_code == 200:
                        break
                except Exception:
                    retry_count -= 1
                    if retry_count == 0:
                        cls.delete_proxy(bytes.decode(proxy))
            if html != '' and html.status_code == 200:
                break
        return bytes.decode(proxy)


# a = Proxy().get_ip()
# pp = pprint.PrettyPrinter(indent=4)
# ddd = pp.pformat(a.__dict__)
# print(ddd)
# print(a)
