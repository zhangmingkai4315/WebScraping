from bs4 import BeautifulSoup
from urllib2 import urlopen

html=urlopen('http://www.jsmean.com')
bsObj=BeautifulSoup(html.read(),'html.parser')
print(bsObj.header)