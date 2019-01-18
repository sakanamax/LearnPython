# -*- coding: utf-8 -*-
from gtts import gTTS
import playsound

msg = [
"我也可以講中文喔",
"所以，如果有什麼需要我唸的文章", 
"只要把它放在這個程式裡，", 
"我就可以一句一句地把它唸出來"
]

i=0; 
for m in msg:
	print(m)
	tts = gTTS(m, lang='zh-tw')
	tts.save("{}.mp3".format(i))
	playsound.playsound("{}.mp3".format(i))
	i+=1
