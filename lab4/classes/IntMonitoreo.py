# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Monitoreo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Cdatos = QtWidgets.QRadioButton(self.groupBox)
        self.Cdatos.setGeometry(QtCore.QRect(20, 30, 141, 17))
        self.Cdatos.setObjectName("Cdatos")


        self.Cparametros = QtWidgets.QRadioButton(self.groupBox)
        self.Cparametros.setGeometry(QtCore.QRect(20, 50, 181, 17))
        self.Cparametros.setObjectName("Cparametros")


        self.reportes = QtWidgets.QRadioButton(self.groupBox)
        self.reportes.setGeometry(QtCore.QRect(20, 70, 82, 17))
        self.reportes.setObjectName("reportes")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 270, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 211, 20))
        self.label_2.setObjectName("label_2")
        self.Ndatos = QtWidgets.QTextBrowser(self.groupBox_2)
        self.Ndatos.setGeometry(QtCore.QRect(40, 60, 111, 31))
        self.Ndatos.setObjectName("Ndatos")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 100, 281, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 211, 20))
        self.label_3.setObjectName("label_3")
        self.minh = QtWidgets.QTextBrowser(self.groupBox_3)
        self.minh.setGeometry(QtCore.QRect(50, 50, 51, 31))
        self.minh.setObjectName("minh")


        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.label_4.setObjectName("label_4")
        self.maxh = QtWidgets.QTextBrowser(self.groupBox_3)
        self.maxh.setGeometry(QtCore.QRect(180, 50, 51, 31))
        self.maxh.setObjectName("maxh")


        self.maxn = QtWidgets.QTextBrowser(self.groupBox_3)
        self.maxn.setGeometry(QtCore.QRect(180, 120, 51, 31))
        self.maxn.setObjectName("maxn")


        self.minn = QtWidgets.QTextBrowser(self.groupBox_3)
        self.minn.setGeometry(QtCore.QRect(50, 120, 51, 31))
        self.minn.setObjectName("minn")


        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 21, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 211, 20))
        self.label_6.setObjectName("label_6")
        self.maxf = QtWidgets.QTextBrowser(self.groupBox_3)
        self.maxf.setGeometry(QtCore.QRect(180, 200, 51, 31))
        self.maxf.setObjectName("maxf")


        self.minf = QtWidgets.QTextBrowser(self.groupBox_3)
        self.minf.setGeometry(QtCore.QRect(50, 200, 51, 31))
        self.minf.setObjectName("minf")


        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 21, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 211, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(150, 60, 21, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(150, 130, 21, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(150, 210, 21, 16))
        self.label_11.setObjectName("label_11")
        self.BMenu = QtWidgets.QPushButton(self.centralwidget)
        self.BMenu.setGeometry(QtCore.QRect(90, 190, 121, 41))
        self.BMenu.setObjectName("BMenu")


        self.Bcdatos = QtWidgets.QPushButton(self.centralwidget)
        self.Bcdatos.setGeometry(QtCore.QRect(100, 400, 121, 41))
        self.Bcdatos.setObjectName("Bcdatos")
                                   def Bcdatos (self):


        self.Btemperaturas = QtWidgets.QPushButton(self.centralwidget)
        self.Btemperaturas.setGeometry(QtCore.QRect(450, 380, 121, 41))
        self.Btemperaturas.setObjectName("Btemperaturas")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Menu"))
        self.Cdatos.setText(_translate("MainWindow", "Captura de datos"))
        self.Cparametros.setText(_translate("MainWindow", "Configuración de parámetros"))
        self.reportes.setText(_translate("MainWindow", "Reportes"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Captura de datos"))
        self.label_2.setText(_translate("MainWindow", "Número de datos que desea capturar"))
        self.label.setText(_translate("MainWindow", "MONITOR DE TEMPERATURA"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parametros de temperatura"))
        self.label_3.setText(_translate("MainWindow", "Temperatura hipotermia"))
        self.label_4.setText(_translate("MainWindow", "Min"))
        self.label_5.setText(_translate("MainWindow", "Min"))
        self.label_6.setText(_translate("MainWindow", "Temperatura normal"))
        self.label_7.setText(_translate("MainWindow", "Min"))
        self.label_8.setText(_translate("MainWindow", "Temperatura fiebre"))
        self.label_9.setText(_translate("MainWindow", "Max"))
        self.label_10.setText(_translate("MainWindow", "Max"))
        self.label_11.setText(_translate("MainWindow", "Max"))
        self.BMenu.setText(_translate("MainWindow", "Aceptar"))
        self.Bcdatos.setText(_translate("MainWindow", "Aceptar"))
        self.Btemperaturas.setText(_translate("MainWindow", "Aceptar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
