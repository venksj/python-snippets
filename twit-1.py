from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import textblob as TextBlob

ckey = 'aeJrIGwoIiCk6mBUoXctH1Zqy'
csecret = 'qwKWyGkNkNdKVuPlnQvwjSQ9z0FwCqSpThdzMUkBjkFjFAcZfH'
atoken = '93027311-xGcSYdxakwLq2kKV7YU3q2ldPWrhbm8aYV9obHZ2H'
asecret = '7Vz0E5DJPlV4s2555smwrSRPx1Rdsh86g3CxZ0EVIOIzV'


class VJListener(StreamListener):
    def on_data(self, data):
        try:
            #print data
            data = data + '\n'

            f = open('tweets.txt', 'a')
            f.write(data)
            f.close()
        except BaseException, e:
            print "Failed: ", str(e)
            time.sleep(5)

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    vj = VJListener()
    tstream = Stream(auth, vj)
    tstream.filter(track=['kejriwal', '#aap'])



