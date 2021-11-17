# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:01:01 2021

@author: Hewlett-Packard
"""

import snscrape.modules.twitter as sntwitter
import pandas as pd


maxTweets = 8000

tweets_list2 = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('belajar daring lang:id since:2020-03-13 until:2020-06-30').get_items()):
    if i>maxTweets:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# tweets_df2.to_csv('dataBaruMaretJuni.csv', sep=',', index=False)

