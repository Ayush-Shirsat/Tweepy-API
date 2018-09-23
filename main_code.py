from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import twitter_credentials

class StdOutListener(StreamListener):

	def __init__(self):
		self.counter = 0


	def on_data(self, data):
		self.counter += 1
		if self.counter > 200: # limit the stream to 200 tweets
			sys.exit() 
		else:
			print(data) #Display tweets as they stream
			with open('fetched_tweets.json','a+') as tf: #Save tweets in json format
				tf.write(data)

		return True

	def on_error(self, status):
		print(status) # Print error (if any)

if __name__== "__main__":

	listener = StdOutListener()
	auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
	auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

	stream = Stream(auth, listener)

	stream.filter(track=['football']) # Set category of tweets by filtering track
end

