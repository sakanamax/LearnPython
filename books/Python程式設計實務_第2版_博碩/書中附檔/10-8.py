# -*- coding: utf-8 -*-
# 程式 10-8 (Python 3 version)

from selenium import webdriver

url = 'https://member.pixnet.cc/login/verify'

web = webdriver.Chrome(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
web.get(url)
web.find_element_by_name('email').clear()
web.find_element_by_name('email').send_keys('yourname')
web.find_element_by_name('password').clear()
web.find_element_by_name('password').send_keys('yourpassword')
web.find_element_by_id('signup__form--post').submit()
