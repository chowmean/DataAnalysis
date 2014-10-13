_author_ = 'chowmean'
import oauth2 as oauth
from datetime import datetime
import json
import csv


consumer_key='6zSyLNhbmD1O68uNhZtF16ifJ'
consumer_secret='CbI4Ew3t4HLnkpGjBP7YC1Bm31HxTDJ9rQiERy12iy37hGSdALyE'
access_token='298398033-jU0Q9NvuD2B0cmkiX97zgzoVig1Q3tgIgFSmj5Vx'
access_secret='mG6uiNPzu91V2I6KTCInm8Mh6NKorzG3w5od4TNXknVd1230f'

consumer=oauth.Consumer(key=consumer_key,secret=consumer_secret)
token=oauth.Token(key=access_token,secret=access_secret)
client=oauth.Client(consumer,token)

total_pulled=0
fixed_url='https://api.google.com/1.1/statuses/user_timeline.json?'
userid='nike'
count=200

parameter_url='include_entities=true&include_rts=false&screen_name='+userid+'&count='+str(count)

request_url=fixed_url+parameter_url

def parse_date(created_at):
	temp_at = created_at[:19] + created_at[25:30]
	d=datetime.strptime(time_at, '%a %b %d %H:%M:%S %Y')
	yyyy_mm_dd=d.strftime('%Y-%m-%d')
	return yyyy_mm_dd

outfile=open('test_tweets.tsv','wt')
tc = 0
for loop in range(20):
	header,response=client.request(request_url)
	total_pulled+=len(json.loads(response))
	load=json.load(response)
	for status in load:
		created_at=status["created_at"]
		if parse_date(created_at) >= '2014-01-01' and parse_date(created_at)<='2014-04-20':
			print"(%s) @%s %s %s %s" % (status["created_at"],status["user"]["screen_name"],status["text"],status["retweet_count"],status_id)
			tc+=1
			x=status["text"].encode('utf-8',errors='replace')
			x=x.replace('\n',' ')
			outfile.write(str(status["id"])+'\t'+str(x)+'\t'+str(status["retweet_count"])+'\n')
	last_id=int(status["id"]) 
	max_id=str(int(last_id-1))
	parameter_url = 'include_entities=true&include_rts=true&screen_name='+userid+'&count='+str(count)+'&max_id='+str(max_id)
	request_url = fixed_url + parameter_url
print total_pulled
print tc


  
