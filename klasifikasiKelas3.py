# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 20:22:21 2021

@author: Hewlett-Packard
"""

from sklearn.model_selection import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import numpy as np

class KlasifikasiSVM:
    def LinearSVM(k, X, y, c):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='linear', C=c)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
                        
        akurasiTotal = np.mean(akurasi)
        recallTotal = np.mean(recall)
        precisionTotal = np.mean(precision)
        sv = clf.support_vectors_
        return akurasiTotal, recallTotal, precisionTotal, sv
        
    def RbfSVM(k, X, y, c, g):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='rbf', C=c, gamma = g)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            
        akurasiTotal = np.mean(akurasi)
        recallTotal = np.mean(recall)
        precisionTotal = np.mean(precision)
        return akurasiTotal, recallTotal, precisionTotal
        
    def PolySVM(k, X, y,c, g, d):
        skf = KFold(n_splits=k)
        akurasi = []
        recall = []
        precision=[]
        for train_index, test_index in skf.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]

            vectorizer = TfidfVectorizer(norm = 'l1')

            X_train=vectorizer.fit_transform(X_train)
            X_test=vectorizer.transform(X_test)
            clf=svm.SVC(kernel='poly', C=c, gamma = g, degree = d)
            clf.fit(X_train,y_train)
            
            y_pred = clf.predict(X_test)
            akurasi.append(metrics.accuracy_score(y_test, y_pred))
            recall.append(metrics.recall_score(y_test, y_pred))
            precision.append(metrics.precision_score(y_test, y_pred))
            
        akurasiTotal = np.mean(akurasi)
        recallTotal = np.mean(recall)
        precisionTotal = np.mean(precision)
        return akurasiTotal, recallTotal, precisionTotal
            

    
    def clSVMTunggal(X_test):
        dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
        X = dataset['Tweet']
        y = dataset['label']

        skf = KFold(n_splits=10)
        X_train = X
        y_train = y
        
        vectorizer = TfidfVectorizer(norm = 'l1')

        X_train=vectorizer.fit_transform(X_train)
        X_test=vectorizer.transform(X_test)
        clf=svm.SVC(kernel='rbf', C=5, gamma = 9)
        clf.fit(X_train,y_train)
        print(X_test)
            
        y_pred = clf.predict(X_test)
        return y_pred
    
    def confMatrix(self):
        cm = confusion_matrix(self.y_test, self.y_pred)
        cr = classification_report(self.y_test, self.y_pred)
        return cr
    
    
    