
import time, tweepy, sys



consumer_key='7ZZwelEhWFW2DQSTO9aYRJ3Oc'
consumer_secret='wZiM9KpYeyd87IrXcgxSOwijq51ZYiSLbnLnZrtT6lTSz6IFp6'
access_token_key='298398033-jU0Q9NvuD2B0cmkiX97zgzoVig1Q3tgIgFSmj5Vx'
access_token_secret='mG6uiNPzu91V2I6KTCInm8Mh6NKorzGw5od4TNXknVd0f'

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print 'Ran on_status'

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        print 'Ok, this is actually running'


l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
#setTerms = ['hello', 'goodbye', 'goodnight', 'good morning']
setTerms = ['twitter']
streamer.filter(track = setTerms)
