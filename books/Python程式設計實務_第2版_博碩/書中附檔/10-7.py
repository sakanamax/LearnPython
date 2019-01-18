# -*- coding: utf-8 -*-
# 程式 10-7 (Python 3 version)

import time
from selenium import webdriver
url = 'https://drho.tw/news'

web = webdriver.Chrome(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
web.get(url)
for i in range(1,9):
    web.find_element_by_id('btn{}'.format(i)).click()
    time.sleep(10)
web.close()
