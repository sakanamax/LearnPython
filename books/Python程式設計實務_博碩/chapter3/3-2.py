# 書上的作法是 a = range(5), 他其實是要列出 list 0 到 4
# 這個時候 print( a ) 在 python 3, 會出現 range(0, 5)
# 所以 python3 內的寫法, 如果要使用 a = range(5)來列出 list 0 - 4, 應該是 print( list(a) )
# 所以將程式碼改為
# 註解寫了中文在 python 好像就會產生 error, 先無視他吧
a = list( range(5) )
#print( a )
#print( list(a) )

# 同理可證 b
b = list( range(10, 15) )

# 不然 c = a + b 在 python 3 就會出現錯誤
c = a + b
print( "List a", a )
print( "List b", b )
print( "List a + List b", c )
