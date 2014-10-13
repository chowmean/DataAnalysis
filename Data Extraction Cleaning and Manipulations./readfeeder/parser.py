import re
import time
import glob
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
			print "Description ("+str(j)+") = > "+ title+"\n\n\n\n"
		
			j=j+1
	except Exception, e:
		print str(e)
	i=i+1
