# -*- coding: utf-8 -*-
# 程式 9-2  (Python 3 version)

from pprint import pprint
import requests

url = 'https://news.pts.org.tw/list/0'

html = requests.get(url).text.splitlines()
for i in range(10):
    print(html[i])
