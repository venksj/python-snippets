import json
import pandas as pd
import matplotlib.pyplot as plt

tpath = 'tweets.txt'
tdata = []


tfile = open(tpath, 'r')

for line in tfile:
    try:
        tw = json.loads(line)
        #print tw
        tdata.append(tw)
    except:
        continue

tdf = pd.DataFrame()

tdf['text'] = map(lambda t: t['text'], tdata)
tdf['lang'] = map(lambda t: t['lang'], tdata)
tdf['country'] = map(lambda t: t['place']['country'] if t['place'] != None else None, tdata)

tc = tdf['text'].count()
print "Total Tweets: ", tc

tl = tdf['lang'].value_counts()

print "Tweets by lang: " 
print tl
