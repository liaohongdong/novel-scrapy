import requests
import json
import pprint
import time


class get_proxy():
    @classmethod
    def get_proxy(cls):
        return requests.get("http://39.108.115.177:5010/get/").content
        # return requests.get(
        #     'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=47232&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')

    @classmethod
    def delete_proxy(cls, proxy):
        requests.get("http://39.108.115.177:5010/delete/?proxy={}".format(proxy))

    @classmethod
    def get_ip(cls):
        html = ''
        proxy = ''
        while True:
            retry_count = 5
            proxy = cls.get_proxy()
            print(proxy)
            if proxy == b'no proxy!':
                time.sleep(5)
                continue

            while retry_count > 0:
                try:
                    # jsons = json.dumps(proxy.text)
                    # proxy_json = json.loads(s=jsons)
                    # proxy_json = json.loads(s=proxy_json)
                    # ip = proxy_json["data"][0]["ip"]
                    # port = proxy_json["data"][0]["port"]
                    # proxy = str(ip) + ":" + str(port)
                    # 使用代理访问
                    print(proxy)
                    html = requests.get('http://www.baidu.com',
                                        proxies={"http": "http://{}".format(bytes.decode(proxy))})
                    # html = requests.get('http://www.baidu.com', timeout=1,
                    #                     proxies={"http": "http://{}".format(proxy)})
                    if html != '' and html.status_code == 200:
                        break
                except Exception:
                    retry_count -= 1
                    if retry_count == 0:
                        cls.delete_proxy(bytes.decode(proxy))
                        time.sleep(3)

            if html != '' and html.status_code == 200:
                break

        return bytes.decode(proxy)
        # return proxy


a = get_proxy().get_ip()
# pp = pprint.PrettyPrinter(indent=4)
# ddd = pp.pformat(a.__dict__)
# print(ddd)
print(a)

# d = requests.get("http://liaohongdong.cn:5010/get")
# print(d.content)

# time.sleep(3)
# print('112233')
