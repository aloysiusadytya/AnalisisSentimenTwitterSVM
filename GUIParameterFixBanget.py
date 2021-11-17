# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIParameterFixBanget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

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
        self.groupBoxUjiDataTunggal.setGeometry(QtCore.QRect(420, 520, 601, 151))
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
        self.lineEditDataTuggal = QtWidgets.QLineEdit(self.groupBoxUjiDataTunggal)
        self.lineEditDataTuggal.setGeometry(QtCore.QRect(160, 30, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditDataTuggal.setFont(font)
        self.lineEditDataTuggal.setObjectName("lineEditDataTuggal")
        self.labelHasilLexicon = QtWidgets.QLabel(self.groupBoxUjiDataTunggal)
        self.labelHasilLexicon.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelHasilLexicon.setFont(font)
        self.labelHasilLexicon.setObjectName("labelHasilLexicon")
        self.pushButtonProsesDataTunggal = QtWidgets.QPushButton(self.groupBoxUjiDataTunggal)
        self.pushButtonProsesDataTunggal.setGeometry(QtCore.QRect(490, 60, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonProsesDataTunggal.setFont(font)
        self.pushButtonProsesDataTunggal.setObjectName("pushButtonProsesDataTunggal")
        self.lineEditHasilLexicon = QtWidgets.QLineEdit(self.groupBoxUjiDataTunggal)
        self.lineEditHasilLexicon.setGeometry(QtCore.QRect(160, 90, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditHasilLexicon.setFont(font)
        self.lineEditHasilLexicon.setObjectName("lineEditHasilLexicon")
        self.pushButtonResetDataTunggal = QtWidgets.QPushButton(self.groupBoxUjiDataTunggal)
        self.pushButtonResetDataTunggal.setGeometry(QtCore.QRect(490, 120, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonResetDataTunggal.setFont(font)
        self.pushButtonResetDataTunggal.setObjectName("pushButtonResetDataTunggal")
        self.groupBoxKlasifikasiSVM = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxKlasifikasiSVM.setGeometry(QtCore.QRect(420, 250, 601, 261))
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
        self.radioButtonPoly.setGeometry(QtCore.QRect(100, 70, 91, 21))
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
        self.pushButtonKlasifikasi.setGeometry(QtCore.QRect(270, 190, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonKlasifikasi.setFont(font)
        self.pushButtonKlasifikasi.setObjectName("pushButtonKlasifikasi")
        self.labelRecall = QtWidgets.QLabel(self.groupBoxKlasifikasiSVM)
        self.labelRecall.setGeometry(QtCore.QRect(470, 40, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelRecall.setFont(font)
        self.labelRecall.setObjectName("labelRecall")
        self.labelPrecision = QtWidgets.QLabel(self.groupBoxKlasifikasiSVM)
        self.labelPrecision.setGeometry(QtCore.QRect(460, 100, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelPrecision.setFont(font)
        self.labelPrecision.setObjectName("labelPrecision")
        self.labelAkurasi = QtWidgets.QLabel(self.groupBoxKlasifikasiSVM)
        self.labelAkurasi.setGeometry(QtCore.QRect(470, 160, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelAkurasi.setFont(font)
        self.labelAkurasi.setObjectName("labelAkurasi")
        self.lineEditRecall = QtWidgets.QLineEdit(self.groupBoxKlasifikasiSVM)
        self.lineEditRecall.setGeometry(QtCore.QRect(410, 60, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditRecall.setFont(font)
        self.lineEditRecall.setObjectName("lineEditRecall")
        self.lineEditPrecision = QtWidgets.QLineEdit(self.groupBoxKlasifikasiSVM)
        self.lineEditPrecision.setGeometry(QtCore.QRect(410, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditPrecision.setFont(font)
        self.lineEditPrecision.setObjectName("lineEditPrecision")
        self.lineEditAkurasi = QtWidgets.QLineEdit(self.groupBoxKlasifikasiSVM)
        self.lineEditAkurasi.setGeometry(QtCore.QRect(410, 180, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditAkurasi.setFont(font)
        self.lineEditAkurasi.setObjectName("lineEditAkurasi")
        self.pushButtonResetKlasifikasi = QtWidgets.QPushButton(self.groupBoxKlasifikasiSVM)
        self.pushButtonResetKlasifikasi.setGeometry(QtCore.QRect(470, 220, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonResetKlasifikasi.setFont(font)
        self.pushButtonResetKlasifikasi.setObjectName("pushButtonResetKlasifikasi")
        self.groupBox = QtWidgets.QGroupBox(self.groupBoxKlasifikasiSVM)
        self.groupBox.setGeometry(QtCore.QRect(230, 20, 171, 141))
        self.groupBox.setObjectName("groupBox")
        self.comboBoxC = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxC.setGeometry(QtCore.QRect(90, 30, 69, 22))
        self.comboBoxC.setObjectName("comboBoxC")
        self.comboBoxC.addItem("")
        self.comboBoxC.setItemText(0, "")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.comboBoxC.addItem("")
        self.labelC = QtWidgets.QLabel(self.groupBox)
        self.labelC.setGeometry(QtCore.QRect(10, 30, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelC.setFont(font)
        self.labelC.setObjectName("labelC")
        self.labelGamma = QtWidgets.QLabel(self.groupBox)
        self.labelGamma.setGeometry(QtCore.QRect(10, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelGamma.setFont(font)
        self.labelGamma.setObjectName("labelGamma")
        self.labelKDegree = QtWidgets.QLabel(self.groupBox)
        self.labelKDegree.setGeometry(QtCore.QRect(10, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelKDegree.setFont(font)
        self.labelKDegree.setObjectName("labelKDegree")
        self.comboBoxGamma = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxGamma.setGeometry(QtCore.QRect(90, 70, 69, 22))
        self.comboBoxGamma.setObjectName("comboBoxGamma")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.setItemText(0, "")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBoxGamma.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 110, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.groupBoxSentimen.setGeometry(QtCore.QRect(420, 140, 281, 80))
        self.groupBoxSentimen.setObjectName("groupBoxSentimen")
        self.pushButtonSentimen = QtWidgets.QPushButton(self.groupBoxSentimen)
        self.pushButtonSentimen.setGeometry(QtCore.QRect(20, 30, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSentimen.setFont(font)
        self.pushButtonSentimen.setObjectName("pushButtonSentimen")
        self.labelPositif = QtWidgets.QLabel(self.groupBoxSentimen)
        self.labelPositif.setGeometry(QtCore.QRect(140, 10, 61, 16))
        self.labelPositif.setObjectName("labelPositif")
        self.labelNegatif = QtWidgets.QLabel(self.groupBoxSentimen)
        self.labelNegatif.setGeometry(QtCore.QRect(210, 10, 61, 16))
        self.labelNegatif.setObjectName("labelNegatif")
        self.lineEditSentimenPositif = QtWidgets.QLineEdit(self.groupBoxSentimen)
        self.lineEditSentimenPositif.setGeometry(QtCore.QRect(150, 30, 41, 31))
        self.lineEditSentimenPositif.setObjectName("lineEditSentimenPositif")
        self.lineEditSentimenNegatif = QtWidgets.QLineEdit(self.groupBoxSentimen)
        self.lineEditSentimenNegatif.setGeometry(QtCore.QRect(220, 30, 41, 31))
        self.lineEditSentimenNegatif.setObjectName("lineEditSentimenNegatif")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(730, 140, 291, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(70, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        self.labelHasilLexicon.setText(_translate("MainWindow", "Hasil :"))
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
        self.groupBox.setTitle(_translate("MainWindow", "PARAMETER"))
        self.comboBoxC.setItemText(1, _translate("MainWindow", "0.1"))
        self.comboBoxC.setItemText(2, _translate("MainWindow", "0.5"))
        self.comboBoxC.setItemText(3, _translate("MainWindow", "1"))
        self.comboBoxC.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxC.setItemText(5, _translate("MainWindow", "10"))
        self.comboBoxC.setItemText(6, _translate("MainWindow", "15"))
        self.comboBoxC.setItemText(7, _translate("MainWindow", "20"))
        self.comboBoxC.setItemText(8, _translate("MainWindow", "25"))
        self.comboBoxC.setItemText(9, _translate("MainWindow", "30"))
        self.comboBoxC.setItemText(10, _translate("MainWindow", "35"))
        self.comboBoxC.setItemText(11, _translate("MainWindow", "40"))
        self.comboBoxC.setItemText(12, _translate("MainWindow", "45"))
        

        
        self.labelC.setText(_translate("MainWindow", "C = "))
        self.labelGamma.setText(_translate("MainWindow", "Gamma = "))
        self.labelKDegree.setText(_translate("MainWindow", "Degree = "))
        self.comboBoxGamma.setItemText(1, _translate("MainWindow", "0.01"))
        self.comboBoxGamma.setItemText(2, _translate("MainWindow", "0.1"))
        self.comboBoxGamma.setItemText(3, _translate("MainWindow", "1"))
        self.comboBoxGamma.setItemText(4, _translate("MainWindow", "2"))
        self.comboBoxGamma.setItemText(5, _translate("MainWindow", "3"))
        self.comboBoxGamma.setItemText(6, _translate("MainWindow", "4"))
        self.comboBoxGamma.setItemText(7, _translate("MainWindow", "5"))
        self.comboBoxGamma.setItemText(8, _translate("MainWindow", "6"))
        self.comboBoxGamma.setItemText(9, _translate("MainWindow", "7"))
        self.comboBoxGamma.setItemText(10, _translate("MainWindow", "8"))
        self.comboBoxGamma.setItemText(11, _translate("MainWindow", "9"))
        self.comboBoxGamma.setItemText(12, _translate("MainWindow", "10"))
        self.comboBoxGamma.setItemText(13, _translate("MainWindow", "11"))
        self.comboBoxGamma.setItemText(14, _translate("MainWindow", "12"))
        self.comboBoxGamma.setItemText(15, _translate("MainWindow", "13"))
        self.comboBoxGamma.setItemText(16, _translate("MainWindow", "14"))
        self.comboBoxGamma.setItemText(17, _translate("MainWindow", "scale"))
        self.comboBox.setItemText(1, _translate("MainWindow", "0.001"))
        self.comboBox.setItemText(2, _translate("MainWindow", "0.01"))
        self.comboBox.setItemText(3, _translate("MainWindow", "0.1"))
        self.comboBox.setItemText(4, _translate("MainWindow", "1"))
        self.comboBox.setItemText(5, _translate("MainWindow", "2"))
        self.comboBox.setItemText(6, _translate("MainWindow", "3"))
        self.comboBox.setItemText(7, _translate("MainWindow", "4"))
        self.comboBox.setItemText(8, _translate("MainWindow", "5"))
        self.comboBox.setItemText(9, _translate("MainWindow", "6"))
        self.comboBox.setItemText(10, _translate("MainWindow", "7"))
        self.pushButtonProsesCleaningLexicon.setText(_translate("MainWindow", "Proses Cleaning - Lexicon"))
        self.labelJudul2_2.setText(_translate("MainWindow", "BERDASARKAN MEDIA SOSIAL TWITTER "))
        self.label_4.setText(_translate("MainWindow", "SUPPORT VECTOR MACHINE (SVM)"))
        self.labelJudul1_2.setText(_translate("MainWindow", "ANALISIS SENTIMEN TERHADAP PEMBELAJARAN DARING "))
        self.groupBoxSentimen.setTitle(_translate("MainWindow", "Jumlah Sentimen"))
        self.pushButtonSentimen.setText(_translate("MainWindow", "Sentimen"))
        self.labelPositif.setText(_translate("MainWindow", "POSITIF"))
        self.labelNegatif.setText(_translate("MainWindow", "NEGATIF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "KETERANGAN KLASIFIKASI"))
        self.label_2.setText(_translate("MainWindow", "Parameter Kenel RBF =  C dan Gamma."))
        self.label_3.setText(_translate("MainWindow", "Parameter Kenel Polynomial = C, Gamma, Degree"))
        self.label.setText(_translate("MainWindow", "Parameter Kernel Linear = C"))


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
            self.index = self.comboBoxC.currentIndex()
            if self.index == 1:
                c = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 2:
                c = 0.5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 3:
                c = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 4:
                c = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            elif self.index == 5:
                c = 10
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 6:
                c = 15
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            elif self.index == 7:
                c = 20
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 8:
                c = 25
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 9:
                c = 30
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 10:
                c = 35
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 11:
                c = 40
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 12:
                c = 45
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(3, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
        elif self.radioButtonK3.isChecked() and self.radioButtonRBF.isChecked():
            self.index = self.comboBoxGamma.currentIndex()
            if self.index == 1:
                c = 5
                g = 0.01
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 2:
                c = 5
                g = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 3:
                c = 5
                g = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 4:
                c = 5
                g = 2
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 5:
                c = 5
                g = 3
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 6:
                c = 5
                g = 4
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 7:
                c = 5
                g = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 8:
                c = 5
                g = 6
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 9:
                c = 5
                g = 7
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 10:
                c = 5
                g = 8
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 11:
                c = 5
                g = 9
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 12:
                c = 5
                g = 10
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 13:
                c = 5
                g = 11
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 14:
                c = 5
                g = 12
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 15:
                c = 5
                g = 13
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 16:
                c = 5
                g = 14
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 17:
                c = 5
                g = 'scale'
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(3, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
                
        elif self.radioButtonK3.isChecked() and self.radioButtonPoly.isChecked():
            self.index = self.comboBox.currentIndex()
            if self.index == 1:
                c = 35
                g = 'scale'
                d = 0.001
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 2:
                c = 35
                g = 'scale'
                d = 0.01
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 3:
                c = 35
                g = 'scale'
                d = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 4:
                c = 35
                g = 'scale'
                d = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 5:
                c = 35
                g = 'scale'
                d = 2
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 6:
                c = 35
                g = 'scale'
                d = 3
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 7:
                c = 35
                g = 'scale'
                d = 4
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 8:
                c = 35
                g = 'scale'
                d = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 9:
                c = 35
                g = 'scale'
                d = 6
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 10:
                c = 35
                g = 'scale'
                d = 7
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(3, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            
        elif self.radioButtonK5.isChecked() and self.radioButtonLinear.isChecked():
            self.index = self.comboBoxC.currentIndex()
            if self.index == 1:
                c = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 2:
                c = 0.5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 3:
                c = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 4:
                c = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            elif self.index == 5:
                c = 10
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 6:
                c = 15
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            elif self.index == 7:
                c = 20
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 8:
                c = 25
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 9:
                c = 30
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 10:
                c = 35
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 11:
                c = 40
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 12:
                c = 45
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(5, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
        elif self.radioButtonK5.isChecked() and self.radioButtonRBF.isChecked():
            self.index = self.comboBoxGamma.currentIndex()
            if self.index == 1:
                c = 5
                g = 0.01
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 2:
                c = 5
                g = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 3:
                c = 5
                g = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 4:
                c = 5
                g = 2
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 5:
                c = 5
                g = 3
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 6:
                c = 5
                g = 4
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 7:
                c = 5
                g = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 8:
                c = 5
                g = 6
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 9:
                c = 5
                g = 7
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 10:
                c = 5
                g = 8
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 11:
                c = 5
                g = 9
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 12:
                c = 5
                g = 10
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 13:
                c = 5
                g = 11
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 14:
                c = 5
                g = 12
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 15:
                c = 5
                g = 13
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 16:
                c = 5
                g = 14
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 17:
                c = 5
                g = 'scale'
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
        elif self.radioButtonK5.isChecked() and self.radioButtonPoly.isChecked():
            self.index = self.comboBox.currentIndex()
            if self.index == 1:
                c = 35
                g = 'scale'
                d = 0.001
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 2:
                c = 35
                g = 'scale'
                d = 0.01
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 3:
                c = 35
                g = 'scale'
                d = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 4:
                c = 35
                g = 'scale'
                d = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 5:
                c = 35
                g = 'scale'
                d = 2
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 6:
                c = 35
                g = 'scale'
                d = 3
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 7:
                c = 35
                g = 'scale'
                d = 4
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 8:
                c = 35
                g = 'scale'
                d = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 9:
                c = 35
                g = 'scale'
                d = 6
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 10:
                c = 35
                g = 'scale'
                d = 7
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(5, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
        elif self.radioButtonK10.isChecked() and self.radioButtonLinear.isChecked():
            self.index = self.comboBoxC.currentIndex()
            if self.index == 1:
                c = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 2:
                c = 0.5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 3:
                c = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 4:
                c = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            elif self.index == 5:
                c = 10
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 6:
                c = 15
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            
            elif self.index == 7:
                c = 20
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 8:
                c = 25
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 9:
                c = 30
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 10:
                c = 35
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 11:
                c = 40
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
            elif self.index == 12:
                c = 45
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.LinearSVM(10, X, y, c)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
        elif self.radioButtonK10.isChecked() and self.radioButtonRBF.isChecked():
            self.index = self.comboBoxGamma.currentIndex()
            if self.index == 1:
                c = 5
                g = 0.01
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 2:
                c = 5
                g = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 3:
                c = 5
                g = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 4:
                c = 5
                g = 2
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 5:
                c = 5
                g = 3
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 6:
                c = 5
                g = 4
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(5, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 7:
                c = 5
                g = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 8:
                c = 5
                g = 6
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 9:
                c = 5
                g = 7
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 10:
                c = 5
                g = 8
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 11:
                c = 5
                g = 9
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 12:
                c = 5
                g = 10
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 13:
                c = 5
                g = 11
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 14:
                c = 5
                g = 12
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 15:
                c = 5
                g = 13
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 16:
                c = 5
                g = 14
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 17:
                c = 5
                g = 'scale'
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.RbfSVM(10, X, y, c, g)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
                
        elif self.radioButtonK10.isChecked() and self.radioButtonPoly.isChecked():
            self.index = self.comboBox.currentIndex()
            if self.index == 1:
                c = 35
                g = 'scale'
                d = 0.001
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 2:
                c = 35
                g = 'scale'
                d = 0.01
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 3:
                c = 35
                g = 'scale'
                d = 0.1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 4:
                c = 35
                g = 'scale'
                d = 1
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 5:
                c = 35
                g = 'scale'
                d = 2
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 6:
                c = 35
                g = 'scale'
                d = 3
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 7:
                c = 35
                g = 'scale'
                d = 4
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 8:
                c = 35
                g = 'scale'
                d = 5
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 9:
                c = 35
                g = 'scale'
                d = 6
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
                akurasi = svm[0]*100
                recall = svm[1]*100
                precision = svm[2]*100
            elif self.index == 10:
                c = 35
                g = 'scale'
                d = 7
                X = self.hasilLexicon['Tweet']
                y = self.hasilLexicon['label']
                svm = clsvm.PolySVM(10, X, y, c, g, d)
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
        self.data = self.lineEditDataTuggal.text()
        
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
        self.lineEditDataTuggal.clear()
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

