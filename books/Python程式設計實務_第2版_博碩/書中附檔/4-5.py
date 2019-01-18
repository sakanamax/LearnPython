# -*- coding: utf-8 -*-
from gtts import gTTS

tts = gTTS("我也可以講中文喔", lang='zh-tw')
tts.save("chinese.mp3")
