#! /usr/bin/python
import cookielib, urllib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# default User-Agent ('Python-urllib/2.6') will *not* work
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'),
    ]


stylesheets = [
    'https://www.idcourts.us/repository/css/id_style.css',
    'https://www.idcourts.us/repository/css/id_print.css',
]

home = opener.open('https://www.idcourts.us/repository/start.do')
print cj
sessid = cj._cookies['www.idcourts.us']['/repository']['JSESSIONID'].value
# Note the +=
opener.addheaders += [
    ('Referer', 'https://www.idcourts.us/repository/start.do'),
    ]
for st in stylesheets:
    # da trick
    opener.open(st+';jsessionid='+sessid)
search = opener.open('https://www.idcourts.us/repository/partySearch.do')
print cj
