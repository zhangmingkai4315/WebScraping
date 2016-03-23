#coding= utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError


html=urlopen('http://pythonscraping.com/pages/page3.html')
bsObj=BeautifulSoup(html.read(),'html.parser')

productions=bsObj.find('table',{'id':'giftList'}).tr.next_siblings
for production in productions:
    print production

print(bsObj.find('img',{'src':'../img/gifts/img6.jpg'}).parent.previous_sibling.get_text())