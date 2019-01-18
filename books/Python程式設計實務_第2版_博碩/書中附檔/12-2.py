# -*- coding: utf-8 -*-
# 程式 12-2 (Python 3 Version)

import requests, json
import facebook

token = "EAACEdEose0cBAGWFrZBfyDkg2YLq35v5Voxk7ZBQlNDCJSoIaBcZBKJTmuHVAiWF2cJCqXUmsXbmBx9XvYCOEtZBljLM5rynisyjQ3YxcamhKLdK7OkeeqFZCQywIhNSXijZABwNnusV7vZAVz93ZAmpK9mzz2vrEn2ZBdQKm0d10MTdXKKLH3U5ZCyTW0Uc5PDeq1WPsdZCsZAZCAwZDZD"
g = facebook.GraphAPI(access_token = token)

conn = g.get_connections(
    id='me', connection_name='posts', 
    fields='created_time,message,likes')

posts = conn['data']

print("--------")
for post in posts:
    if 'message' in post:
        print("張貼日期：",post['created_time'])
        print("貼文內容：",post['message'])
        print("按讚人數：{}".format(len(post['likes']['data'])))
        print("-------------------------")
