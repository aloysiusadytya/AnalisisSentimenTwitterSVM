# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:36:35 2021

@author: Hewlett-Packard
"""
from klasifikasiKelas3 import KlasifikasiSVM as clsvm
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']


k=3
c = 0.1
print('K = 3')
print('-------------------')
svm = clsvm.LinearSVM(k, X, y, c)
akurasi = svm[0]*100
recall = svm[1]*100
precision = svm[2]*100
print('Linear')
print(recall)
print(precision)
print(akurasi)
print('====================')

# svm2 = clsvm.RbfSVM(k, X, y)
# akurasi2 = svm2[0]*100
# recall2 = svm2[1]*100
# precision2 = svm2[2]*100
# print("RBF")
# print(recall2)
# print(precision2)
# print(akurasi2)
# print('====================')

# svm3 = clsvm.PolySVM(k, X, y)
# akurasi3 = svm3[0]*100
# recall3 = svm3[1]*100
# precision3 = svm3[2]*100
# print('Poly')
# print(recall3)
# print(precision3)
# print(akurasi3)
