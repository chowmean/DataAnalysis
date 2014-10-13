import urllib2
import re
import cookielib
from cookielib import CookieJar
import time

cj=CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheader= [('User-agent','Mozilla/5.0')]

def main():
    try:
        page='http://www.9news.ph/?widgetName=rssfeed&widgetContentId=2085&getXmlFeed=true'
        sourceCode=opener.open(page).read()
        print (sourceCode)
	file = open("store/newsNews9"+time.strftime('_%d_%m_%Y')+".xml", "w")
	file.write(sourceCode)
	file.close()
    except Exception , e:
	print e

main()
