from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'VikhlihyfK4Ws6PdsXUD4LSDp'
CONSUMER_SECRET = 'YBzNrGmuHZ6tFIRknBgMqfINlL1eWTkCzm9pqgBfwIqM7lIdkH'
OAUTH_TOKEN = '816925867708469248-wqOqxf4ySj9zZMpqKtAtZp0xqfodYyb'
OAUTH_TOKEN_SECRET = 'T7JJd3CWlCdBTf7SrTULCKP6eBDuJwNUFX5ybtKAsVDLO'


keyword_list = ['python', 'java', 'c#', 'ruby']  # track list


class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)