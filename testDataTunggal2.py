# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:47:54 2021

@author: Hewlett-Packard
"""
from klasifikasiKelas3 import KlasifikasiSVM as clsvm
from PreprocessingLexicon2 import PreprocessingLexicon as pl
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import pandas as pd
import numpy as np


data = {'Text':['kakkk pagi pagi lohh aku dah bantun pagi hihi biar rezeki nya ga patok ayamm kakakkk ga gedor dm acuuu biarr semangatt nichhh daring nyaaa']}
df = pd.DataFrame(data)
df['remove_user'] = np.vectorize(pl.remove_pattern)(df, "@[\w]*")
# df = df['remove_user']

  # remove angka
df['remove_http'] = df['remove_user'].apply(lambda x: pl.remove(x))
        
emoticons = pl.getEmoticons(df)
stopwords_indonesia = pl.getStopwords(df)
stemmer = pl.getStemming(df)
        
#cleaning
df['tweet_clean'] = df['remove_http'].apply(lambda x: pl.cleanTweets(x,df))
        
        # punct
        # remove_punct = pl.removePunct(self.df)
df['Tweet'] = df['tweet_clean'].apply(lambda x: pl.removePunct(x))
df = pd.DataFrame(df['Tweet'])


# df = df.values.tolist()
df = df.squeeze()


df = pd.Series(df)
# dataTunggal = clsvm.clSVMTunggal(data)
# vectorizer = TfidfVectorizer(norm = 'l1')
# vectorizer.fit(data)
# data = vectorizer.transform(data)
dataTunggal = clsvm.clSVMTunggal(df)
dataTunggal = pd.DataFrame(dataTunggal, columns=['label'])

        # polaritasDataTunggal
dataTunggal['label2'] = dataTunggal['label'].apply(lambda c: 'POSITIF' if c >0 else 'NEGATIF')
        
sentimen = dataTunggal['label2']
sentimen = sentimen.to_string(index=False)

