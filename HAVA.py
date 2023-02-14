from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(585, 753)
        self.widget = QtWidgets.QWidget(Form)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget.setGeometry(QtCore.QRect(60, 10, 491, 731))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 441, 691))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("#label{\n"
"border-image: url(:/arka/Resimler/HD-wallpaper-gokyuzu-galaxy-night-note-purple-resullcanndemirrx-sky-solar-star-stars-system.jpg);\n"
"border-top-left-radius : 150px\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(147, 241, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 620, 441, 81))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0,80);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(47, 640, 101, 51))
        self.pushButton_2.setStyleSheet(".QPushButton{\n"
"  height: 100%;\n"
"  width: 100%;\n"
"  display: flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  background: linear-gradient(to left, #606c88 , #3f4c6b);\n"
"  font-family: \'Oswald\', sans-serif;\n"
"}\n"
"\n"
".QPushButton{\n"
"  text-align: center;\n"
"  text-transform: uppercase;\n"
"  cursor: pointer;\n"
"  font-size: 14px;\n"
"  letter-spacing: 4px;\n"
"  position: relative;\n"
"  background-color: #16a085;\n"
"  border: none;\n"
"  color: #fff;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  text-align: center;\n"
"  transition-duration: 0.4s;\n"
"  overflow: hidden;\n"
"  box-shadow: 0 5px 15px #193047;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #fff;\n"
"  box-shadow: 0px 2px 10px 5px #1abc9c;\n"
"  color: #000;\n"
"}\n"
"\n"
".QPushButton:after {\n"
"  content: \"\";\n"
"  background: #1abc9c;\n"
"  display: block;\n"
"  position: absolute;\n"
"  padding-top: 300%;\n"
"  padding-left: 350%;\n"
"  margin-left: -20px !important;\n"
"  margin-top: -120%;\n"
"  opacity: 0;\n"
"  transition: all 0.8s\n"
"}\n"
"\n"
".QPushButton:active:after {\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  opacity: 1;\n"
"  transition: 0s\n"
"}\n"
".QPushButton:focus { outline:0; }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.istanbul)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(157, 640, 101, 51))
        self.pushButton_3.setStyleSheet(".QPushButton{\n"
"  height: 100%;\n"
"  width: 100%;\n"
"  display: flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  background: linear-gradient(to left, #606c88 , #3f4c6b);\n"
"  font-family: \'Oswald\', sans-serif;\n"
"}\n"
"\n"
".QPushButton{\n"
"  text-align: center;\n"
"  text-transform: uppercase;\n"
"  cursor: pointer;\n"
"  font-size: 14px;\n"
"  letter-spacing: 4px;\n"
"  position: relative;\n"
"  background-color: #16a085;\n"
"  border: none;\n"
"  color: #fff;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  text-align: center;\n"
"  transition-duration: 0.4s;\n"
"  overflow: hidden;\n"
"  box-shadow: 0 5px 15px #193047;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #fff;\n"
"  box-shadow: 0px 2px 10px 5px #1abc9c;\n"
"  color: #000;\n"
"}\n"
"\n"
".QPushButton:after {\n"
"  content: \"\";\n"
"  background: #1abc9c;\n"
"  display: block;\n"
"  position: absolute;\n"
"  padding-top: 300%;\n"
"  padding-left: 350%;\n"
"  margin-left: -20px !important;\n"
"  margin-top: -120%;\n"
"  opacity: 0;\n"
"  transition: all 0.8s\n"
"}\n"
"\n"
".QPushButton:active:after {\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  opacity: 1;\n"
"  transition: 0s\n"
"}\n"
".QPushButton:focus { outline:0; }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.ankara)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(266, 640, 101, 51))
        self.pushButton_4.setStyleSheet(".QPushButton{\n"
"  height: 100%;\n"
"  width: 100%;\n"
"  display: flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  background: linear-gradient(to left, #606c88 , #3f4c6b);\n"
"  font-family: \'Oswald\', sans-serif;\n"
"}\n"
"\n"
".QPushButton{\n"
"  text-align: center;\n"
"  text-transform: uppercase;\n"
"  cursor: pointer;\n"
"  font-size: 14px;\n"
"  letter-spacing: 4px;\n"
"  position: relative;\n"
"  background-color: #16a085;\n"
"  border: none;\n"
"  color: #fff;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  text-align: center;\n"
"  transition-duration: 0.4s;\n"
"  overflow: hidden;\n"
"  box-shadow: 0 5px 15px #193047;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #fff;\n"
"  box-shadow: 0px 2px 10px 5px #1abc9c;\n"
"  color: #000;\n"
"}\n"
"\n"
".QPushButton:after {\n"
"  content: \"\";\n"
"  background: #1abc9c;\n"
"  display: block;\n"
"  position: absolute;\n"
"  padding-top: 300%;\n"
"  padding-left: 350%;\n"
"  margin-left: -20px !important;\n"
"  margin-top: -120%;\n"
"  opacity: 0;\n"
"  transition: all 0.8s\n"
"}\n"
"\n"
".QPushButton:active:after {\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  opacity: 1;\n"
"  transition: 0s\n"
"}\n"
".QPushButton:focus { outline:0; }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.mersin)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(376, 640, 101, 51))
        self.pushButton_5.setStyleSheet(".QPushButton{\n"
"  height: 100%;\n"
"  width: 100%;\n"
"  display: flex;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  background: linear-gradient(to left, #606c88 , #3f4c6b);\n"
"  font-family: \'Oswald\', sans-serif;\n"
"}\n"
"\n"
".QPushButton{\n"
"  text-align: center;\n"
"  text-transform: uppercase;\n"
"  cursor: pointer;\n"
"  font-size: 14px;\n"
"  letter-spacing: 4px;\n"
"  position: relative;\n"
"  background-color: #16a085;\n"
"  border: none;\n"
"  color: #fff;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  text-align: center;\n"
"  transition-duration: 0.4s;\n"
"  overflow: hidden;\n"
"  box-shadow: 0 5px 15px #193047;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #fff;\n"
"  box-shadow: 0px 2px 10px 5px #1abc9c;\n"
"  color: #000;\n"
"}\n"
"\n"
".QPushButton:after {\n"
"  content: \"\";\n"
"  background: #1abc9c;\n"
"  display: block;\n"
"  position: absolute;\n"
"  padding-top: 300%;\n"
"  padding-left: 350%;\n"
"  margin-left: -20px !important;\n"
"  margin-top: -120%;\n"
"  opacity: 0;\n"
"  transition: all 0.8s\n"
"}\n"
"\n"
".QPushButton:active:after {\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  opacity: 1;\n"
"  transition: 0s\n"
"}\n"
".QPushButton:focus { outline:0; }")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.adana)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(70, 100, 361, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(29)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(147, 241, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(170, 180, 281, 251))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(80, 430, 151, 171))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(240, 450, 141, 131))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(62)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(420, 420, 61, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0,80);\n"
"border-top-left-radius : 150px")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arka/Resimler/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(52, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.exit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hava Durumu"))
        self.label_2.setText(_translate("Form", "HAVA DURUMU "))
        self.pushButton_2.setText(_translate("Form", "İSTANBUL"))
        self.pushButton_3.setText(_translate("Form", "ANKARA"))
        self.pushButton_4.setText(_translate("Form", "MERSİN"))
        self.pushButton_5.setText(_translate("Form", "ADANA"))
        self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/season.png);")


    def exit(self):
        exit()
    def mersin(self):
        url = "https://www.ntv.com.tr/mersin-hava-durumu"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        toplam = []
        for i in soup.find_all("p", {"class": "hava-durumu--detail-data-item-bottom-temp-max"}):
            toplam.append(i.text)
        mesaj = []
        for e in soup.find_all("div", {"class": "container hava-durumu--detail-data-item-bottom-desc"}):
            mesaj.append(e.text)
        durum = str(mesaj[0]).strip("\r\n\r\n ")
        self.label_4.setText("MERSİN")
        self.label_7.setText(toplam[0])
        self.label_6.setStyleSheet("border-image: url(:/arka/Resimler/temperature.png);")
        if durum == "Parçalı Bulutlu" or durum == "Az Bulutlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloudy (1).png);")
        elif durum == "Kar Yağışı" or durum == "Yoğun Kar Yağışı" or durum == "Karla Karışık Yağmur":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/snow.png);")
        elif durum == "Yağmurlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/rain.png);")
        elif durum == "Güneşli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/sun.png);")
        elif durum == "Sisli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/fog.png);")
        else:
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloud.png);")

    def adana(self):
        url = "https://www.ntv.com.tr/adana-hava-durumu"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        toplam = []
        for i in soup.find_all("p", {"class": "hava-durumu--detail-data-item-bottom-temp-max"}):
            toplam.append(i.text)
        mesaj = []
        for e in soup.find_all("div", {"class": "container hava-durumu--detail-data-item-bottom-desc"}):
            mesaj.append(e.text)
        durum = str(mesaj[0]).strip("\r\n\r\n ")
        self.label_4.setText("ADANA")
        self.label_7.setText(toplam[0])
        self.label_6.setStyleSheet("border-image: url(:/arka/Resimler/temperature.png);")
        if durum == "Parçalı Bulutlu" or durum == "Az Bulutlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloudy (1).png);")
        elif durum == "Kar Yağışı" or durum == "Yoğun Kar Yağışı" or durum == "Karla Karışık Yağmur":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/snow.png);")
        elif durum == "Yağmurlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/rain.png);")
        elif durum == "Güneşli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/sun.png);")
        elif durum == "Sisli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/fog.png);")
        else:
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloud.png);")
    def ankara(self):
        url = "https://www.ntv.com.tr/ankara-hava-durumu"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        toplam = []
        for i in soup.find_all("p", {"class": "hava-durumu--detail-data-item-bottom-temp-max"}):
            toplam.append(i.text)
        mesaj = []
        for e in soup.find_all("div", {"class": "container hava-durumu--detail-data-item-bottom-desc"}):
            mesaj.append(e.text)
        durum = str(mesaj[0]).strip("\r\n\r\n ")
        self.label_4.setText("ANKARA")
        self.label_7.setText(toplam[0])
        self.label_6.setStyleSheet("border-image: url(:/arka/Resimler/temperature.png);")
        if durum == "Parçalı Bulutlu" or durum == "Az Bulutlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloudy (1).png);")
        elif durum == "Kar Yağışı" or durum == "Yoğun Kar Yağışı" or durum == "Karla Karışık Yağmur":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/snow.png);")
        elif durum == "Yağmurlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/rain.png);")
        elif durum == "Güneşli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/sun.png);")
        elif durum == "Sisli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/fog.png);")
        else:
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloud.png);")
    def istanbul(self):
        url = "https://www.ntv.com.tr/istanbul-hava-durumu"
        mert = requests.get(url)
        sayfa_icerigi = mert.content
        soup = BeautifulSoup(sayfa_icerigi, "html.parser")
        toplam = []
        for i in soup.find_all("p", {"class": "hava-durumu--detail-data-item-bottom-temp-max"}):
            toplam.append(i.text)
        mesaj = []
        for e in soup.find_all("div", {"class": "container hava-durumu--detail-data-item-bottom-desc"}):
            mesaj.append(e.text)
        durum = str(mesaj[0]).strip("\r\n\r\n ")
        self.label_4.setText("İSTANBUL")
        self.label_7.setText(toplam[0])
        self.label_6.setStyleSheet("border-image: url(:/arka/Resimler/temperature.png);")
        if durum == "Parçalı Bulutlu" or durum == "Az Bulutlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloudy (1).png);")
        elif durum == "Kar Yağışı" or durum == "Yoğun Kar Yağışı" or durum == "Karla Karışık Yağmur":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/snow.png);")
        elif durum == "Yağmurlu":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/rain.png);")
        elif durum == "Güneşli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/sun.png);")
        elif durum == "Sisli":
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/fog.png);")
        else:
            self.label_5.setStyleSheet("border-image: url(:/arka/Resimler/cloud.png);")
import resim_rc
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(pencere)
    pencere.show()
    sys.exit(app.exec_())