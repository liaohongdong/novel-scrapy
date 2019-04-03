# coding=utf-8
import requests
import json

# 请求地址
targetUrl = "http://baidu.com"
#
# proxyAll = requests.get(
#     'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=47232&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=')
# jsons = json.dumps(proxyAll.text)
# proxyJson = json.loads(s=jsons)
# proxyJson = json.loads(s=proxyJson)
# ip = proxyJson["data"][0]["ip"]
# port = proxyJson["data"][0]["port"]
#
# print(str(ip)+':'+str(port))

# requests.get(targetUrl, )
# proxy = '114.55.236.62:3128'
# proxy = '202.100.83.139:80'
# proxy = '114.55.236.62:3128'
# proxy = '202.100.83.139:80'
# proxy = '116.196.90.181:3128'
# proxy = '159.226.140.15:3128'
# proxy = '218.60.8.98:3129'
# proxy = '121.196.197.17:3128'
# html = requests.get(targetUrl, proxies={"http": "http://{}".format(proxy)})
# print(html)
# print(html.status_code)

d = False
c = 4 if d else 3
print(c)
