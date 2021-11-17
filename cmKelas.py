# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:51:32 2021

@author: Hewlett-Packard
"""

from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np

class CM:
    def LinearSVM(k, X, y):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        cm = []
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='linear', C=10)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            cm.append(confusion_matrix(y_test,y_pred))
            akurasiTotal = np.mean(akurasi)
        
        return cm, akurasi, akurasiTotal
        
    def RbfSVM(k, X, y):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        cm=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='rbf', C=5, gamma = 9)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            cm.append(confusion_matrix(y_test,y_pred))
            akurasiTotal = np.mean(akurasi)
            
        return cm, akurasi, akurasiTotal
        
    def PolySVM(k, X, y):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        cm=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='poly', C=35, gamma = 'scale', degree = 2)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            cm.append(confusion_matrix(y_test,y_pred))
            akurasiTotal = np.mean(akurasi)
            
        return cm, akurasi, akurasiTotal