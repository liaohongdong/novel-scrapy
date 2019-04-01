import requests
import pprint


def get_proxy():
    return requests.get("http://39.108.115.177:5010/get/").content


def delete_proxy(proxy):
    requests.get("http://39.108.115.177:5010/delete/?proxy={}".format(bytes.decode(proxy)))


def getHtml():
    # ....
    retry_count = 3
    proxy = get_proxy()
    print(proxy)
    while retry_count > 0:
        try:
            html = requests.get('http://www.baidu.com', proxies={"http": "http://{}".format(bytes.decode(proxy))})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错3次, 删除代理池中代理
    delete_proxy(bytes.decode(proxy))
    return None


a = getHtml()
pp = pprint.PrettyPrinter(indent=4)
ddd = pp.pformat(a.__dict__)
print(ddd)
