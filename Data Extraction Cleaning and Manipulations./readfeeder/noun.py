#! /usr/bin/python
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
file1=open("/home/hduser/Desktop/hello.txt", "r")
for line in file1:
	extractor = ConllExtractor()
	blob = TextBlob(line,np_extractor=extractor)
	print  blob.noun_phrases
		
