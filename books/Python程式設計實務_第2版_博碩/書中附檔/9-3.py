# -*- coding: utf-8 -*-
# 程式 9-3 (Python 3 version)

import requests

url = 'http://www.get.com.tw/billboard/detail.aspx?sF=1school/02master/107graduate/second/1070192.txt'
name = input("請輸入要查詢的姓名:")
html = requests.get(url).text
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))
