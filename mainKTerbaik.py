# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:00:50 2021

@author: Hewlett-Packard
"""

import pandas as pd
from KTerbaik import testK


dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']

# Linear
linearK3 = testK.LinearSVM(3,X, y)
linearK3 = linearK3[0]
linearK5 = testK.LinearSVM(5,X, y)
linearK5 = linearK5[0]
linearK10 = testK.LinearSVM(10,X, y)
linearK10 = linearK10[0]

# RBF
RbfK3 = testK.RbfSVM(3, X, y)
RbfK3 = RbfK3[0]
RbfK5 = testK.RbfSVM(5, X, y)
RbfK5 = RbfK5[0]
RbfK10 = testK.RbfSVM(10, X, y)
RbfK10= RbfK10[0]

# Poly
PolyK3 = testK.PolySVM(3, X, y)
PolyK3 = PolyK3[0]
PolyK5 = testK.PolySVM(5, X, y)
PolyK5 = PolyK5[0]
PolyK10 = testK.PolySVM(10, X, y)
PolyK10 = PolyK10[0]

