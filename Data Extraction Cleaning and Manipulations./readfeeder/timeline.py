import glob
import json 
from collections import Counter
from textblob import TextBlob
import re
a = open("cleared.json", 'r')
file=a.read()
a.close()
listof=file.split("\n")
array = glob.glob("store/*.xml")




for words in listof:
	print words
	print "getting timeline for " + words
	text=[]
	i=0
	j=0
	data=""
	dictionary={i:{'description':"Des",'date':"Date",'source':"URL"}}
	dicttowrite=dict()
	dicttowrite.update(dictionary)
	i=1
	for arrays in array: 
		afile= open(arrays, 'r')
		filetoread=afile.read()
		try:
			dates=re.findall(r'<pubDate>(.*?)</pubDate>',filetoread)	
			if(dates!=""):			
				date=dates[0]			
			link=re.findall(r'<link>(.*?)</link>',filetoread)	
			if(link!=""):			
				url=link[0]			
			if (dates==""):
				date=re.findall(r'<pubDate>(.*?)</pubDate>',filetoread)	
				
			titles=re.findall(r'<title>(.*?)</title>',filetoread)
			for title in titles:
				if(words!=''):
					if(words.lower() in title.lower()):
						print words+"=>"+title	
						dictionary=dict({'description':title,'date':date,'source':url})
						text.append(dictionary)						
						#dicttowrite.update((dictionary))									
						
					j=j+1
			
		except Exception, e:
			print str(e)
		i=i+1
	filetowrite = open("datastore/timeline_"+words+".json", "w")
	filetowrite.write(json.dumps(text))
	filetowrite.close()
	
		


