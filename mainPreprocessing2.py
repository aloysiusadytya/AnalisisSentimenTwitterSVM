# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:19:24 2021

@author: Hewlett-Packard
"""

from PreprocessingLexicon2 import PreprocessingLexicon as pl
import pandas as pd
import numpy as np

df = pd.read_csv('dataBaruMaretJuni.csv')
df = df
df = df['Text']
df = df.to_frame()

df['remove_user'] = np.vectorize(pl.remove_pattern)(df, "@[\w]*")
# df = df['remove_user']

df.drop_duplicates(subset ="remove_user", keep = 'first', inplace = True)
 # remove angka
df['remove_http'] = df['remove_user'].apply(lambda x: pl.remove(x))
df.sort_values("remove_http", inplace = True)
df.drop_duplicates(subset ="remove_http", keep = 'first', inplace = True)
        
emoticons = pl.getEmoticons(df)
stopwords_indonesia = pl.getStopwords(df)
stemmer = pl.getStemming(df)
        
#cleaning
df['tweet_clean'] = df['remove_http'].apply(lambda x: pl.cleanTweets(x,df))
        
        # punct
        # remove_punct = pl.removePunct(self.df)
df['Tweet'] = df['tweet_clean'].apply(lambda x: pl.removePunct(x))
df.drop_duplicates(subset ="Tweet", keep = 'first', inplace = True) 
df.sort_values("Tweet", inplace = True)
df = pd.DataFrame(df['Tweet'])
# mengurutkan index
df = df.sort_index()
# df.to_csv('CleanDataMaretAprilBARU.csv',encoding='utf8', index=False)
# df.to_excel('CleanDataMaretJuni.xlsx')


