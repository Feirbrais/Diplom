# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 140, 780, 500))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(QFont("Times", 10))

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 10, 25, 25))
        self.pushButton_1.setObjectName("pushButton")
        self.textBrowser.setFont(QFont("Times", 8))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 10, 71, 23))
        self.pushButton.setObjectName("pushButton_1")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 690, 20))
        self.label.setText("")
        self.label.setObjectName("label")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 40, 71, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 40, 690, 20))
        self.label_4.setText(" C:/user/Mihman/Desktop")
        self.label_4.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 110, 30))
        self.label_2.setFont(QFont("Times", 10))
        self.label_2.setText("")
        self.label_2.setAlignment (QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 200, 30))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(QFont("Times", 10))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Файл"))
        self.pushButton_1.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "Папка"))
        self.label_3.setText(_translate("MainWindow", "Результат анализа содержимого:"))
