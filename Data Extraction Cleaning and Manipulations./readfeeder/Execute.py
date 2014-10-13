import re
import time
import glob
array = glob.glob("*.py")
cnt=0
for arrays in array: 
	if(arrays[0]=='r'):
		execfile(arrays)
		cnt=cnt+1;
print "total news channels covered:"+str(cnt)
execfile("../readfeeder/parser.py")


#	a = open(arrays, 'r')
#	file=a.read()

#	try:
#		titles=re.findall(r'<title>(.*?)</title>',file)
#		for title in titles:
#			print "Description ("+str(j)+") = > "+ title+"\n\n\n\n"
#			j=j+1
#	except Exception, e:
#		print str(e)
#	i=i+1

	
