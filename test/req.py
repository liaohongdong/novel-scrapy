import requests

# from test import testRun
import pymysql

if __name__ == '__main__':
    # asd = '123.117.254.56:8060'
    # d = requests.get('http://www.baidu.com/', proxies={"http": "http://111.13.134.22:80"}, timeout=10)
    # d = requests.get('https://www.qidian.com/', proxies={"http": asd}, timeout=5)
    # d = requests.get('http://httpbin.org/ip', proxies={"http": asd}, timeout=5)
    # d = requests.get(
    #     'https://www.qidian.com/finish?action=hidden&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=2&page=3',
    #     proxies={"http": asd}, timeout=5)
    # print(d)

    # t = testRun()
    # requests.get('http://www.baidu.com/', proxies={"http": "http://112.91.224.33:9069"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://123.117.32.145:8359"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://40.73.36.247:8411"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://123.139.56.238:8510"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://39.137.69.10:8968"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://218.60.8.99:8825"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://124.250.26.129:9011"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://39.137.77.66:8086"})
    # requests.get('http://www.baidu.com/', proxies={"http": "http://39.137.69.7:9036"})

    a = "aaa\n '     /n "
    d = pymysql.escape_string(a + ' " hha')
    print(d)
