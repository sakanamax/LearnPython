# -*- coding: utf-8 -*-
# 程式 12-1 (Python 3 Version)

import requests, json

url = "https://graph.facebook.com/v2.12/me?fields=posts.until(1524614400).since(1517443200).limit(10)&access_token=EAACEdEose0cBAGWFrZBfyDkg2YLq35v5Voxk7ZBQlNDCJSoIaBcZBKJTmuHVAiWF2cJCqXUmsXbmBx9XvYCOEtZBljLM5rynisyjQ3YxcamhKLdK7OkeeqFZCQywIhNSXijZABwNnusV7vZAVz93ZAmpK9mzz2vrEn2ZBdQKm0d10MTdXKKLH3U5ZCyTW0Uc5PDeq1WPsdZCsZAZCAwZDZD"
res = requests.get(url)

res = json.loads(res.text)
posts = res['posts']['data']

for post in posts:
    if 'message' in post:
        print (post['created_time'], ':', post['message'])
        print('----------------------------------')
