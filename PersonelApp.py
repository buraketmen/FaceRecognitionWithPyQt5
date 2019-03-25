import numpy
import os
import cv2
import datetime
import locale
from PyQt5 import QtGui, QtWidgets
from PersonelTakipMain import Ui_MainWindow
import PersonelSureEkrani
from Personel import Ui_Dialog
import PersonelEkle
import PersonelGuncelle
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import face_recognition.api as face_recognition
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog, QWidget
from xlsxwriter.workbook import Workbook
import sqlite3

locale.setlocale(locale.LC_ALL, '')
conn = sqlite3.connect('personelDB.db')
curs = conn.cursor()
curs.execute("""
            CREATE TABLE IF NOT EXISTS personeller(
            TcNo INTEGER PRIMARY KEY NOT NULL,
            image TEXT,
            Ad VARCHAR(20),
            Soyad VARCHAR(20),
            Yas INTEGER(2),
            Pozisyon VARCHAR(30), 
            TelNo INTEGER(10),
            MesaiTipi TEXT,
            Aciklama TEXT)
            """)
curs.execute("""
            CREATE TABLE IF NOT EXISTS giriscikis(
            GirisCikisId INTEGER PRIMARY KEY,
            TcNo INTEGER ,
            Ad TEXT ,
            Soyad TEXT ,
            Tarih TEXT ,
            Saat TEXT ,
            Tipi TEXT)
            """ )
curs.execute("""
            CREATE TABLE IF NOT EXISTS log(
            LogId INTEGER PRIMARY KEY,
            TcNo INTEGER,
            Ad VARCHAR(15),
            Soyad VARCHAR(15),
            Tarih TEXT,
            Saat TEXT)
            """)

known_face_encodings = []
known_face_names = []

def Train_Faces():
    if (os.path.exists("./yuzler")):
        known_face_names.clear()
        known_face_encodings.clear()
        for root, dirs, files in os.walk("./yuzler"):
            for filename in files:
                file_result = filename.split("_")
                known_face_names.append(file_result[0])
                image = face_recognition.load_image_file("yuzler/" + filename)
                image_face_encoding = face_recognition.face_encodings(image)[0]
                known_face_encodings.append(image_face_encoding)

