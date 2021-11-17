# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:53:59 2021

@author: Hewlett-Packard
"""
from cmKelas import CM
import pandas as pd


dataset = pd.read_excel('HasilVaderMaretJuniId.xlsx')
X = dataset['Tweet']
y = dataset['label']

# linear
# cmLineark3 = CM.LinearSVM(3, X, y)
# cmLineark5 = CM.LinearSVM(5, X, y)
cmLineark10 = CM.LinearSVM(10, X, y)

# # RBF
# cmRbfk3 = CM.RbfSVM(3, X, y)
# cmRbfk5 = CM.RbfSVM(5, X, y)
cmRbfk10 = CM.RbfSVM(10, X, y)

# # Poly
# cmPolyk3 = CM.PolySVM(3, X, y)
# cmPolyk5 = CM.PolySVM(5, X, y)
cmPolyk10 = CM.PolySVM(10, X, y)


# # Akurasi
# akurasiLinearK3 = cmLineark3[1]
# # akurasiTotalK3 = cmLineark3[2] #cek akurasi percobaan
# akurasiLinearK4 = cmLineark5[1]
# akurasiLinearK5 = cmLineark10[1]

# akurasiRbfK3 = cmRbfk3[1]
# akurasiRbfK5 = cmRbfk5[1]
# akurasiRbfK10 = cmRbfk10[1]

# akurasiPolyK3 = cmPolyk3[1]
# akurasiPolyK5 = cmPolyk5[1]
# akurasipolyK10 = cmPolyk10[1]

