# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:27:50 2021

@author: Hewlett-Packard
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PandasModel import PandasModel
import pandas as pd
import numpy as np
from PreprocessingLexicon2 import PreprocessingLexicon as pl
from klasifikasiKelas3 import KlasifikasiSVM as clsvm

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 711)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 120, 1011, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tombolBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.tombolBrowse.setGeometry(QtCore.QRect(20, 140, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tombolBrowse.setFont(font)
        self.tombolBrowse.setObjectName("tombolBrowse")
        self.showPath = QtWidgets.QLineEdit(self.centralwidget)
        self.showPath.setGeometry(QtCore.QRect(100, 140, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.showPath.setFont(font)
        self.showPath.setObjectName("showPath")
        self.labelDataMentah = QtWidgets.QLabel(self.centralwidget)
        self.labelDataMentah.setGeometry(QtCore.QRect(160, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelDataMentah.setFont(font)
        self.labelDataMentah.setObjectName("labelDataMentah")
        self.tableViewDataMentah = QtWidgets.QTableView(self.centralwidget)
        self.tableViewDataMentah.setGeometry(QtCore.QRect(20, 190, 371, 192))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableViewDataMentah.setFont(font)
        self.tableViewDataMentah.setObjectName("tableViewDataMentah")
        self.labelDataCleaningLexicon = QtWidgets.QLabel(self.centralwidget)
        self.labelDataCleaningLexicon.setGeometry(QtCore.QRect(120, 430, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelDataCleaningLexicon.setFont(font)
        self.labelDataCleaningLexicon.setObjectName("labelDataCleaningLexicon")
        self.tableViewCleaningLexicon = QtWidgets.QTableView(self.centralwidget)
        self.tableViewCleaningLexicon.setGeometry(QtCore.QRect(20, 460, 371, 192))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableViewCleaningLexicon.setFont(font)
        self.tableViewCleaningLexicon.setObjectName("tableViewCleaningLexicon")
        self.groupBoxUjiDataTunggal = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUjiDataTunggal.setGeometry(QtCore.QRect(440, 510, 571, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxUjiDataTunggal.setFont(font)
        self.groupBoxUjiDataTunggal.setAutoFillBackground(False)
        self.groupBoxUjiDataTunggal.setObjectName("groupBoxUjiDataTunggal")
        self.labelMasukanDataTunggal = QtWidgets.QLabel(self.groupBoxUjiDataTunggal)
        self.labelMasukanDataTunggal.setGeometry(QtCore.QRect(20, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelMasukanDataTunggal.setFont(font)
        self.labelMasukanDataTunggal.setObjectName("labelMasukanDataTunggal")
        self.lineEditDataTunggal = QtWidgets.QLineEdit(self.groupBoxUjiDataTunggal)
        self.lineEditDataTunggal.setGeometry(QtCore.QRect(150, 30, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditDataTunggal.setFont(font)
        self.lineEditDataTunggal.setObjectName("lineEditDataTunggal")
        self.labelHasilLexicon = QtWidgets.QLabel(self.groupBoxUjiDataTunggal)
        self.labelHasilLexicon.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelHasilLexicon.setFont(font)
        self.labelHasilLexicon.setObjectName("labelHasilLexicon")
        self.pushButtonProsesDataTunggal = QtWidgets.QPushButton(self.groupBoxUjiDataTunggal)
        self.pushButtonProsesDataTunggal.setGeometry(QtCore.QRect(480, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonProsesDataTunggal.setFont(font)
        self.pushButtonProsesDataTunggal.setObjectName("pushButtonProsesDataTunggal")
        self.lineEditHasilLexicon = QtWidgets.QLineEdit(self.groupBoxUjiDataTunggal)
        self.lineEditHasilLexicon.setGeometry(QtCore.QRect(150, 90, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditHasilLexicon.setFont(font)
        self.lineEditHasilLexicon.setObjectName("lineEditHasilLexicon")
        self.pushButtonResetDataTunggal = QtWidgets.QPushButton(self.groupBoxUjiDataTunggal)
        self.pushButtonResetDataTunggal.setGeometry(QtCore.QRect(480, 120, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonResetDataTunggal.setFont(font)
        self.pushButtonResetDataTunggal.setObjectName("pushButtonResetDataTunggal")
        self.groupBoxKlasifikasiSVM = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxKlasifikasiSVM.setGeometry(QtCore.QRect(440, 240, 571, 261))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxKlasifikasiSVM.setFont(font)
        self.groupBoxKlasifikasiSVM.setObjectName("groupBoxKlasifikasiSVM")
        self.groupBoxKFold = QtWidgets.QGroupBox(self.groupBoxKlasifikasiSVM)
        self.groupBoxKFold.setGeometry(QtCore.QRect(10, 20, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxKFold.setFont(font)
        self.groupBoxKFold.setObjectName("groupBoxKFold")
        self.radioButtonK3 = QtWidgets.QRadioButton(self.groupBoxKFold)
        self.radioButtonK3.setGeometry(QtCore.QRect(60, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonK3.setFont(font)
        self.radioButtonK3.setObjectName("radioButtonK3")
        self.radioButtonK10 = QtWidgets.QRadioButton(self.groupBoxKFold)
        self.radioButtonK10.setGeometry(QtCore.QRect(60, 70, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonK10.setFont(font)
        self.radioButtonK10.setObjectName("radioButtonK10")
        self.labelK = QtWidgets.QLabel(self.groupBoxKFold)
        self.labelK.setGeometry(QtCore.QRect(20, 30, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelK.setFont(font)
        self.labelK.setObjectName("labelK")
        self.radioButtonK5 = QtWidgets.QRadioButton(self.groupBoxKFold)
        self.radioButtonK5.setGeometry(QtCore.QRect(60, 50, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonK5.setFont(font)
        self.radioButtonK5.setObjectName("radioButtonK5")
        self.groupBoxSVM = QtWidgets.QGroupBox(self.groupBoxKlasifikasiSVM)
        self.groupBoxSVM.setGeometry(QtCore.QRect(10, 130, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBoxSVM.setFont(font)
        self.groupBoxSVM.setObjectName("groupBoxSVM")
        self.radioButtonPoly = QtWidgets.QRadioButton(self.groupBoxSVM)
        self.radioButtonPoly.setGeometry(QtCore.QRect(100, 70, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonPoly.setFont(font)
        self.radioButtonPoly.setObjectName("radioButtonPoly")
        self.labelKernel = QtWidgets.QLabel(self.groupBoxSVM)
        self.labelKernel.setGeometry(QtCore.QRect(20, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelKernel.setFont(font)
        self.labelKernel.setObjectName("labelKernel")
        self.radioButtonRBF = QtWidgets.QRadioButton(self.groupBoxSVM)
        self.radioButtonRBF.setGeometry(QtCore.QRect(100, 50, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonRBF.setFont(font)
        self.radioButtonRBF.setObjectName("radioButtonRBF")
        self.radioButtonLinear = QtWidgets.QRadioButton(self.groupBoxSVM)
        self.radioButtonLinear.setGeometry(QtCore.QRect(100, 30, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButtonLinear.setFont(font)
        self.radioButtonLinear.setObjectName("radioButtonLinear")
        self.pushButtonKlasifikasi = QtWidgets.QPushButton(self.groupBoxKlasifikasiSVM)
        self.pushButtonKlasifikasi.setGeometry(QtCore.QRect(240, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKlasifikasi.setFont(font)
        self.pushButtonKlasifikasi.setObjectName("pushButtonKlasifikasi")
        self.labelRecall = QtWidgets.QLabel(self.groupBoxKlasifikasiSVM)
        self.labelRecall.setGeometry(QtCore.QRect(380, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelRecall.setFont(font)
        self.labelRecall.setObjectName("labelRecall")
        self.labelPrecision = QtWidgets.QLabel(self.groupBoxKlasifikasiSVM)
        self.labelPrecision.setGeometry(QtCore.QRect(380, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelPrecision.setFont(font)
        self.labelPrecision.setObjectName("labelPrecision")
        self.labelAkurasi = QtWidgets.QLabel(self.groupBoxKlasifikasiSVM)
        self.labelAkurasi.setGeometry(QtCore.QRect(380, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelAkurasi.setFont(font)
        self.labelAkurasi.setObjectName("labelAkurasi")
        self.lineEditRecall = QtWidgets.QLineEdit(self.groupBoxKlasifikasiSVM)
        self.lineEditRecall.setGeometry(QtCore.QRect(380, 70, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditRecall.setFont(font)
        self.lineEditRecall.setObjectName("lineEditRecall")
        self.lineEditPrecision = QtWidgets.QLineEdit(self.groupBoxKlasifikasiSVM)
        self.lineEditPrecision.setGeometry(QtCore.QRect(380, 130, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditPrecision.setFont(font)
        self.lineEditPrecision.setObjectName("lineEditPrecision")
        self.lineEditAkurasi = QtWidgets.QLineEdit(self.groupBoxKlasifikasiSVM)
        self.lineEditAkurasi.setGeometry(QtCore.QRect(380, 190, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditAkurasi.setFont(font)
        self.lineEditAkurasi.setObjectName("lineEditAkurasi")
        self.pushButtonResetKlasifikasi = QtWidgets.QPushButton(self.groupBoxKlasifikasiSVM)
        self.pushButtonResetKlasifikasi.setGeometry(QtCore.QRect(260, 210, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonResetKlasifikasi.setFont(font)
        self.pushButtonResetKlasifikasi.setObjectName("pushButtonResetKlasifikasi")
        self.pushButtonProsesCleaningLexicon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonProsesCleaningLexicon.setGeometry(QtCore.QRect(100, 390, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonProsesCleaningLexicon.setFont(font)
        self.pushButtonProsesCleaningLexicon.setObjectName("pushButtonProsesCleaningLexicon")
        self.groupBoxJudul = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxJudul.setGeometry(QtCore.QRect(10, 10, 1011, 111))
        self.groupBoxJudul.setTitle("")
        self.groupBoxJudul.setObjectName("groupBoxJudul")
        self.labelJudul2_2 = QtWidgets.QLabel(self.groupBoxJudul)
        self.labelJudul2_2.setGeometry(QtCore.QRect(270, 40, 471, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.labelJudul2_2.setFont(font)
        self.labelJudul2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelJudul2_2.setObjectName("labelJudul2_2")
        self.label_4 = QtWidgets.QLabel(self.groupBoxJudul)
        self.label_4.setGeometry(QtCore.QRect(300, 70, 411, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.labelJudul1_2 = QtWidgets.QLabel(self.groupBoxJudul)
        self.labelJudul1_2.setGeometry(QtCore.QRect(170, 10, 700, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        self.labelJudul1_2.setFont(font)
        self.labelJudul1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelJudul1_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelJudul1_2.setScaledContents(False)
        self.labelJudul1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelJudul1_2.setObjectName("labelJudul1_2")
        self.groupBoxSentimen = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSentimen.setGeometry(QtCore.QRect(440, 140, 401, 80))
        self.groupBoxSentimen.setObjectName("groupBoxSentimen")
        self.pushButtonSentimen = QtWidgets.QPushButton(self.groupBoxSentimen)
        self.pushButtonSentimen.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSentimen.setFont(font)
        self.pushButtonSentimen.setObjectName("pushButtonSentimen")
        self.labelPositif = QtWidgets.QLabel(self.groupBoxSentimen)
        self.labelPositif.setGeometry(QtCore.QRect(180, 10, 61, 16))
        self.labelPositif.setObjectName("labelPositif")
        self.labelNegatif = QtWidgets.QLabel(self.groupBoxSentimen)
        self.labelNegatif.setGeometry(QtCore.QRect(280, 10, 61, 16))
        self.labelNegatif.setObjectName("labelNegatif")
        self.lineEditSentimenPositif = QtWidgets.QLineEdit(self.groupBoxSentimen)
        self.lineEditSentimenPositif.setGeometry(QtCore.QRect(190, 30, 41, 31))
        self.lineEditSentimenPositif.setObjectName("lineEditSentimenPositif")
        self.lineEditSentimenNegatif = QtWidgets.QLineEdit(self.groupBoxSentimen)
        self.lineEditSentimenNegatif.setGeometry(QtCore.QRect(290, 30, 41, 31))
        self.lineEditSentimenNegatif.setObjectName("lineEditSentimenNegatif")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # tombol-showBrowse(dataMentah)
        self.tombolBrowse.clicked.connect(self.browseKlik)
        self.showPath.returnPressed.connect(self.browseKlik) 
        
        # tombol-showcleaning
        self.pushButtonProsesCleaningLexicon.clicked.connect(self.CleaningLexiconKlik)
        
        # tombol Sentimen
        self.pushButtonSentimen.clicked.connect(self.SentimenKlik)
        
        # radio button
        self.pushButtonKlasifikasi.clicked.connect(self.klasifikasi)
        
        # tombol reset data klasifikasi
        self.pushButtonResetKlasifikasi.clicked.connect(self.ClearDataKlasifikasi)
            
        # tombolProsesDataTunggal
        self.pushButtonProsesDataTunggal.clicked.connect(self.DataTunggal)
        
        # tombol reset data tunggal
        self.pushButtonResetDataTunggal.clicked.connect(self.ClearDataTunggal)
       
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analisis Sentimen SVM"))
        self.tombolBrowse.setText(_translate("MainWindow", "Browse"))
        self.labelDataMentah.setText(_translate("MainWindow", "Data Mentah"))
        self.labelDataCleaningLexicon.setText(_translate("MainWindow", "Data Cleaning - Lexicon"))
        self.groupBoxUjiDataTunggal.setTitle(_translate("MainWindow", "Uji Data Tunggal"))
        self.labelMasukanDataTunggal.setText(_translate("MainWindow", "Masukkan Data :"))
        self.labelHasilLexicon.setText(_translate("MainWindow", "Hasil Lexicon :"))
        self.pushButtonProsesDataTunggal.setText(_translate("MainWindow", "Proses"))
        self.pushButtonResetDataTunggal.setText(_translate("MainWindow", "Reset"))
        self.groupBoxKlasifikasiSVM.setTitle(_translate("MainWindow", "Klasifikasi SVM"))
        self.groupBoxKFold.setTitle(_translate("MainWindow", "K-FOLD"))
        self.radioButtonK3.setText(_translate("MainWindow", "3"))
        self.radioButtonK10.setText(_translate("MainWindow", "10"))
        self.labelK.setText(_translate("MainWindow", "K = "))
        self.radioButtonK5.setText(_translate("MainWindow", "5"))
        self.groupBoxSVM.setTitle(_translate("MainWindow", "Support Vector Machine"))
        self.radioButtonPoly.setText(_translate("MainWindow", "Polynomial"))
        self.labelKernel.setText(_translate("MainWindow", "KERNEL = "))
        self.radioButtonRBF.setText(_translate("MainWindow", "RBF"))
        self.radioButtonLinear.setText(_translate("MainWindow", "Linear"))
        self.pushButtonKlasifikasi.setText(_translate("MainWindow", "Klasifikasi"))
        self.labelRecall.setText(_translate("MainWindow", "Recall"))
        self.labelPrecision.setText(_translate("MainWindow", "Precision"))
        self.labelAkurasi.setText(_translate("MainWindow", "Akurasi"))
        self.pushButtonResetKlasifikasi.setText(_translate("MainWindow", "Reset"))
        self.pushButtonProsesCleaningLexicon.setText(_translate("MainWindow", "Proses Cleaning - Lexicon"))
        self.labelJudul2_2.setText(_translate("MainWindow", "BERDASARKAN MEDIA SOSIAL TWITTER "))
        self.label_4.setText(_translate("MainWindow", "SUPPORT VECTOR MACHINE (SVM)"))
        self.labelJudul1_2.setText(_translate("MainWindow", "ANALISIS SENTIMEN TERHADAP PEMBELAJARAN DARING "))
        self.groupBoxSentimen.setTitle(_translate("MainWindow", "Jumlah Sentimen"))
        self.pushButtonSentimen.setText(_translate("MainWindow", "Sentimen"))
        self.labelPositif.setText(_translate("MainWindow", "POSITIF"))
        self.labelNegatif.setText(_translate("MainWindow", "NEGATIF"))

    
    def browseKlik(self):
        filename,_ = QtWidgets.QFileDialog.getOpenFileName()
        self.df = pd.read_csv(filename)
        datasetMentah = PandasModel(self.df)
        self.tableViewDataMentah.setModel(datasetMentah)
        self.showPath.setText(filename)
        
    def CleaningLexiconKlik(self):
        self.hasilLexicon = pd.read_excel('HasilVaderMaretJuniId.xlsx')
        data = self.hasilLexicon[['Tweet', 'label']]
        cleaning = PandasModel(data)
        self.tableViewCleaningLexicon.setModel(cleaning)
        
    def SentimenKlik(self):
        # hitungPolaritasself.dfFrame
        self.positif = self.hasilLexicon[self.hasilLexicon['label']==1]['label'].count()
        self.negatif = self.hasilLexicon[self.hasilLexicon['label']==-1]['label'].count()    

        self.pos = str(self.positif)
        self.neg = str(self.negatif)        
        self.lineEditSentimenPositif.setText(self.pos)
        self.lineEditSentimenNegatif.setText(self.neg)

    def klasifikasi(self):
        self.k = 0
        self.krl=''
        if self.radioButtonK3.isChecked() and self.radioButtonLinear.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.LinearSVM(3, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK3.isChecked() and self.radioButtonRBF.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.RbfSVM(3, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK3.isChecked() and self.radioButtonPoly.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.PolySVM(3, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK5.isChecked() and self.radioButtonLinear.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.LinearSVM(5, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK5.isChecked() and self.radioButtonRBF.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.RbfSVM(5, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK5.isChecked() and self.radioButtonPoly.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.PolySVM(5, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK10.isChecked() and self.radioButtonLinear.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.LinearSVM(10, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK10.isChecked() and self.radioButtonRBF.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.RbfSVM(10, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
        elif self.radioButtonK10.isChecked() and self.radioButtonPoly.isChecked():
            X = self.hasilLexicon['Tweet']
            y = self.hasilLexicon['label']
            svm = clsvm.PolySVM(10, X, y)
            akurasi = svm[0]*100
            recall = svm[1]*100
            precision = svm[2]*100
            
        self.akurasi = str(akurasi)
        self.recall = str(recall)
        self.precision = str(precision)
        self.lineEditRecall.setText(self.recall)
        self.lineEditPrecision.setText(self.precision)
        self.lineEditAkurasi.setText(self.akurasi)


    def DataTunggal(self):
        self.data = self.lineEditDataTunggal.text()
        
        # self.data = {'Text':[self.inputData]}
        # self.data = pd.DataFrame(self.data)

        self.data = pd.Series(self.data)

        self.dataTunggal = clsvm.clSVMTunggal(self.data)
        self.dataTunggal = pd.DataFrame(self.dataTunggal, columns=['label'])

        # polaritasDataTunggal
        self.dataTunggal['label2'] = self.dataTunggal['label'].apply(lambda c: 'POSITIF' if c >0 else 'NEGATIF')
        
        
        self.sentimen = self.dataTunggal['label2']
        self.sentimen = self.sentimen.to_string(index=False)
        self.lineEditHasilLexicon.setText(self.sentimen)
        
    def ClearDataTunggal(self):
        self.lineEditDataTunggal.clear()
        self.lineEditHasilLexicon.clear()
    
    def ClearDataKlasifikasi(self):
        self.lineEditRecall.clear()
        self.lineEditPrecision.clear()
        self.lineEditAkurasi.clear()
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
