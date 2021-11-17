# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 21:46:10 2021

@author: Hewlett-Packard
"""
from PreprocessingLexicon2 import PreprocessingLexicon as pl
import pandas as pd
import numpy as np


# CleanDataMaretJuni.xlsx ditranslate kembali menjadi HasilTranslateMaretJuni.xlsx

df = pd.read_excel('HasilTranslateMaretJuni.xlsx').astype(str)
# df = df['Tweet']

df['scores'] = df['Tweet'].apply(lambda x: pl.Labeling(x))
df['compound']  = df['scores'].apply(lambda score_dict: score_dict['compound'])
df['label'] = df['compound'].apply(lambda c: 1 if c >0 else 0 if c==0 else -1)

indexNames = df[(df['label'] == 0)].index
a = df.drop(indexNames, inplace=True)


hasilLexicon = df[['Tweet','label']]
hasilLexicon['Tweet'].replace('', np.nan, inplace=True)
hasilLexicon.dropna(subset=['Tweet'], inplace =True)


positif = hasilLexicon[hasilLexicon['label']==1]['label'].count()
negatif = hasilLexicon[hasilLexicon['label']==-1]['label'].count()

dataPos = hasilLexicon[hasilLexicon['label']==1]
dataNeg = hasilLexicon[hasilLexicon['label']==-1]

dataPos = dataPos[:1550]
dataGabung = [dataPos, dataNeg]
dataset = pd.concat(dataGabung, ignore_index=True)
dataset  = dataset.sample(frac=1).reset_index(drop=True)
# dataset.to_excel('HasilVaderMaretJuni.xlsx')

