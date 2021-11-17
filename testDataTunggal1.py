# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 12:41:26 2021

@author: Hewlett-Packard
"""
import pandas as pd
from klasifikasiKelas3 import KlasifikasiSVM as clsvm
from PreprocessingLexicon2 import PreprocessingLexicon as pl
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer


data = ['kakkk pagi pagi lohh aku dah bantun pagi hihi biar rezeki nya ga patok ayamm kakakkk ga gedor dm acuuu biarr semangatt nichhh daring nyaaa']
# data = pd.DataFrame(data)
data = pd.Series(data)
# dataTunggal = clsvm.clSVMTunggal(data)
# vectorizer = TfidfVectorizer(norm = 'l1')
# vectorizer.fit(data)
# data = vectorizer.transform(data)
dataTunggal = clsvm.clSVMTunggal(data)
dataTunggal = pd.DataFrame(dataTunggal, columns=['label'])

        # polaritasDataTunggal
dataTunggal['label2'] = dataTunggal['label'].apply(lambda c: 'POSITIF' if c >0 else 'NEGATIF')
        
sentimen = dataTunggal['label2']
sentimen = sentimen.to_string(index=False)