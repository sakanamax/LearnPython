# -*- coding: utf-8 -*-
# 程式 12-3 (Python 3 Version)

import requests, json
import facebook

token = "EAACEdEose0cBALbvFFvh8Pr57JkugiIxvUi2B510BapZCY4k34m0X1yNL0ZCFnD6PIIChUCEZCpclSku16bmOXOgaCY5eQHUJSP3I1MSTHW9Jc0mFtbJEU3EtuEgnZAaZAaTJ4EV33YGLDdCdpB9mK75BlMCk63fTmgY6OZBXs2ztqmY91FZBMXKGhyutEguLfGhZA7q62RJiwZDZD"
g = facebook.GraphAPI(access_token = token)

attachment =  {
    'name': '新聞直播台網址分享', 
    'link': 'http://drho.tw/news',
    'caption': '新聞直播台',
    'description': '在Youtube上已有許多的新聞台提供直播的功能，而這個網路就找出8個品質較佳的，做一個簡單的介面讓大家方便使用。',
    'picture': 'http://static.ettoday.net/web_2011/images/logo_ettoday.gif'
}

g.put_wall_post(message='這是使用 Python facebook-sdk 測試張貼的範例，我的書要改版囉~~', attachment=attachment)
