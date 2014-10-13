from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='7ZZwelEhWFW2DQSTO9aYRJ3Oc'
csecret='wZiM9KpYeyd87IrXcgxSOwijq51ZYiSLbnLnZrtT6lTSz6IFp6'
atoken='298398033-jU0Q9NvuD2B0cmkiX97zgzoVig1Q3tgIgFSmj5Vx'
asecret='mG6uiNPzu91V2I6KTCInm8Mh6NKorzGw5od4TNXknVd0f'

class listener(StreamListener):
	def on_data(self,data):
		print data
		return True
	def on_error(self,status):
		print status

auth = OAuthHandler(ckey,csecret)

auth.set_access_token(atoken,asecret)

twitterStream=Stream(auth,listener())
twitterStream.filter()

