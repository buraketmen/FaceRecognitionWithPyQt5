# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonelEkle.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(783, 481)
        Dialog.setMinimumSize(QtCore.QSize(783, 481))
        Dialog.setMaximumSize(QtCore.QSize(783, 481))
        self.buttonPersonelEkle = QtWidgets.QPushButton(Dialog)
        self.buttonPersonelEkle.setGeometry(QtCore.QRect(500, 410, 261, 51))
        self.buttonPersonelEkle.setMinimumSize(QtCore.QSize(261, 51))
        self.buttonPersonelEkle.setMaximumSize(QtCore.QSize(261, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.buttonPersonelEkle.setFont(font)
        self.buttonPersonelEkle.setObjectName("buttonPersonelEkle")
        self.labelPersonelEkle = QtWidgets.QLabel(Dialog)
        self.labelPersonelEkle.setGeometry(QtCore.QRect(320, 10, 141, 31))
        self.labelPersonelEkle.setMinimumSize(QtCore.QSize(141, 31))
        self.labelPersonelEkle.setMaximumSize(QtCore.QSize(141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelPersonelEkle.setFont(font)
        self.labelPersonelEkle.setObjectName("labelPersonelEkle")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(17, 19, 291, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(470, 20, 291, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(373, 50, 21, 411))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 341, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelFotograf = QtWidgets.QLabel(self.layoutWidget)
        self.labelFotograf.setMinimumSize(QtCore.QSize(339, 343))
        self.labelFotograf.setMaximumSize(QtCore.QSize(339, 343))
        self.labelFotograf.setAutoFillBackground(False)
        self.labelFotograf.setStyleSheet("")
        self.labelFotograf.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.labelFotograf.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelFotograf.setText("")
        self.labelFotograf.setObjectName("labelFotograf")
        self.verticalLayout.addWidget(self.labelFotograf)
        self.buttonFotografYukle = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonFotografYukle.setMinimumSize(QtCore.QSize(339, 40))
        self.buttonFotografYukle.setMaximumSize(QtCore.QSize(339, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonFotografYukle.setFont(font)
        self.buttonFotografYukle.setObjectName("buttonFotografYukle")
        self.verticalLayout.addWidget(self.buttonFotografYukle)
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(411, 61, 81, 241))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.labelTcNo = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTcNo.setFont(font)
        self.labelTcNo.setObjectName("labelTcNo")
        self.labelAd = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelAd.setFont(font)
        self.labelAd.setObjectName("labelAd")
        self.labelSoyad = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelSoyad.setFont(font)
        self.labelSoyad.setObjectName("labelSoyad")
        self.labelYas = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelYas.setFont(font)
        self.labelYas.setObjectName("labelYas")
        self.labelPozisyon = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelPozisyon.setFont(font)
        self.labelPozisyon.setObjectName("labelPozisyon")
        self.labelTelefonNo = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTelefonNo.setFont(font)
        self.labelTelefonNo.setObjectName("labelTelefonNo")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(500, 60, 261, 241))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.editTcNo = QtWidgets.QLineEdit(self.splitter)
        self.editTcNo.setMinimumSize(QtCore.QSize(261, 36))
        self.editTcNo.setMaximumSize(QtCore.QSize(261, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editTcNo.setFont(font)
        self.editTcNo.setText("")
        self.editTcNo.setClearButtonEnabled(True)
        self.editTcNo.setObjectName("editTcNo")
        self.editAd = QtWidgets.QLineEdit(self.splitter)
        self.editAd.setMinimumSize(QtCore.QSize(261, 36))
        self.editAd.setMaximumSize(QtCore.QSize(261, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editAd.setFont(font)
        self.editAd.setText("")
        self.editAd.setClearButtonEnabled(True)
        self.editAd.setObjectName("editAd")
        self.editSoyad = QtWidgets.QLineEdit(self.splitter)
        self.editSoyad.setMinimumSize(QtCore.QSize(261, 36))
        self.editSoyad.setMaximumSize(QtCore.QSize(261, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editSoyad.setFont(font)
        self.editSoyad.setClearButtonEnabled(True)
        self.editSoyad.setObjectName("editSoyad")
        self.editYas = QtWidgets.QLineEdit(self.splitter)
        self.editYas.setMinimumSize(QtCore.QSize(261, 36))
        self.editYas.setMaximumSize(QtCore.QSize(261, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editYas.setFont(font)
        self.editYas.setText("")
        self.editYas.setClearButtonEnabled(True)
        self.editYas.setObjectName("editYas")
        self.editPozisyon = QtWidgets.QLineEdit(self.splitter)
        self.editPozisyon.setMinimumSize(QtCore.QSize(261, 36))
        self.editPozisyon.setMaximumSize(QtCore.QSize(261, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editPozisyon.setFont(font)
        self.editPozisyon.setText("")
        self.editPozisyon.setClearButtonEnabled(True)
        self.editPozisyon.setObjectName("editPozisyon")
        self.editTelefonNo = QtWidgets.QLineEdit(self.splitter)
        self.editTelefonNo.setMinimumSize(QtCore.QSize(261, 36))
        self.editTelefonNo.setMaximumSize(QtCore.QSize(261, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editTelefonNo.setFont(font)
        self.editTelefonNo.setText("")
        self.editTelefonNo.setClearButtonEnabled(True)
        self.editTelefonNo.setObjectName("editTelefonNo")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 450, 371, 16))
        self.label.setObjectName("label")
        self.editAciklama = QtWidgets.QLineEdit(Dialog)
        self.editAciklama.setGeometry(QtCore.QRect(500, 360, 261, 41))
        self.editAciklama.setMinimumSize(QtCore.QSize(261, 41))
        self.editAciklama.setMaximumSize(QtCore.QSize(261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editAciklama.setFont(font)
        self.editAciklama.setText("")
        self.editAciklama.setClearButtonEnabled(True)
        self.editAciklama.setObjectName("editAciklama")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(530, 310, 231, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonGunduz = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButtonGunduz.setMinimumSize(QtCore.QSize(115, 22))
        self.radioButtonGunduz.setMaximumSize(QtCore.QSize(115, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonGunduz.setFont(font)
        self.radioButtonGunduz.setObjectName("radioButtonGunduz")
        self.horizontalLayout.addWidget(self.radioButtonGunduz)
        self.radioButtonGece = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioButtonGece.setMinimumSize(QtCore.QSize(114, 22))
        self.radioButtonGece.setMaximumSize(QtCore.QSize(114, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonGece.setFont(font)
        self.radioButtonGece.setObjectName("radioButtonGece")
        self.horizontalLayout.addWidget(self.radioButtonGece)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(410, 310, 91, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelMesaiTipi = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelMesaiTipi.setFont(font)
        self.labelMesaiTipi.setObjectName("labelMesaiTipi")
        self.verticalLayout_2.addWidget(self.labelMesaiTipi)
        self.labelAciklama = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelAciklama.setFont(font)
        self.labelAciklama.setObjectName("labelAciklama")
        self.verticalLayout_2.addWidget(self.labelAciklama)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.buttonPersonelEkle.setText(_translate("Dialog", "PERSONELİ EKLE"))
        self.labelPersonelEkle.setText(_translate("Dialog", "PERSONEL EKLE"))
        self.buttonFotografYukle.setText(_translate("Dialog", "Fotoğraf Yükle"))
        self.labelTcNo.setText(_translate("Dialog", "T.C. No"))
        self.labelAd.setText(_translate("Dialog", "Ad"))
        self.labelSoyad.setText(_translate("Dialog", "Soyad"))
        self.labelYas.setText(_translate("Dialog", "Yaş"))
        self.labelPozisyon.setText(_translate("Dialog", "Pozisyon"))
        self.labelTelefonNo.setText(_translate("Dialog", "Telefon No"))
        self.label.setText(_translate("Dialog", "*Fotograf uzerinden yuz tanima ve kirpma gerceklesecegi icin uzun surebilir."))
        self.radioButtonGunduz.setText(_translate("Dialog", "Gündüz"))
        self.radioButtonGece.setText(_translate("Dialog", "Gece"))
        self.labelMesaiTipi.setText(_translate("Dialog", "Mesai Tipi"))
        self.labelAciklama.setText(_translate("Dialog", "Açıklama"))