class PersonelApp(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(PersonelApp,self).__init__(parent)
        self.setupUi(self)
        self.image = None
        self.photo = None
        self.fname = None
        self.capture = None
        self.oldtcno=None
        self.iterim=1
        self.mesaitipi = "Gunduz"
        self.oldsecond=None
        self.backimage= cv2.imread('background.jpg')
        self.Init_Ui()
        self.status_bar()
        curs.execute("DELETE FROM log")

    def status_bar(self):
        self.statusbar.show()
        self.statusbar.showMessage('Program Hazır')
        self.startButton.setStatusTip('Kamerayı başlatmak için tıkla.')
        self.stopButton.setStatusTip('Kamerayı durdurmak için tıkla.')
        self.detectButton.setStatusTip('Yüz tanımayı başlatmak için tıkla.')
        self.trainButton.setStatusTip('Kayıtlı personellerin yüzlerini kimliklendirmek için tıkla.')
        self.actionPersoneller.setStatusTip('Personeller ekranı için tıkla.')
        self.actionPersonelEkle.setStatusTip('Personel ekleme ekranı için tıkla.')
        self.actionPersonelleriExcelDosyasinaAktar.setStatusTip('Personelleri excel tablosuna aktarır.')
        self.actionGiris_Cikis_KayitlariniExcelDosyasinaAktar.setStatusTip('Giris-cikis kayitlarini excel tablosuna aktarır.')
        self.actionPersonelGirisCikisBilgileri.setStatusTip('Personellerin giris-cikis saatleri için tıkla.')

    def Init_Ui(self):
        self.show()
        self.startButton.clicked.connect(self.start_webcam)
        self.startButton.setEnabled(True)

        self.stopButton.clicked.connect(self.stop_webcam)
        self.stopButton.setEnabled(False)
        self.cameraStatus = False

        self.detectButton.toggled.connect(self.detect_webcam_face)
        self.detectButton.setCheckable(True)
        self.detectButton.setEnabled(False)
        self.face_Enabled = False

        self.trainButton.clicked.connect(self.Train_Faces)
        self.face_Train =False

        self.actionGiris_Cikis_KayitlariniExcelDosyasinaAktar.triggered.connect(self.GirisCikis_Excel)
        self.actionPersonelleriExcelDosyasinaAktar.triggered.connect(self.Personel_Excel)
        self.actionPersonelEkle.triggered.connect(self.Show_PersonelEkle)
        self.actionPersoneller.triggered.connect(self.Show_Personeller)
        self.actionPersonelGirisCikisBilgileri.triggered.connect(self.Show_PersonelGirisCikis)
        self.actionGelistiriciHakkinda.triggered.connect(self.Contact)
        self.actionProgramHakkinda.triggered.connect(self.About_Program)
        try:
            self.capture = cv2.VideoCapture(0)
        except:
            self.startButton.setEnabled(False)
            QMessageBox.warning(self, 'Kamera Hatasi!',
                                "Sistemde herhangi bir kamera bulunamadi.\n",
                                QMessageBox.Ok, QMessageBox.Ok)


    def Personel_Excel(self):
        try:
            fname, filter = QFileDialog().getSaveFileName(self, 'Excel Dosyasini Kaydet', '', "Excel Files (*.xlsx)")
            if fname:
                workbook = Workbook(fname)
                worksheet = workbook.add_worksheet()
                content = 'SELECT TcNo,Ad,Soyad,Yas,Pozisyon,TelNo,MesaiTipi,Aciklama,image FROM personeller'
                mysel = conn.execute(content)
                cell_format = workbook.add_format({'bold': True, 'italic': False})
                worksheet.write(0,0,"T.C. No",cell_format)
                worksheet.write(0, 1, "Ad",cell_format)
                worksheet.write(0, 2, "Soyad",cell_format)
                worksheet.write(0, 3, "Yas",cell_format)
                worksheet.write(0, 4, "Pozisyon",cell_format)
                worksheet.write(0, 5, "Telefon Numarasi",cell_format)
                worksheet.write(0, 6, "Mesai Tipi",cell_format)
                worksheet.write(0, 7, "Aciklama",cell_format)
                worksheet.write(0, 8, "Fotograf Uzantisi",cell_format)
                for i, row in enumerate(mysel):
                    for j, value in enumerate(row):
                        worksheet.write(i+1, j, row[j])
                workbook.close()
        except Exception:
            QMessageBox.warning(self, 'Kaydetme Hatasi!',
                                               "Bilinmeyen bir hata gerçekleşti!.\n",
                                               QMessageBox.Ok, QMessageBox.Ok)
    def GirisCikis_Excel(self):
        try:
            fname, filter = QFileDialog().getSaveFileName(self, 'Excel Dosyasini Kaydet', '', "Excel Files (*.xlsx)")
            if fname:
                workbook = Workbook(fname)
                worksheet = workbook.add_worksheet()
                content = 'SELECT TcNo,Ad,Soyad,Tarih,Saat,Tipi FROM giriscikis'
                mysel = conn.execute(content)
                cell_format = workbook.add_format({'bold': True, 'italic': False})
                worksheet.write(0, 0, "T.C. No",cell_format)
                worksheet.write(0, 1, "Ad",cell_format)
                worksheet.write(0, 2, "Soyad",cell_format)
                worksheet.write(0, 3, "Tarih",cell_format)
                worksheet.write(0, 4,"Saat",cell_format)
                worksheet.write(0, 5, "Tipi",cell_format)
                for i, row in enumerate(mysel):
                    for j, value in enumerate(row):
                        worksheet.write(i+1, j, row[j])
                workbook.close()
        except Exception:
            QMessageBox.warning(self, 'Kaydetme Hatasi!',
                                "Bilinmeyen bir hata gerçekleşti!.\n",
                                QMessageBox.Ok, QMessageBox.Ok)
    def Contact(self):
        QMessageBox.information(self, 'Gelistirici Hakkinda...',
                            "Bu program Sakarya Universitesi ogrencisi, Hasan Burak Ketmen tarafından yazilmistir.\n" + "Iletisim icin buraketmen@gmail.com mail adresine mail atabilirsiniz.",
                            QMessageBox.Ok, QMessageBox.Ok)
    def About_Program(self):
        QMessageBox.information(self, 'Program Hakkinda...',
                                "Bu program, HOG ve 68 düğüm algoritmalarını kullanarak yuz tanima islemi yapar ve taninan yuzleri bir listeye cesitli filtrelerden gecirerek kaydedip personelin giris ve cikisini kontrol etme imkani sunar.\n",
                                QMessageBox.Ok, QMessageBox.Ok)

    def Show_Personeller(self):
        self.adding = Personel()
        self.adding.exec_()

    def Show_PersonelEkle(self):
        self.addingAdd = PersonelEkle()
        self.addingAdd.buttonPersonelEkle.clicked.connect(self.Add_Personel)
        self.addingAdd.buttonFotografYukle.clicked.connect(self.Load_Photo)
        self.addingAdd.exec_()

    def Show_PersonelGirisCikis(self):
        self.addingGirisCikis = PersonelSureEkrani()
        self.addingGirisCikis.exec_()

    def detect_webcam_face(self, status):
        if status:
            self.detectButton.setText('Yuz Tanimayi Durdur')
            self.face_Enabled = True

        else:
            self.detectButton.setText('Yuz Tanimayi Baslat')
            self.face_Enabled = False
            self.iterim=1

    def start_webcam(self):
        if(self.capture!=None):
            self.cameraStatus=True
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)
            self.trainButton.setEnabled(False)
            if(self.face_Train==True):
                self.detectButton.setEnabled(True)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(1)
            self.statusbar.showMessage('Kamera baslatildi.')

    def stop_webcam(self):
        self.cameraStatus=False
        if(self.face_Enabled != False):
            self.face_Enabled= False
            self.detectButton.toggle()
            self.detectButton.setText('Yuz Tanimayi Baslat')
        self.timer.stop()
        self.displayImage(self.backimage)
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.detectButton.setEnabled(False)
        self.trainButton.setEnabled(True)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image, 1)
        if (self.face_Enabled):
            detected_image = self.detect_face(self.image)
            self.displayImage(detected_image)
        else:
            self.displayImage(self.image)

    def Train_Faces(self):
        self.face_Train =True
        if (os.path.exists("./yuzler")):
            known_face_names.clear()
            known_face_encodings.clear()
            for root, dirs, files in os.walk("./yuzler"):
                for filename in files:
                    file_result = filename.split("_")
                    known_face_names.append(file_result[0])
                    image = face_recognition.load_image_file("yuzler/" + filename)
                    image_face_encoding = face_recognition.face_encodings(image)[0]
                    known_face_encodings.append(image_face_encoding)
                    switch_name = filename[::-1]
                    dotname = switch_name[4:]
                    new_name = dotname[::-1]
                    self.statusbar.showMessage(new_name + " kimlik numarali kisinin yuzu tarandi.")
        QMessageBox.information(self, 'Yuz Taramasi',
                            "Kayitli personellerin yuzleri basariyla tarandi!\n" ,
                            QMessageBox.Ok, QMessageBox.Ok)
        if(self.cameraStatus == True):
            self.detectButton.setEnabled(True)

    def detect_face(self, img):
        face_locations = []
        face_encodings = []
        face_names = []

        #small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        #rgb_small_frame = small_frame[:, :, ::-1]
        #face_locations = face_recognition.face_locations(rgb_small_frame)
        #face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        rgb_img = img[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_img)
        face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Bilinmiyor"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            #top *= 4
            #right *= 4
            #bottom *= 4
            #left *= 4
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 1)
            cv2.rectangle(img, (left, bottom + 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            if(str(name) != "Bilinmiyor"):
                switch_name = name[::-1]
                dotname = switch_name[4:]
                new_name = dotname[::-1]
                tcno=new_name
                if(str(self.oldtcno) !=str(tcno) and self.oldtcno!=None):
                    self.Add_Log(self.oldtcno)
                self.Add_Log(tcno)
                self.oldtcno = tcno
            else:
                new_name = "Bilinmiyor"
            cv2.putText(img, new_name, (left + 1, bottom + 30), font, 1.0, (255, 255, 255), 1)
        return img

    def Add_Log(self,tcno):
        an = datetime.datetime.now()
        second = int(an.second)
        hour = int(an.hour)
        date = str(an.day) + "/" + str(an.month) + "/" + str(an.year)
        time = str(an.hour) + ":" + str(an.minute) + ":" + str(an.second)

        logdate= "./Log/" + str(an.day) + "." + str(an.month) + "." + str(an.year) + ".txt"
        logToday = open(logdate,"a+")

        search = curs.execute('SELECT Ad, Soyad, MesaiTipi FROM personeller WHERE TcNo = ? ', (tcno,))
        results = search.fetchone()
        ad = str(results[0])
        soyad = str(results[1])
        mesaitipi = str(results[2])

        tipi = "Bilinmiyor"
        if(mesaitipi=="Gunduz"):
            if(7<=hour<=11):
                tipi = "Giris"
            if(23 >= hour >= 16):
                tipi = "Cikis"
        if (mesaitipi == "Gece"):
            if (7 <= hour <= 11):
                tipi = "Cikis"
            if (23 >= hour >= 16):
                tipi = "Giris"

        if (self.iterim == 1):
            self.iterim = 2
            self.oldsecond = second
            logToday.write(tcno + " kimlik numarali kisi " + time + " saatinde kamerada gorundu.\n")
            curs.execute("INSERT INTO log (TcNo,Ad,Soyad,Tarih,Saat) VALUES(?,?,?,?,?)",
                         (tcno, ad, soyad, date, time))
            conn.commit()
            self.Load_Database()

        searchall = curs.execute('SELECT Saat FROM giriscikis WHERE TcNo = ? AND Tarih =?', (tcno,date,))
        rows = searchall.fetchall()
        i=0
        if(rows!=None):
            for row in rows:
                i=i+1
        if(i==0):
            if (7 <= hour <= 11 or 23 >= hour >= 16):
                curs.execute("INSERT INTO giriscikis (TcNo,Ad,Soyad,Tarih,Saat,Tipi) VALUES(?,?,?,?,?,?)",
                             (tcno, ad, soyad, date, time,tipi))
                conn.commit()
        if(i==1):
            for row in rows:
                try:
                    log_hour = int(row[0][0:2])
                except ValueError:
                    log_hour = int(row[0][0:1])
            if(log_hour +5 < hour):
                if (7 <= hour <= 11 or 23 >= hour >= 16):
                    curs.execute("INSERT INTO giriscikis (TcNo,Ad,Soyad,Tarih,Saat,Tipi) VALUES(?,?,?,?,?,?)",
                                 (tcno, ad, soyad, date, time,tipi))
                    conn.commit()

        if(self.oldsecond +1 <= second):
            self.oldsecond = second
            logToday.write(tcno + " kimlik numarali kisi "+ time + " saatinde kamerada gorundu.\n")
            curs.execute("INSERT INTO log (TcNo,Ad,Soyad,Tarih,Saat) VALUES(?,?,?,?,?)",
                         (tcno, ad, soyad, date, time))
            conn.commit()
            self.Load_Database()

    def Add_Personel(self):
        global known_face_encodings
        global known_face_names
        tcno = self.addingAdd.editTcNo.text()
        ad = self.addingAdd.editAd.text()
        soyad = self.addingAdd.editSoyad.text()
        yas = self.addingAdd.editYas.text()
        telno = self.addingAdd.editTelefonNo.text()
        pozisyon = self.addingAdd.editPozisyon.text()
        aciklama = self.addingAdd.editAciklama.text()
        filename = ""
        if (str(self.photo) != "None"):
            filename = "./yuzler/" + str(tcno) + ".jpg"
        search = curs.execute('SELECT TcNo FROM personeller WHERE TcNo = ? ', (tcno,))
        results = search.fetchone()
        if (len(tcno) == 11 and len(ad) <= 20 and len(soyad) <= 20 and len(yas) <= 2 and len(telno) <= 11 and len(pozisyon) <= 30):
            if (results == None):
                if (len(filename) != 0):
                    face_names = []
                    name = "Bilinmiyor"
                    face_names.append(name)
                    rgb_img = self.photo[:, :, ::-1]
                    face_locations = face_recognition.face_locations(rgb_img)
                    if(len(face_locations)==1):
                        for (top, right, bottom, left), name in zip(face_locations, face_names):
                            crop_img = self.photo[top:bottom, left:right]
                        cv2.imwrite(filename, crop_img)
                        if(self.addingAdd.radioButtonGece.isChecked()==True):
                            self.mesaitipi ="Gece"
                        image = face_recognition.load_image_file("./yuzler/" + str(tcno) + ".jpg")
                        if(len(face_recognition.face_encodings(image))>0):
                            known_face_names.append(str(tcno) + ".jpg")
                            image_face_encoding = face_recognition.face_encodings(image)[0]
                            known_face_encodings.append(image_face_encoding)
                            curs.execute("""INSERT INTO personeller(TcNo,image,Ad,Soyad,Yas,Pozisyon,TelNo,Aciklama,MesaiTipi) 
                                                                                                                                VALUES(?,?,?,?,?,?,?,?,?)""",
                                         (tcno, filename, ad, soyad, yas, pozisyon, telno, aciklama, self.mesaitipi))
                            conn.commit()
                            self.Load_Database()
                            self.addingAdd.close()
                            self.photo = None
                            self.mesaitipi = "Gunduz"
                            QMessageBox.information(self, 'Kayit Basarili!',
                                                    "Personel kaydi ve yuz taramasi basariyla yapildi.\n",
                                                    QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            os.remove("./yuzler/" + str(tcno) + ".jpg")
                            QMessageBox.warning(self, 'Gecersiz Fotograf',
                                                "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                                QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.warning(self, 'Gecersiz Fotograf',
                                            "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                            QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.photo = None
                    QMessageBox.warning(self, 'Fotograf Eklenmedi',
                                         "Lutfen olusturdugunuz personel kaydi icin fotograf belirleyin.\n",
                                         QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'Kayit Basarisiz',
                                     "Girilen T.C. ile personel mevcut.\n",
                                     QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Kayit Basarisiz',
                                 "Lutfen gecerli bilgiler giriniz.\n",
                                 QMessageBox.Ok, QMessageBox.Ok)

    def Load_Database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        content = 'SELECT TcNo,Ad,Soyad,Tarih,Saat FROM log'
        res = conn.execute(content)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        return

    def Load_Photo(self):
        try:
            self.fname, filter = QFileDialog().getOpenFileName(self, 'Fotograf Sec', '', ("Image Files (*.jpg)"))
            if self.fname:
                self.loadImage(self.fname)
        except Exception as error:
            self.photo = None
            QMessageBox.warning(self, 'Fotograf Uzanti Hatasi',
                                               "Fotograf uzantisini degistirerek tekrar deneyiniz.",
                                               QMessageBox.Ok, QMessageBox.Ok)

    def loadImage(self, fname):
        stream = open(fname, "rb")
        bytes = bytearray(stream.read())
        numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
        self.photo = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        self.displayPhoto()

    def displayPhoto(self):
        qformat = QImage.Format_Indexed8
        if len(self.photo.shape) == 3:  # rows[0],cols[1],channels[2]
            if (self.photo.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.photo, self.photo.shape[1], self.photo.shape[0], self.photo.strides[0], qformat)
        # BGR >RGB
        img = img.rgbSwapped()
        self.addingAdd.labelFotograf.setPixmap(QPixmap.fromImage(img))
        self.addingAdd.labelFotograf.setScaledContents(True)

    def displayImage(self, img):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:  # [0]=satırlar, [1]=sütunlar, [2]=kanallar
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        # BGR>>RGB
        outImage = outImage.rgbSwapped()
        self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
        self.imgLabel.setScaledContents(True)

class Personel(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(Personel,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Personel Ekranı')
        try:
            self.setWindowIcon(QtGui.QIcon('./icon.png'))
        except Exception:
            pass
        self.Load_Database()
        self.Init_Ui()
        self.mesaitipi="Gunduz"
        self.oldtcno = None
        self.photo = None
        self.oldphoto= None
        self.avaiblephoto= True

    def Init_Ui(self):
        self.buttonPersonelEkle.clicked.connect(self.Show_PersonelEkle)
        self.buttonPersonelSil.clicked.connect(self.Delete_Personel)
        self.buttonPersonelGuncelle.clicked.connect(self.Show_PersonelGuncelle)
        self.buttonPersonelGirisSaatleri.clicked.connect(self.Show_PersonelSureEkrani)
        self.buttonPersonelAra.clicked.connect(self.Search_Personel)
        self.tableWidget.itemClicked.connect(self.Table_Clicked)
        self.buttonPersonelGuncelle.setEnabled(False)
        self.buttonPersonelSil.setEnabled(False)

    def Show_PersonelSureEkrani(self):
        self.adding = PersonelSureEkrani()
        self.adding.exec_()

    def Show_PersonelEkle(self):
        self.addingAdd = PersonelEkle()
        self.addingAdd.buttonPersonelEkle.clicked.connect(self.Add_Personel)
        self.addingAdd.buttonFotografYukle.clicked.connect(self.Load_Photo)
        self.addingAdd.exec_()

    def Show_PersonelGuncelle(self):
        self.addingUpdate = PersonelGuncelle()
        self.buttonPersonelGuncelle.setEnabled(False)
        self.buttonPersonelSil.setEnabled(False)
        self.addingUpdate.buttonFotografYukle.clicked.connect(self.Loaded_Photo)
        self.addingUpdate.buttonPersonelDuzenle.clicked.connect(self.Update_Personel)
        self.Show_Data()
        self.addingUpdate.exec_()

    def Table_Clicked(self):
        self.buttonPersonelGuncelle.setEnabled(True)
        self.buttonPersonelSil.setEnabled(True)

    def Search_Personel(self):
        tcno = self.editAranacakTcNo.text()
        if(str(tcno)!=""):
            while self.tableWidget.rowCount() > 0:
                self.tableWidget.removeRow(0)
            res = conn.execute("SELECT TcNo,Ad,Soyad,Yas,Pozisyon,TelNo,MesaiTipi,Aciklama FROM personeller WHERE TcNo = ? ",
                               (tcno,))
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
            return
        else:
            self.Load_Database()

    def Show_Data(self):
        content = 'SELECT TcNo,Ad,Soyad,Yas,Pozisyon,TelNo,MesaiTipi,Aciklama FROM personeller'
        res = conn.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                self.oldtcno = data[0]
                tcno=self.oldtcno
                ad = data[1]
                soyad = data[2]
                yas = data[3]
                pozisyon = data[4]
                telno = data[5]
                mesaitipi=data[6]
                aciklama = data[7]
                self.addingUpdate.editTcNo.setText(str(tcno))
                self.addingUpdate.editAd.setText(str(ad))
                self.addingUpdate.editSoyad.setText(str(soyad))
                self.addingUpdate.editYas.setText(str(yas))
                self.addingUpdate.editPozisyon.setText(str(pozisyon))
                self.addingUpdate.editTelefonNo.setText(str(telno))
                self.addingUpdate.editAciklama.setText(str(aciklama))
                if(mesaitipi=="Gece"):
                    self.addingUpdate.radioButtonGeceGuncelle.setChecked(True)
                if(mesaitipi=="Gunduz"):
                    self.addingUpdate.radioButtonGunduzGuncelle.setChecked(True)
                if os.path.exists("./yuzler/" + str(tcno) + ".jpg"):
                    self.photo = cv2.imread("./yuzler/" +str(tcno) + ".jpg", cv2.IMREAD_ANYCOLOR)
                    self.oldphoto = self.photo
                    self.displayPhoto(2)

    def Add_Personel(self):
        global known_face_encodings
        global known_face_names
        tcno = self.addingAdd.editTcNo.text()
        ad = self.addingAdd.editAd.text()
        soyad = self.addingAdd.editSoyad.text()
        yas = self.addingAdd.editYas.text()
        telno = self.addingAdd.editTelefonNo.text()
        pozisyon = self.addingAdd.editPozisyon.text()
        aciklama = self.addingAdd.editAciklama.text()
        filename = ""
        if (str(self.photo) != "None"):
            filename = "./yuzler/" + str(tcno) + ".jpg"
        search = curs.execute('SELECT TcNo FROM personeller WHERE TcNo = ? ', (tcno,))
        results = search.fetchone()
        if (len(tcno) == 11 and len(ad) <= 20 and len(soyad) <= 20 and len(yas) <= 2 and len(telno) <= 11 and len(
                pozisyon) <= 30):
            if (results == None):
                if (len(filename) != 0):
                    face_names = []
                    name = "Bilinmiyor"
                    face_names.append(name)
                    rgb_img = self.photo[:, :, ::-1]
                    face_locations = face_recognition.face_locations(rgb_img)
                    if (len(face_locations) == 1):
                        for (top, right, bottom, left), name in zip(face_locations, face_names):
                            crop_img = self.photo[top:bottom, left:right]
                        cv2.imwrite(filename, crop_img)
                        if (self.addingAdd.radioButtonGece.isChecked() == True):
                            self.mesaitipi = "Gece"
                        image = face_recognition.load_image_file("./yuzler/" + str(tcno) + ".jpg")
                        if (len(face_recognition.face_encodings(image)) > 0):
                            known_face_names.append(str(tcno) + ".jpg")
                            image_face_encoding = face_recognition.face_encodings(image)[0]
                            known_face_encodings.append(image_face_encoding)
                            curs.execute("""INSERT INTO personeller(TcNo,image,Ad,Soyad,Yas,Pozisyon,TelNo,Aciklama,MesaiTipi) 
                                                                                                                        VALUES(?,?,?,?,?,?,?,?,?)""",
                                         (tcno, filename, ad, soyad, yas, pozisyon, telno, aciklama, self.mesaitipi))
                            conn.commit()
                            self.Load_Database()
                            self.addingAdd.close()
                            self.photo = None
                            self.mesaitipi = "Gunduz"
                            QMessageBox.information(self, 'Kayit Basarili!',
                                                    "Personel kaydi ve yuz taramasi basariyla yapildi.\n",
                                                    QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            os.remove("./yuzler/" + str(tcno) + ".jpg")
                            QMessageBox.warning(self, 'Gecersiz Fotograf',
                                                "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                                QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        QMessageBox.warning(self, 'Gecersiz Fotograf',
                                            "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                            QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.photo = None
                    QMessageBox.warning(self, 'Fotograf Eklenmedi',
                                        "Lutfen olusturdugunuz personel kaydi icin fotograf belirleyin.\n",
                                        QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'Kayit Basarisiz',
                                    "Girilen T.C. ile personel mevcut.\n",
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Kayit Basarisiz',
                                "Lutfen gecerli bir T.C. kimlik numarasi giriniz.\n",
                                QMessageBox.Ok, QMessageBox.Ok)

    def Update_Personel(self):
        face_names = []
        name = "Bilinmiyor"
        face_names.append(name)
        tcno = self.addingUpdate.editTcNo.text()
        ad = self.addingUpdate.editAd.text()
        soyad = self.addingUpdate.editSoyad.text()
        yas = self.addingUpdate.editYas.text()
        telno = self.addingUpdate.editTelefonNo.text()
        pozisyon = self.addingUpdate.editPozisyon.text()
        aciklama = self.addingUpdate.editAciklama.text()
        if(self.addingUpdate.radioButtonGeceGuncelle.isChecked()==True):
            self.mesaitipi="Gece"
        filename = "./yuzler/" + str(tcno) + ".jpg"
        search = curs.execute('SELECT TcNo FROM personeller WHERE TcNo = ? ', (tcno,))
        results = search.fetchone()
        if (len(tcno) == 11 and len(ad) <= 20 and len(soyad) <= 20 and len(yas) <= 2 and len(telno) <= 11 and len(
                pozisyon) <= 30):
            if(str(self.oldtcno)==str(tcno)):
                if(len(self.oldphoto)!=len(self.photo)):
                    rgb_img = self.photo[:, :, ::-1]
                    face_locations = face_recognition.face_locations(rgb_img)
                    if (len(face_locations) == 1):
                        for (top, right, bottom, left), name in zip(face_locations, face_names):
                            crop_img = self.photo[top:bottom, left:right]
                        if (len(face_recognition.face_encodings(crop_img)) > 0):
                            if os.path.exists("./yuzler/" + str(self.oldtcno) + ".jpg"):
                                os.remove("./yuzler/" + str(self.oldtcno) + ".jpg")
                            cv2.imwrite(filename, crop_img)
                            curs.execute("UPDATE personeller SET TcNo = ? , image = ? , Ad = ? ,Soyad = ? , Yas = ? , Pozisyon = ? , TelNo = ? , MesaiTipi = ?, Aciklama = ? WHERE TcNo = ?",
                                         (tcno, filename, ad, soyad, yas, pozisyon, telno, self.mesaitipi, aciklama, self.oldtcno))
                            conn.commit()
                            self.photo = None
                            self.oldtcno = None
                            self.oldphoto = None
                            self.mesaitipi = "Gunduz"
                            self.Load_Database()

                            self.addingUpdate.close()
                            QMessageBox.information(self, 'Guncelleme Basarili!',
                                                    "Personel bilgi guncellemesi basariyla yapildi.\n" + "Yuz taramasi yapilmadigi icin tekrar tarama yapilmasi tavsiye edilir.",
                                                    QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            print("1")
                            self.loadedImage("./yuzler/" + str(self.oldtcno) + ".jpg")
                            QMessageBox.warning(self, 'Gecersiz Fotograf',
                                                "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                                QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        print("2")
                        self.loadedImage("./yuzler/" + str(self.oldtcno) + ".jpg")
                        QMessageBox.warning(self, 'Gecersiz Fotograf',
                                            "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                            QMessageBox.Ok, QMessageBox.Ok)
                else:
                    curs.execute(
                        "UPDATE personeller SET TcNo = ? , image = ? , Ad = ? ,Soyad = ? , Yas = ? , Pozisyon = ? , TelNo = ? , MesaiTipi = ?, Aciklama = ? WHERE TcNo = ?",
                        (tcno, filename, ad, soyad, yas, pozisyon, telno, self.mesaitipi, aciklama, self.oldtcno))
                    conn.commit()
                    self.photo = None
                    self.oldtcno = None
                    self.oldphoto = None
                    self.mesaitipi = "Gunduz"
                    self.Load_Database()

                    self.addingUpdate.close()
                    QMessageBox.information(self, 'Guncelleme Basarili!',
                                            "Personel bilgi guncellemesi basariyla yapildi.\n" + "Yuz taramasi yapilmadigi icin tekrar tarama yapilmasi tavsiye edilir.",
                                            QMessageBox.Ok, QMessageBox.Ok)

            else:
                if(results==None):
                    if (len(self.oldphoto)!=len(self.photo)):
                        rgb_img = self.photo[:, :, ::-1]
                        face_locations = face_recognition.face_locations(rgb_img)
                        if (len(face_locations) == 1):
                            for (top, right, bottom, left), name in zip(face_locations, face_names):
                                crop_img = self.photo[top:bottom, left:right]
                            if (len(face_recognition.face_encodings(crop_img)) > 0):
                                if os.path.exists("./yuzler/" + str(self.oldtcno) + ".jpg"):
                                    os.remove("./yuzler/" + str(self.oldtcno) + ".jpg")
                                cv2.imwrite(filename, crop_img)
                                curs.execute( "UPDATE personeller SET TcNo = ? , image = ? , Ad = ? , Soyad = ? , Yas = ? , Pozisyon = ? , TelNo = ? , MesaiTipi = ?, Aciklama = ? WHERE TcNo = ?",
                                    (tcno, filename, ad, soyad, yas, pozisyon, telno, self.mesaitipi, aciklama, self.oldtcno))
                                conn.commit()
                                self.photo = None
                                self.oldtcno = None
                                self.oldphoto = None
                                self.mesaitipi = "Gunduz"
                                self.Load_Database()
                                self.addingUpdate.close()
                                QMessageBox.information(self, 'Guncelleme Basarili!',
                                                        "Personel bilgi guncellemesi basariyla yapildi.\n" + "Yuz taramasi yapilmadigi icin tekrar tarama yapilmasi tavsiye edilir.",
                                                        QMessageBox.Ok, QMessageBox.Ok)
                            else:
                                self.loadedImage("./yuzler/" + str(self.oldtcno) + ".jpg")
                                QMessageBox.warning(self, 'Gecersiz Fotograf',
                                                    "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                                    QMessageBox.Ok, QMessageBox.Ok)
                        else:
                            self.loadedImage("./yuzler/" + str(self.oldtcno) + ".jpg")
                            QMessageBox.warning(self, 'Gecersiz Fotograf',
                                                "Eklenmek istenen fotograf yuz tanima icin gecersiz.\n",
                                                QMessageBox.Ok, QMessageBox.Ok)
                    else:
                        if os.path.exists("./yuzler/" + str(self.oldtcno) + ".jpg"):
                            os.remove("./yuzler/" + str(self.oldtcno) + ".jpg")
                        cv2.imwrite(filename, self.oldphoto)
                        curs.execute(
                            "UPDATE personeller SET TcNo = ? , image = ? , Ad = ? , Soyad = ? , Yas = ? , Pozisyon = ? , TelNo = ? , MesaiTipi = ?, Aciklama = ? WHERE TcNo = ?",
                            (tcno, filename, ad, soyad, yas, pozisyon, telno, self.mesaitipi, aciklama, self.oldtcno))
                        conn.commit()
                        self.photo = None
                        self.oldtcno = None
                        self.oldphoto = None
                        self.mesaitipi = "Gunduz"
                        self.Load_Database()
                        self.addingUpdate.close()
                        QMessageBox.information(self, 'Guncelleme Basarili!',
                                                "Personel bilgi guncellemesi basariyla yapildi.\n" + "Yuz taramasi yapilmadigi icin tekrar tarama yapilmasi tavsiye edilir.",
                                                QMessageBox.Ok, QMessageBox.Ok)

                else:
                    QMessageBox.warning(self, 'Hata!',
                                        "Guncellenen T.C. numarasi ile kayit mevcut.\n",
                                        QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Kayit Basarisiz',
                                "Lutfen gecerli bir T.C. kimlik numarasi giriniz.\n",
                                QMessageBox.Ok, QMessageBox.Ok)


    def Delete_Personel(self):
        self.buttonPersonelSil.setEnabled(False)
        self.buttonPersonelGuncelle.setEnabled(False)
        content = 'SELECT * FROM personeller'
        res = conn.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                tcno = data[0]
                buttonReply = QMessageBox.question(self, 'Personel Silme İslemi', str(tcno) +
                                                   " kimlik numarali personeli sildiginizde personele ait giris ve cikis kayitlari da silinir. Bunu yapmak istediginize emin misiniz?",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    if os.path.exists("./yuzler/" + str(tcno) + ".jpg"):
                        os.remove("./yuzler/" + str(tcno) + ".jpg")
                    curs.execute("DELETE FROM personeller WHERE tcno=?", (tcno,))
                    curs.execute("DELETE FROM giriscikis WHERE tcno=?", (tcno,))
                    conn.commit()
                    self.Load_Database()
                    Train_Faces()
                    QMessageBox.information(self, 'Silme İslemi Basarili!',
                                            "Personelin silinmesi basariyla tamamlandi.\n",
                                            QMessageBox.Ok, QMessageBox.Ok)

                else:
                    self.Load_Database()
                self.show()

    def Load_Database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        content = 'SELECT TcNo,Ad,Soyad,Yas,Pozisyon,TelNo,MesaiTipi,Aciklama FROM personeller'
        res = conn.execute(content)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))
        self.labelToplamPersonelSayisi.setText("Toplam Personel Sayisi: " + str(self.tableWidget.rowCount()))
        return

    @pyqtSlot()
    def Loaded_Photo(self):
        try:
            self.fname, filter = QFileDialog().getOpenFileName(self, 'Fotograf Sec', '', ("Image Files (*.jpg)"))
            if self.fname:
                self.loadedImage(self.fname)
                self.avaiblephoto = True
        except Exception as error:
            self.avaiblephoto = False
            QMessageBox.warning(self, 'Fotograf Uzanti Hatasi',
                                               "Fotograf uzantisini degistirerek tekrar deneyiniz.",
                                               QMessageBox.Ok, QMessageBox.Ok)

    def loadedImage(self, fname):
        stream = open(fname, "rb")
        bytes = bytearray(stream.read())
        numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
        self.photo = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        self.displayPhoto(2)

    def Load_Photo(self):
        try:
            self.fname, filter = QFileDialog().getOpenFileName(self, 'Fotograf Sec', '', ("Image Files (*.jpg)"))
            if self.fname:
                self.loadImage(self.fname)
        except Exception as error:
            self.photo = None
            QMessageBox.warning(self, 'Fotograf Uzanti Hatasi',
                                               "Fotograf uzantisini degistirerek tekrar deneyiniz.",
                                               QMessageBox.Ok, QMessageBox.Ok)

    def loadImage(self, fname):
        stream = open(fname, "rb")
        bytes = bytearray(stream.read())
        numpyarray = numpy.asarray(bytes, dtype=numpy.uint8)
        self.photo = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)
        self.displayPhoto(1)

    def displayPhoto(self,window=1):
        qformat = QImage.Format_Indexed8
        if len(self.photo.shape) == 3:  # rows[0],cols[1],channels[2]
            if (self.photo.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.photo, self.photo.shape[1], self.photo.shape[0], self.photo.strides[0], qformat)
        # BGR >RGB
        img = img.rgbSwapped()
        if window==1:
            self.addingAdd.labelFotograf.setPixmap(QPixmap.fromImage(img))
            self.addingAdd.labelFotograf.setScaledContents(True)
        if window==2:
            self.addingUpdate.labelFotograf.setPixmap(QPixmap.fromImage(img))
            self.addingUpdate.labelFotograf.setScaledContents(True)

class PersonelSureEkrani(QDialog,PersonelSureEkrani.Ui_Dialog):
    def __init__(self,parent=None):
        super(PersonelSureEkrani,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Personel Giris ve Cikis Kayitlari')
        try:
            self.setWindowIcon(QtGui.QIcon('./icon.png'))
        except Exception:
            pass
        self.Load_Database()
        self.Init_Ui()

    def Init_Ui(self):
        self.buttonAra.clicked.connect(self.Search_Data)
        self.buttonKaydiSil.clicked.connect(self.Delete_Data)
        self.buttonKaydiSil.setEnabled(False)
        self.tableWidget.itemClicked.connect(self.Table_Clicked)

    def Table_Clicked(self):
        self.buttonKaydiSil.setEnabled(True)

    def Search_Data(self):
        tcno = self.editArama.text()
        if (str(tcno) != ""):
            while self.tableWidget.rowCount() > 0:
                self.tableWidget.removeRow(0)
            res = conn.execute("SELECT TcNo,Ad,Soyad,Tarih,Saat,Tipi FROM giriscikis WHERE TcNo = ? ", (tcno,))
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                for colm_index, colm_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
            return
        else:
            self.Load_Database()

    def Delete_Data(self):
        content = 'SELECT TcNo,Ad,Soyad,Tarih,Saat FROM giriscikis'
        res = conn.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                tcno = data[0]
                tarih = data[3]
                saat = data[4]
                buttonReply = QMessageBox.question(self, 'Kayit Silme',
                                                   "Kaydi silmek istediginize emin misiniz?",
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    curs.execute("DELETE FROM giriscikis WHERE TcNo =? AND tarih =? AND saat =? ", (tcno, tarih, saat,))
                    conn.commit()
                    self.Load_Database()


    def Load_Database(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        content = 'SELECT TcNo,Ad,Soyad,Tarih,Saat,Tipi FROM giriscikis'
        res = conn.execute(content)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        return

class PersonelEkle(QDialog,PersonelEkle.Ui_Dialog):
    def __init__(self,parent=None):
        super(PersonelEkle,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Personel Ekle')
        try:
            self.setWindowIcon(QtGui.QIcon('./icon.png'))
        except Exception:
            pass

class PersonelGuncelle(QDialog,PersonelGuncelle.Ui_Dialog):
    def __init__(self,parent=None):
        super(PersonelGuncelle,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Personeli Güncelle')
        try:
            self.setWindowIcon(QtGui.QIcon('./icon.png'))
        except Exception:
            pass

def main():
    app = QApplication([])
    win = PersonelApp()
    try:
        win.setWindowIcon(QtGui.QIcon('./icon.png'))
    except Exception:
        pass
    win.setWindowTitle('Personel Mesai Takip Uygulamasi')
    app.exec_()

main()

"""
class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.textAd = QtWidgets.QLabel('Kullanici Adi',self)
        self.textParola = QtWidgets.QLabel('Parola', self)

        self.buttonLogin = QtWidgets.QPushButton('Giris', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textAd)
        layout.addWidget(self.textName)
        layout.addWidget(self.textParola)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'admin' and
            self.textPass.text() == '123456'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Hata!', 'Yanlis kullanici veya şifre!')


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = PersonelApp()
        window.show()
        sys.exit(app.exec_())
"""

