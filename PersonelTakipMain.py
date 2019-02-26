# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PersonelTakipMain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 605)
        MainWindow.setMinimumSize(QtCore.QSize(1313, 605))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(0, 30))
        self.startButton.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color:rgb(197, 208, 255)")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 30))
        self.stopButton.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("background-color:rgb(197, 208, 255)")
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.detectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detectButton.sizePolicy().hasHeightForWidth())
        self.detectButton.setSizePolicy(sizePolicy)
        self.detectButton.setMinimumSize(QtCore.QSize(0, 30))
        self.detectButton.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.detectButton.setFont(font)
        self.detectButton.setStyleSheet("background-color:rgb(197, 208, 255)")
        self.detectButton.setObjectName("detectButton")
        self.horizontalLayout.addWidget(self.detectButton)
        self.trainButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.trainButton.setFont(font)
        self.trainButton.setStyleSheet("background-color:rgb(197, 208, 255)")
        self.trainButton.setObjectName("trainButton")
        self.horizontalLayout.addWidget(self.trainButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.imgLabel.setMaximumSize(QtCore.QSize(640, 480))
        self.imgLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imgLabel.setAutoFillBackground(False)
        self.imgLabel.setStyleSheet("\n"
"background-color: rgb(0, 0, 0)\n"
"")
        self.imgLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imgLabel.setLineWidth(1)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.gridLayout.addWidget(self.imgLabel, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(640, 480))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 638, 497))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1313, 21))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuExceleAktar = QtWidgets.QMenu(self.menuDosya)
        self.menuExceleAktar.setObjectName("menuExceleAktar")
        self.menuPersonel = QtWidgets.QMenu(self.menubar)
        self.menuPersonel.setObjectName("menuPersonel")
        self.menuHakkinda = QtWidgets.QMenu(self.menubar)
        self.menuHakkinda.setObjectName("menuHakkinda")
        MainWindow.setMenuBar(self.menubar)
        self.actionDiskten_Ekle = QtWidgets.QAction(MainWindow)
        self.actionDiskten_Ekle.setObjectName("actionDiskten_Ekle")
        self.actionProgramHakkinda = QtWidgets.QAction(MainWindow)
        self.actionProgramHakkinda.setObjectName("actionProgramHakkinda")
        self.actionGelistiriciHakkinda = QtWidgets.QAction(MainWindow)
        self.actionGelistiriciHakkinda.setObjectName("actionGelistiriciHakkinda")
        self.actionPersonelEkle = QtWidgets.QAction(MainWindow)
        self.actionPersonelEkle.setObjectName("actionPersonelEkle")
        self.actionPersoneller = QtWidgets.QAction(MainWindow)
        self.actionPersoneller.setObjectName("actionPersoneller")
        self.actionLoglar = QtWidgets.QAction(MainWindow)
        self.actionLoglar.setObjectName("actionLoglar")
        self.actionKamera1 = QtWidgets.QAction(MainWindow)
        self.actionKamera1.setCheckable(True)
        self.actionKamera1.setObjectName("actionKamera1")
        self.actionKamera2 = QtWidgets.QAction(MainWindow)
        self.actionKamera2.setCheckable(True)
        self.actionKamera2.setObjectName("actionKamera2")
        self.actionKamera3 = QtWidgets.QAction(MainWindow)
        self.actionKamera3.setCheckable(True)
        self.actionKamera3.setObjectName("actionKamera3")
        self.actionKamera4 = QtWidgets.QAction(MainWindow)
        self.actionKamera4.setCheckable(True)
        self.actionKamera4.setObjectName("actionKamera4")
        self.actionKamera5 = QtWidgets.QAction(MainWindow)
        self.actionKamera5.setCheckable(True)
        self.actionKamera5.setObjectName("actionKamera5")
        self.actionCikis = QtWidgets.QAction(MainWindow)
        self.actionCikis.setObjectName("actionCikis")
        self.actionYazdir = QtWidgets.QAction(MainWindow)
        self.actionYazdir.setObjectName("actionYazdir")
        self.actionPersonelGirisCikisBilgileri = QtWidgets.QAction(MainWindow)
        self.actionPersonelGirisCikisBilgileri.setObjectName("actionPersonelGirisCikisBilgileri")
        self.actionFotograf_Ekle = QtWidgets.QAction(MainWindow)
        self.actionFotograf_Ekle.setObjectName("actionFotograf_Ekle")
        self.actionPersonelleriExcelDosyasinaAktar = QtWidgets.QAction(MainWindow)
        self.actionPersonelleriExcelDosyasinaAktar.setObjectName("actionPersonelleriExcelDosyasinaAktar")
        self.actionGiris_Cikis_KayitlariniExcelDosyasinaAktar = QtWidgets.QAction(MainWindow)
        self.actionGiris_Cikis_KayitlariniExcelDosyasinaAktar.setObjectName("actionGiris_Cikis_KayitlariniExcelDosyasinaAktar")
        self.menuExceleAktar.addAction(self.actionPersonelleriExcelDosyasinaAktar)
        self.menuExceleAktar.addAction(self.actionGiris_Cikis_KayitlariniExcelDosyasinaAktar)
        self.menuDosya.addAction(self.menuExceleAktar.menuAction())
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionCikis)
        self.menuPersonel.addAction(self.actionPersoneller)
        self.menuPersonel.addAction(self.actionPersonelEkle)
        self.menuPersonel.addSeparator()
        self.menuPersonel.addAction(self.actionPersonelGirisCikisBilgileri)
        self.menuPersonel.addSeparator()
        self.menuHakkinda.addAction(self.actionProgramHakkinda)
        self.menuHakkinda.addAction(self.actionGelistiriciHakkinda)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuPersonel.menuAction())
        self.menubar.addAction(self.menuHakkinda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Personel Takip"))
        self.label.setText(_translate("MainWindow", "KAMERADA GORUNTULENEN YUZLER VE BILGILERI"))
        self.startButton.setText(_translate("MainWindow", "Kamerayi Baslat"))
        self.stopButton.setText(_translate("MainWindow", "Kamerayi Durdur"))
        self.detectButton.setText(_translate("MainWindow", "Yuz Tanimayi Baslat"))
        self.trainButton.setText(_translate("MainWindow", "Yuzleri Tara"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "T.C. Numarasi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Adi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Soyadi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Gorunme Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Gorunme Saati"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuExceleAktar.setTitle(_translate("MainWindow", "Excel\'e Aktar"))
        self.menuPersonel.setTitle(_translate("MainWindow", "Personel"))
        self.menuHakkinda.setTitle(_translate("MainWindow", "Hakkinda"))
        self.actionDiskten_Ekle.setText(_translate("MainWindow", "Diskten Ekle"))
        self.actionProgramHakkinda.setText(_translate("MainWindow", "Program Hakkinda"))
        self.actionGelistiriciHakkinda.setText(_translate("MainWindow", "Gelistirici Hakkinda"))
        self.actionPersonelEkle.setText(_translate("MainWindow", "Personel Ekle"))
        self.actionPersoneller.setText(_translate("MainWindow", "Personeller"))
        self.actionLoglar.setText(_translate("MainWindow", "Genel Loglar"))
        self.actionKamera1.setText(_translate("MainWindow", "Kamera-1"))
        self.actionKamera2.setText(_translate("MainWindow", "Kamera-2"))
        self.actionKamera3.setText(_translate("MainWindow", "Kamera-3"))
        self.actionKamera4.setText(_translate("MainWindow", "Kamera-4"))
        self.actionKamera5.setText(_translate("MainWindow", "Kamera-5"))
        self.actionCikis.setText(_translate("MainWindow", "Cikis"))
        self.actionYazdir.setText(_translate("MainWindow", "Excel\'e Yazdir"))
        self.actionPersonelGirisCikisBilgileri.setText(_translate("MainWindow", "Personel Giris/Cikis Bilgileri"))
        self.actionFotograf_Ekle.setText(_translate("MainWindow", "Fotograf Ekle"))
        self.actionPersonelleriExcelDosyasinaAktar.setText(_translate("MainWindow", "Personelleri Excel Dosyasina Aktar"))
        self.actionGiris_Cikis_KayitlariniExcelDosyasinaAktar.setText(_translate("MainWindow", "Giris-Cikis Kayitlarini Excel Dosyasina Aktar"))

