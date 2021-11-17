# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:38:43 2021

@author: Hewlett-Packard
"""
import pandas as pd
from degreeTerbaik import testDegree

dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']

k = 10

# Poly
poly1 = testDegree.PolySVM(0.001, X, y, k)
poly1 = poly1[0]
poly2 = testDegree.PolySVM(0.01, X, y, k)
poly2 = poly2[0]
poly3 = testDegree.PolySVM(0.1, X, y, k)
poly3 = poly3[0]
poly4 = testDegree.PolySVM(1, X, y, k)
poly4 = poly4[0]
poly5 = testDegree.PolySVM(2, X, y, k)
poly5 = poly5[0]
poly6 = testDegree.PolySVM(3, X, y, k)
poly6 = poly6[0]
poly7 = testDegree.PolySVM(4, X, y, k)
poly7 = poly7[0]
poly8 = testDegree.PolySVM(5, X, y, k)
poly8 = poly8[0]
poly9 = testDegree.PolySVM(6, X, y, k)
poly9 = poly9[0]
poly10 = testDegree.PolySVM(7, X, y, k)
poly10 = poly10[0]