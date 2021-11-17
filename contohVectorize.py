# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:51:23 2021

@author: Hewlett-Packard
"""

from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np

dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']


k=3

skf = KFold(n_splits=k)
for train_index, test_index in skf.split(X):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

    vectorizer = TfidfVectorizer(norm = 'l1')

    X_train=vectorizer.fit_transform(X_train)
    X_test=vectorizer.transform(X_test)
    print(X_train)
            
