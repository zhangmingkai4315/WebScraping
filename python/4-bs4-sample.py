#coding= utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError

html=urlopen('http://www.jsmean.com/blog/docs')
bsObj=BeautifulSoup(html.read(),'html.parser')

navList=bsObj.findAll("h5",{"class":"colorFonts"})
for nav in navList:
    print(nav.get_text())    # get_text()会删除所有的tag 只保留文本内容

print(bsObj.findAll({'h1','h2','h3'}))   

# print (bsObj.findAll({'li'},{'class':"bold"}))

print (bsObj.findAll(id='slide-out'))

print(bsObj.findAll(class_='bold'))  # 注意这里的是class_ 不能使用保留字符class




