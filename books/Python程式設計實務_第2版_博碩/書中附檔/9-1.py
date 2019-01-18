# -*- coding: utf-8 -*-
# 程式 9-1  (Python 3 version)
from urllib.parse import urlparse

url = "https://fund.cnyes.com/search/?categoryAbbr=C74&classCurrency=TWD,USD&investmentArea=A13&page=2"

uc = urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
	print(cmd)
