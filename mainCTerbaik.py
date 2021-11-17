# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:22:49 2021

@author: Hewlett-Packard
"""

import pandas as pd
from CTerbaik import testC


dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']

k = 3


# # linear
# linear1 = testC.LinearSVM(0.1, X, y, k)
# linear1 = linear1[0]
# linear2 = testC.LinearSVM(0.5, X, y, k)
# linear2 = linear2[0]
# linear3 = testC.LinearSVM(1, X, y, k)
# linear3 = linear3[0]
# linear4 = testC.LinearSVM(5, X, y, k)
# linear4 = linear4[0]
linear5 = testC.LinearSVM(10, X, y, k)
linear5 = linear5[0]
# linear6 = testC.LinearSVM(15, X, y, k)
# linear6 = linear6[0]
# linear7 = testC.LinearSVM(20, X, y, k)
# linear7 = linear7[0]
# linear8 = testC.LinearSVM(25, X, y, k)
# linear8 = linear8[0]
# linear9 = testC.LinearSVM(30, X, y, k)
# linear9 = linear9[0]
# linear10 = testC.LinearSVM(35, X, y, k)
# linear10 = linear10[0]
# linear11 = testC.LinearSVM(40, X, y, k)
# linear11 = linear11[0]
# linear12 = testC.LinearSVM(45, X, y, k)
# linear12 = linear12[0]

# # RBF
# rbf1 = testC.RbfSVM(0.1, X, y, k)
# rbf1 = rbf1[0]
# rbf2 = testC.RbfSVM(0.5, X, y, k)
# rbf2 = rbf2[0]
# rbf3 = testC.RbfSVM(1, X, y, k)
# rbf3 = rbf3[0]
# rbf4 = testC.RbfSVM(5, X, y, k)
# rbf4 = rbf4[0]
# rbf5 = testC.RbfSVM(10, X, y, k)
# rbf5 = rbf5[0]
# rbf6 = testC.RbfSVM(15, X, y, k)
# rbf6 = rbf6[0]
# rbf7 = testC.RbfSVM(20, X, y, k)
# rbf7 = rbf7[0]
# rbf8 = testC.RbfSVM(25, X, y, k)
# rbf8 = rbf8[0]
# rbf9 = testC.RbfSVM(30, X, y, k)
# rbf9 = rbf9[0]
# rbf10 = testC.RbfSVM(35, X, y, k)
# rbf10 = rbf10[0]
# rbf11 = testC.RbfSVM(40, X, y, k)
# rbf11 = rbf11[0]
# rbf12 = testC.RbfSVM(45, X, y, k)
# rbf12 = rbf12[0]
# rbf13 = testC.RbfSVM(50, X, y, k)
# rbf13 = rbf13[0]
# rbf14 = testC.RbfSVM(55, X, y, k)
# rbf14 = rbf14[0]
# rbf15 = testC.RbfSVM(60, X, y, k)
# rbf15 = rbf15[0]
# rbf16 = testC.RbfSVM(65, X, y, k)
# rbf16 = rbf16[0]
# rbf17 = testC.RbfSVM(70, X, y, k)
# rbf17 = rbf17[0]


# # Poly
# poly1 = testC.PolySVM(0.1, X, y, k)
# poly1 = poly1[0]
# poly2 = testC.PolySVM(0.5, X, y, k)
# poly2 = poly2[0]
# poly3 = testC.PolySVM(1, X, y, k)
# poly3 = poly3[0]
# poly4 = testC.PolySVM(5, X, y, k)
# poly4 = poly4[0]
# poly5 = testC.PolySVM(10, X, y, k)
# poly5 = poly5[0]
# poly6 = testC.PolySVM(15, X, y, k)
# poly6 = poly6[0]
# poly7 = testC.PolySVM(20, X, y, k)
# poly7 = poly7[0]
# poly8 = testC.PolySVM(25, X, y, k)
# poly8 = poly8[0]
# poly9 = testC.PolySVM(30, X, y, k)
# poly9 = poly9[0]
# poly10 = testC.PolySVM(35, X, y, k)
# poly10 = poly10[0]
# poly11 = testC.PolySVM(40, X, y, k)
# poly11 = poly11[0]
# poly12 = testC.PolySVM(45, X, y, k)
# poly12 = poly12[0]
# poly13 = testC.PolySVM(50, X, y, k)
# poly13 = poly13[0]
# poly14 = testC.PolySVM(55, X, y, k)
# poly14 = poly14[0]





