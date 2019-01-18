# -*- coding: utf-8 -*-
# 程式 13-12 (Python 3 Version)
from PIL import Image, ImageDraw, ImageFont

text_msg = u'此為測試用影像'
im = Image.open('sample_s.jpg')
im_w, im_h = im.size

font = ImageFont.truetype('font/wt014.ttf', 80)
dw = ImageDraw.Draw(im)
fn_w, fn_h = dw.textsize(text_msg, font=font)
x = im_w/2-fn_w/2
y = im_h/2-fn_h/2
dw.text((x+5, y+5), text_msg, font=font, fill=(25,25,25))
dw.text((x, y), text_msg, font=font, fill=(128,255,255))
im.save('sample_s_0.jpg')
im.close()
