import requests
import sys
import time
import oauth2 as oauth
import json
from datetime import datetime



consumer_key='6zSyLNhbmD1O68uNhZt16ifJ'
consumer_secret='CbI4Ew3t4HLnkpGjBYC1Bm31HxTDJ9rQiERyiy37hGSdALyE'

consumer = oauth.Consumer(key=consumer_key , secret=consumer_secret)

request_token_url='http://twitter.com/oauth/request_token'

client=oauth.Client(consumer)

resp,content=client.request(request_token_url,"GET")
print resp
print content

