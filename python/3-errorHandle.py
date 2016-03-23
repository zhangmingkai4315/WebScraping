from bs4 import BeautifulSoup
from urllib2 import urlopen,HTTPError

def getHttpHeader(url):
    try:
        html=urlopen(url)
    except HttpError, e:
        return None
    try:
        bsObj=BeautifulSoup(html.read(),'html.parser')
        header=bsObj.header
    except AttributeError, e:
        return None
    else:
        return header

header=getHttpHeader('http://jsmean.com')
if header==None:
    print('Header can\'t found')
else:
    print(header)



html=urlopen('http://www.jsmean.com')
bsObj=BeautifulSoup(html.read(),'html.parser')
print(bsObj.header)