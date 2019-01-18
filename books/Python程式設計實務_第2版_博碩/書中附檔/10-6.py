# -*- coding: utf-8 -*-
# 程式 10-6 (Python 3 version)
from selenium import webdriver
urls = [
'http://hophd.com',
'http://drho.club',
'http://skynetbooks.com',
'https://tw.news.yahoo.com/',
'http://www.cwb.gov.tw/V7/forecast/town368/']

web = webdriver.Chrome(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
web.set_window_position(0,0)
web.set_window_size(800,600)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage{}.png".format(i))
    i += 1
web.close()
