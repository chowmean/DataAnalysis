import oauth2
import time
import urllib2
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"
params = {
	"oauth_version": "1.0",
	"oauth_nonce": oauth2.generate_nonce(),
	"oauth_timestamp": int(time.time())
}


consumer_key='v4SaVwDXV34TWJwzW557UMTTnbS'
consumer_secret='Ylwqvuo7nqpwLRVPvshXQS3KpIe3kjjQTNXthhM9sr9wXQPKMcKj'
access_token='2531561155-KEVPxKVOdiRWtlkk6UdB4tnjE5PH8MXd8397B7GrV'
access_secret='ZSblc2gd4P9eVn2Bm15416nktFaaiz2pM66WIUCnoKOdDm9'


consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth2.Token(key=access_token, secret=access_secret)
params["oauth_consumer_key"] = consumer.key
params["oauth_token"] = token.key

prev_id = int("501332704705519617")
count=0
for i in range(100):
	url = url1
	params["q"] = "Government"
	params["count"] = 150
	params["geocode"] = "49.000000,32.010000,1000.0km"
#	params["lang"] = "English"
	params["locale"] = "en"
	params["location"] = "Ukraine"
	params["result_type"] = "popular" # Example Values: mixed, recent, popular
#	params["until"] = ""
#	params["since_id"] = ""

	params["max_id"] = str(prev_id)
	req=oauth2.Request(method="GET",url=url,parameters=params)
	signature_method=oauth2.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method,consumer,token)
	headers=req.to_header()
	url=req.to_url()
#	print headers
#	print url
	response=urllib2.Request(url)
	print (url)
	data=json.load(urllib2.urlopen(response))

	
	if data["statuses"] == []:
		print "end of data"
		break
	else:
		prev_id = int(data["statuses"][1]["id"]) - 1
		print prev_id, i
		count=count+1;
	print data["statuses"]
	print "\n count: "
	print count
	f = open("store/Ukraine/outfile_" + str(i) + ".json", "w")
	json.dump(data["statuses"], f)
	f.close()
	time.sleep(5)
