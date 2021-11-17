# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:10:44 2021

@author: Hewlett-Packard
"""


from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np

class testC:
    def LinearSVM(C, X, y, k):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='linear', C=C)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            
        akurasiTotal = np.mean(akurasi)
        recallTotal = np.mean(recall)
        precisionTotal = np.mean(precision)
        return akurasiTotal, recallTotal, precisionTotal
        
    def RbfSVM(C, X, y, k):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='rbf', C=C)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            
        akurasiTotal = np.mean(akurasi)
        recallTotal = np.mean(recall)
        precisionTotal = np.mean(precision)
        return akurasiTotal, recallTotal, precisionTotal
        
    def PolySVM(C, X, y, k):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='poly', C=C)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            
        akurasiTotal = np.mean(akurasi)
        recallTotal = np.mean(recall)
        precisionTotal = np.mean(precision)
        return akurasiTotal, recallTotal, precisionTotal