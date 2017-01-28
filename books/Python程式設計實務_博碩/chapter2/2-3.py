# 匯入 requests
import requests
# 透過 requests.get 去抓 民視的網頁
www = requests.get( "http://m.ftv.com.tw/newslist.aspx?class=L" )
# 如果使用 print( www ) 會得到 網頁回覆, 例如 200
# 所以如果要列出網頁內容使用書上的 print( www.text )
print( www )
print( "=========================================" )
print( www.text )
