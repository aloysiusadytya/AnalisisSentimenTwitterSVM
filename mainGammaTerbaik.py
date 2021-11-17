# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:06:14 2021

@author: Hewlett-Packard
"""

import pandas as pd
from gammaTerbaik import testGamma

dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']

k = 3

# # RBF
# rbf1 = testGamma.RbfSVM(0.01, X, y, k)
# rbf1 = rbf1[0]
# rbf2 = testGamma.RbfSVM(0.1, X, y, k)
# rbf2 = rbf2[0]
# rbf3 = testGamma.RbfSVM(1, X, y, k)
# rbf3 = rbf3[0]
# rbf4 = testGamma.RbfSVM(2, X, y, k)
# rbf4 = rbf4[0]
# rbf5 = testGamma.RbfSVM(3, X, y, k)
# rbf5 = rbf5[0]
# rbf6 = testGamma.RbfSVM(4, X, y, k)
# rbf6 = rbf6[0]
# rbf7 = testGamma.RbfSVM(5, X, y, k)
# rbf7 = rbf7[0]
# rbf8 = testGamma.RbfSVM(6, X, y, k)
# rbf8 = rbf8[0]
# rbf9 = testGamma.RbfSVM(7, X, y, k)
# rbf9 = rbf9[0]
# rbf10 = testGamma.RbfSVM(8, X, y, k)
# rbf10 = rbf10[0]
# rbf11 = testGamma.RbfSVM(9, X, y, k)
# rbf11 = rbf11[0]
# rbf12 = testGamma.RbfSVM(10, X, y, k)
# rbf12 = rbf12[0]
# rbf13 = testGamma.RbfSVM(11, X, y, k)
# rbf13 = rbf13[0]
# rbf14 = testGamma.RbfSVM(12, X, y, k)
# rbf14 = rbf14[0]
# rbf15 = testGamma.RbfSVM(13, X, y, k)
# rbf15 = rbf15[0]
# rbf16 = testGamma.RbfSVM(14, X, y, k)
# rbf16 = rbf16[0]
# rbf17 = testGamma.RbfSVM(15, X, y, k)
# rbf17 = rbf17[0]
# rbf18 = testGamma.RbfSVM(16, X, y, k)
# rbf18 = rbf18[0]

# rbf19 = testGamma.RbfSVM('scale', X, y, k)
# rbf19 = rbf19[0]

# # Poly
# poly1 = testGamma.PolySVM(0.01, X, y, k)
# poly1 = poly1[0]
# poly2 = testGamma.PolySVM(0.1, X, y, k)
# poly2 = poly2[0]
# poly3 = testGamma.PolySVM(1, X, y, k)
# poly3 = poly3[0]
# poly4 = testGamma.PolySVM(2, X, y, k)
# poly4 = poly4[0]
# poly5 = testGamma.PolySVM(3, X, y, k)
# poly5 = poly5[0]
# poly6 = testGamma.PolySVM(4, X, y, k)
# poly6 = poly6[0]
# poly7 = testGamma.PolySVM(5, X, y, k)
# poly7 = poly7[0]
# poly8 = testGamma.PolySVM(6, X, y, k)
# poly8 = poly8[0]
# poly9 = testGamma.PolySVM(7, X, y, k)
# poly9 = poly9[0]
# poly10 = testGamma.PolySVM(8, X, y, k)
# poly10 = poly10[0]
# poly11 = testGamma.PolySVM(9, X, y, k)
# poly11 = poly11[0]
# poly12 = testGamma.PolySVM(10, X, y, k)
# poly12 = poly12[0]
# poly13 = testGamma.PolySVM(11, X, y, k)
# poly13 = poly13[0]
# poly14 = testGamma.PolySVM(12, X, y, k)
# poly14 = poly14[0]
# poly15 = testGamma.PolySVM(13, X, y, k)
# poly15 = poly15[0]
# poly16 = testGamma.PolySVM(14, X, y, k)
# poly16 = poly16[0]
# poly17 = testGamma.PolySVM(15, X, y, k)
# poly17 = poly17[0]
# poly18 = testGamma.PolySVM(16, X, y, k)
# poly18 = poly18[0]

# poly19 = testGamma.PolySVM('scale', X, y, k)
# poly19 = poly19[0]

