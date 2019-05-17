import requests
import pprint
import json
import telnetlib


def checkProxy(ip, port):
    return telnetlib.Telnet(ip, port=port, timeout=20)


if __name__ == '__main__':
    try:
        a = checkProxy('103.238.225.77', '8888')
        print(a)
    except:
        print('该代理IP  无效')
    else:
        print('该代理IP  有效')
