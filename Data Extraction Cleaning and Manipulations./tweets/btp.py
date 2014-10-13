import requests  
import sys  
import time  
import oauth2 as oauth
import json
from datetime import datetime  
   
  

consumer_key='6zSyLNhbmD1O68uNhZtF16if12J'
consumer_secret='CbI4Ew3t4HLnkpGjBP7YC1Bm31HxTDJ9rQiERyiy37hGSdALyE12'
access_token = '298398033-jU0Q9NvuD2B0cmkiX97zgzoVig1Q3tgIgFSmj5Vx'
access_secret = 'mG6uiNPzu91V2I6KTCInm8Mh6NKorzGw5od4TNXknVd012f'

consumer = oauth.Consumer(key=consumer_key , secret=consumer_secret)
token=oauth.Token(key=access_token,secret=access_secret)
client=oauth.Client(consumer, token)
 
   
def store_tweets(keyword, results, max_id):  
   tweet_list = []  
     
   for item in results:  
     tweet_id = item['id_str']  
     tweet_text = item['text'].encode('utf-8', 'ignore')  
     if len(tweet_text) > 255:  
       tweet_text = tweet_text[0:255]  
     from_user = item['from_user'].encode('utf-8', 'ignore')  
     from_user_id = item['from_user_id']  
     from_user_name = item['from_user_name'].encode('utf-8', 'ignore')  
     profile_image = item['profile_image_url'].encode('utf-8', 'ignore')  
     created_at = datetime.strptime(item['created_at'][:-6], "%a, %d %b %Y %H:%M:%S")  
       
     tweet_list.append((keyword, tweet_id, tweet_text, from_user, from_user_id, from_user_name, profile_image, created_at))  
       
   # Now store the tweet list in a database or file  
   return  
   
   
   
def search_tweets(keyword, max_id = '', result_type = 'mixed'):  
   url = 'http://api.twitter.com/1.1/search/search.json'  
     
   params = {'q': keyword, 'rpp': '100'}  
     
   if len(max_id) > 0:  
     params['since_id'] = max_id  
       
   params['result_type'] = result_type  
   r = requests.get(url, params=params)  
   time.sleep(5)  
     
   if r.status_code != 200:  
     print r.status_code  
     print r.text  
     time.sleep(30)  
     return r.status_code  
   
   json_content = r.json  
     
   max_id = json_content['max_id_str']  
     
   while True:  
     results = json_content['results']  
     if len(results) == 0:  
       print "no result"  
       break  
         
     store_tweets(keyword, results, max_id)  
       
     if 'next_page' in json_content.keys():  
       next_page = json_content['next_page']  
     else:  
       break  
       
     r = requests.get(url + next_page)  
     time.sleep(5)  
     print r.status_code  
     if r.status_code != 200:  
       print r.status_code  
       print r.text  
       time.sleep(30)  
       return r.status_code  
   
     json_content = r.json  
       
     
     
if __name__ == "__main__" :  
   keyword = 'python'  
   search_tweets(keyword)  
     
