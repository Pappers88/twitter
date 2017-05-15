import json
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

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
ESS_WOE_ID = 12602168

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
ess_trends = api.trends_place(ESS_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

ess_trends_set = set([trend['name']
                      for trend in ess_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print common_trends