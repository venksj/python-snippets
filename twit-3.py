import tweepy
import time
from textblob import TextBlob 

ckey = 'aeJrIGwoIiCk6mBUoXctH1Zqy'
csecret = 'qwKWyGkNkNdKVuPlnQvwjSQ9z0FwCqSpThdzMUkBjkFjFAcZfH'
atoken = '93027311-xGcSYdxakwLq2kKV7YU3q2ldPWrhbm8aYV9obHZ2H'
asecret = '7Vz0E5DJPlV4s2555smwrSRPx1Rdsh86g3CxZ0EVIOIzV'



if __name__ == '__main__':
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    api = tweepy.API(auth)
    public_tweets = api.search(['Trump', 'Kejriwal'])
    #public_tweets = api.search('Trump')

    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print (analysis.sentiment)




