#coding= utf-8
#   使用urllib库可以直接获得html文档
#   使用request可以携带更多的数据
#   urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
from urllib2 import urlopen
html=urlopen('http://jsmean.com')
print(html.read())