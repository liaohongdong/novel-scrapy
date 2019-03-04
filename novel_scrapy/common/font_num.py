# 起点 反爬字体转数字
from io import BytesIO
import urllib3
from urllib3 import PoolManager
from fontTools.ttLib import TTFont


class FontToNum:
    # 数字字典
    number = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'period': '.'}

    def get_gesources(self, url):
        manager = PoolManager(10)
        urllib3.disable_warnings()
        ttf = manager.request('GET', url)
        font = TTFont(BytesIO(ttf._body))
        camp = font.getBestCmap()
        font.close()
        manager.clear()
        return camp

    def execute(self, encry_text, camp):
        num = ""
        for flag in encry_text.split(";"):
            if flag != '':
                n = int(flag[2:])
                num += self.number[camp[n]]
        return num
