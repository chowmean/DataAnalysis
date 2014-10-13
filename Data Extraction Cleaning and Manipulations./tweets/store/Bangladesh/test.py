from textblob import TextBlob 			#library consisting of Sentiment analysis and NLTK 
import json 					# library to process json
from pprint import pprint 			# library to print json 
import glob 					# library to read folder 
from collections import Counter 		# library to count frequency of words
from geopy.geocoders import GoogleV3  		# library to get the latitude and longitude of each tweet 
geolocator = GoogleV3()     			# googleV3 object
cnt=0
cnt_pos=0
cnt_none=0
datatokeep=''
texttowrite=[]
locationtowrite=[]
array = glob.glob("*.json")			#array consisting of list of all .json files
for arrays in array: 				# processing each file one by one
	json_data=open(arrays, 'r')		#open particular file
	if(arrays!='suggestion.json' and arrays!='Result.json' and arrays!='location.json' ):  #avoid these three files	
		data = json.load(json_data)						#load json data
	else:
		continue
	for datas in data:
		b=datas['text']										
		a=TextBlob(b)								#instantiatng TextBlob object
		print a.sentiment							#calculate sentiment
		print "\n"
		loc= datas['user']['location']						#getting user location
		try:
			address, (latitude, longitude) = geolocator.geocode(loc)	#getting latitude and longitude
		
			dictionary=dict({'address':address,'latitude':latitude,'longitude':longitude})		
			texttowrite.append(dictionary)					#appending to texttowrite variable 
			locationtowrite.append(address)			
			print latitude
			print longitude
		except:
			print "location skipped"
		if(a.sentiment.polarity<0):
			cnt=cnt+1		
			print (a.noun_phrases)						#calculating noun phrases
			datatokeep=datatokeep + datas['text']
		elif (a.sentiment.polarity>0):
			cnt_pos=cnt_pos+1
		else:
			cnt_none=cnt_none+1
	json_data.close()
print "Result of Analysis: Total Analysed tweets="+str(cnt+cnt_pos+cnt_none)			
print "Total Negative="+str(cnt)
print "Total Positive="+str(cnt_pos)
print "No response="+str(cnt_none)

towrite=json.dumps([{'Total':str(cnt+cnt_pos+cnt_none)},{'Positive':str(cnt_pos)},{'Negative':str(cnt)},{'Neutral':str(cnt_none)}])
file = open("Result.json", "w")
file.write(towrite)								#writing total summary in Result.json
file.close()

file = open("location.json", "w")
file.write(json.dumps(texttowrite))						#writing location in location files
file.close()					

#print datatokeep
datatokeep=TextBlob(datatokeep)
a=datatokeep.noun_phrases
cnt=(Counter(a).most_common(10))
print cnt
file = open("suggestion.json", "w")						#writing suggestions in suggestion files
for words in cnt:
	file.write(words[0]+"\n")
print texttowrite
print locationtowrite
