import re
import time
import glob
from textblob import TextBlob
from collections import Counter
from textblob.np_extractors import ConllExtractor
import json
array = glob.glob("store/*.xml")
i=0
j=0
data=""
for arrays in array: 
	a = open(arrays, 'r')
	file=a.read()

	try:
		titles=re.findall(r'<title>(.*?)</title>',file)
		for title in titles:
			data=data+" "+title
			print "Description ("+str(j)+") = > "+ title+"\n"
			j=j+1
	except Exception, e:
		print str(e)
	i=i+1

delete_to_list = ["href", " gt;&lt;img", "src", "lt;img", "/&gt;&lt;/a&gt;&" ,"lt;br/&gt;&lt;a", "lt;br/&gt;&", "/&gt;&", "]]>","sky","international", "...&" ,"lt;p&gt;&lt;", "lt;/a&gt;at", "'", "&amp;#039;s", ".&", "who", "is",  "PM" ,"AM", "cdata" ,"]",">","<","video","world", "news","bbc","top","stories","breaking","CDATA","[ ["]

data = data.decode('utf-8')
#print data
for wordlist in delete_to_list:
#	print wordlist
        data = data.replace(wordlist,"")
	#data1=data1+" "+line

#print data

	#print line1

print "Processing nouns..."

blob = TextBlob(data)
a=blob.noun_phrases
#print a
		
#b=data.split(' ')
#t=TextBlob(b)

cnt=(Counter(a).most_common(100))
print cnt
file = open("cleared.json", "w")
for words in cnt:
	file.write(words[0]+"\n")

print "Nouns listed Successfully"
print "Writing to file..."
print "Done Writing"
file.close()
print "Process Completed Successfully."
#a=TextBlob(data)
#print a.tags
