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
        page='http://ibnlive.in.com/ibnrss/top.xml'
        sourceCode=opener.open(page).read()
        print (sourceCode)
	file = open("store/newsCNN_TOP"+time.strftime('_%d_%m_%Y')+".xml", "w")
	file.write(sourceCode)
	file.close()
    except Exception , e:
	print e

main()
