# -*- coding: utf-8 -*-
# 10-2.py (Python 3 version)

import _mysql

db = _mysql.connect(
    host='db4free.net',
    user='ptest',
    passwd='＊＊＊＊',
    db='ptest')
db.query('select * from PRICES;')
res = db.store_result()
rows = list()
while res.has_next:
  row = res.fetch_row()
  rows.append(row)

for i in range(0,10):
  print("日期：{}, 92無鉛：{}, 95無鉛：{}, 98無鉛：{}".\
      format(rows[i][0], rows[i][1], rows[i][2], rows[i][3]))
