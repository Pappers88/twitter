import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'VikhlihyfK4Ws6PdsXUD4LSDp'
CONSUMER_SECRET = 'YBzNrGmuHZ6tFIRknBgMqfINlL1eWTkCzm9pqgBfwIqM7lIdkH'
OAUTH_TOKEN = '816925867708469248-wqOqxf4ySj9zZMpqKtAtZp0xqfodYyb'
OAUTH_TOKEN_SECRET = 'T7JJd3CWlCdBTf7SrTULCKP6eBDuJwNUFX5ybtKAsVDLO'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.get_user('@madonna')

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print status.text