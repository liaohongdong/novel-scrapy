# 起点 反爬字体转数字
from io import BytesIO
import urllib3
from urllib3 import PoolManager
from fontTools.ttLib import TTFont

number = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
          'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'period': '.'}
manager = PoolManager(10)
urllib3.disable_warnings()
ttf = manager.request('GET', "https://qidian.gtimg.com/qd_anti_spider/uJdXplZn.ttf")
# print(ttf._body)
font = TTFont(BytesIO(ttf._body))
camp = font.getBestCmap()
font.close()

num = ""
encry_text = "&#100482;&#100490;&#100479;&#100487;&#100485;"
for flag in encry_text.split(";"):
    if flag != '':
        ch = int(flag[2:])
        num += number[camp[ch]]

print(num)
