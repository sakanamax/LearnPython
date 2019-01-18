# -*- coding: utf-8 -*-
# 程式 12-4 (Python 3 Version)
import facebook, shutil, os, requests
token = 'EAACEdEose0cBAO3B2zRrFCw14fxEp4ZBnotAYcpKnEZAZC6fY7dxna6eRWQtr4xkRPHYyNjsra5NZAKPnjBfsoXy8Ri1lVndQpSTUZAw43kBO24QMylZB9tM6kFTpPbQvLr2EZCzyvWiFkHmXKLIjnSS0VWhY0GtwRchTYZB4A9flqqicuKyewXmiuW3zGXhv4BmZB74rP9x5cwZDZD'
g = facebook.GraphAPI(access_token=token, version="2.2")
albums = g.get_connections(id='me', connection_name='albums')
albums = albums['data']
for a in albums:
    photos = g.get_connections(id=a['id'], connection_name='photos')
    for photo in photos['data']:
        images = g.get_object(id=photo['id'], fields='images')
        image = images['images'][0]['source']
        #filename = image.split('/')[-1].split('?')[0]
        filename = os.path.basename(image).split('?')[0]
        print(filename)
        fp = open('fb-images/'+filename, 'wb')
        pic = requests.get(image, stream=True)
        shutil.copyfileobj(pic.raw, fp)
        fp.close()
