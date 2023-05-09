# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\moham\BreastCancerDeskTop\View\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1100)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1920, 1100))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(1070, 280, 301, 451))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("Background-color:rgba(255,255,255);\n"
"box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 250, 431, 521))
        self.label_2.setStyleSheet("Background-image:url(:/Images/Hand.png);\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(1090, 290, 161, 61))
        font = QtGui.QFont()
        font.setFamily("12 1px Calibri")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 255));\n"
"color:rgb(0,0,0,200);\n"
"font: 75 22pt bold 1px\"Calibri\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.emailfield = QtWidgets.QLineEdit(self.bgwidget)
        self.emailfield.setGeometry(QtCore.QRect(1090, 410, 241, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.emailfield.setFont(font)
        self.emailfield.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgpa(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82 , 101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.emailfield.setText("")
        self.emailfield.setObjectName("emailfield")
        self.passwordfield = QtWidgets.QLineEdit(self.bgwidget)
        self.passwordfield.setGeometry(QtCore.QRect(1090, 520, 241, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.passwordfield.setFont(font)
        self.passwordfield.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:2px solid rgpa(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82 , 101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordfield.setObjectName("passwordfield")
        self.login = QtWidgets.QPushButton(self.bgwidget)
        self.login.setGeometry(QtCore.QRect(1150, 580, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton#login{\n"
"    Background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"} \n"
"QPushButton#login:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(254, 81, 171, 0.8);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#login:hover{\n"
"    background-color:rgba(254, 81, 171, 0.8)\n"
"}")
        self.login.setObjectName("login")
        self.label_5 = QtWidgets.QPushButton(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(990, 640, 341, 51))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,0);text-decoration: underline;QLabel:hover;color:rgb(0, 0, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(800, 475, 500, 50))
        self.error.setStyleSheet("font: 20pt bold \"MS Shell Dlg 2\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Log In"))
        self.emailfield.setPlaceholderText(_translate("Dialog", "User Name"))
        self.passwordfield.setPlaceholderText(_translate("Dialog", "Password"))
        self.login.setText(_translate("Dialog", "L o g I n"))
        self.label_5.setText(_translate("Dialog", "Don\'t have an account"))