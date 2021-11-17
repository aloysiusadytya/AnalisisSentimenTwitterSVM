# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 20:56:43 2021

@author: Hewlett-Packard
"""

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np

data = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = data['Tweet']
y = data['label']
k = 10

skf = KFold(n_splits=k)
akurasi = []
recall = []
precision=[]
gamma=[]
for train_index, test_index in skf.split(X):
    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

    vectorizer = TfidfVectorizer(norm = 'l1')

    X_train=vectorizer.fit_transform(X_train)
    X_test=vectorizer.transform(X_test)
    clf=svm.SVC(kernel='poly', C=20, gamma = 'scale', degree = 2)
    clf.fit(X_train,y_train)
            
    y_pred = clf.predict(X_test)
    akurasi.append(metrics.accuracy_score(y_test, y_pred))
    recall.append(metrics.recall_score(y_test, y_pred))
    precision.append(metrics.precision_score(y_test, y_pred))
    gamma.append(clf._gamma)
            
akurasiTotal = np.mean(akurasi)
recallTotal = np.mean(recall)
precisionTotal = np.mean(precision)
gammaTotal = np.mean(gamma)