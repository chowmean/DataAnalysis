#http://feeds.news.com.au/public/rss/2.0/news_theworld_3356.xml


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
        page='http://feeds.news.com.au/public/rss/2.0/news_theworld_3356.xml'
        sourceCode=opener.open(page).read()
        print (sourceCode)
	file = open("store/newsNews"+time.strftime('_%d_%m_%Y')+".xml", "w")
	file.write(sourceCode)
	file.close()
    except Exception , e:
	print e

main()
