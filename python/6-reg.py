#coding= utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError
import re


html=urlopen('http://pythonscraping.com/pages/page3.html')
bsObj=BeautifulSoup(html.read(),'html.parser')

productions=bsObj.find('table',{'id':'giftList'}).tr.next_siblings
for production in productions:
    print production

imageRex=re.compile(r"^[\S]+\.jpg$")
images=bsObj.findAll("img",{"src":imageRex})
for image in images:
    print image['src']

