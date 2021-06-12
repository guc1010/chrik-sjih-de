# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Python\测试题\kraihmjenh.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# 界面和逻辑

from PyQt5 import QtCore, QtGui, QtWidgets
from dekhoh import *
deghauh=0
jixtop=0
toptuaih=0
syenx='未选'



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1130, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1130, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1130, 830))
        MainWindow.setBaseSize(QtCore.QSize(1130, 830))
        MainWindow.setToolTipDuration(-5)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Hdekanh = QtWidgets.QTextBrowser(self.centralwidget)
        self.Hdekanh.setGeometry(QtCore.QRect(20, 20, 491, 561))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.Hdekanh.setFont(font)
        self.Hdekanh.setObjectName("Hdekanh")
        self.Hdekanh.setText(demiuk[0]['dekanh'])
        self.Hkrexsek = QtWidgets.QTextBrowser(self.centralwidget)
        self.Hkrexsek.setGeometry(QtCore.QRect(530, 110, 581, 471))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.Hkrexsek.setFont(font)
        self.Hkrexsek.setObjectName("Hkrexsek")
        self.Hsyenx = QtWidgets.QTextBrowser(self.centralwidget)
        self.Hsyenx.setGeometry(QtCore.QRect(690, 20, 121, 71))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.Hsyenx.setFont(font)
        self.Hsyenx.setObjectName("Hsyenx")
        self.Hsyenx.setText(str(syenx))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(830, 30, 161, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Htopqanh = QtWidgets.QTextBrowser(self.centralwidget)
        self.Htopqanh.setGeometry(QtCore.QRect(990, 20, 121, 71))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.Htopqanh.setFont(font)
        self.Htopqanh.setObjectName("Htopqanh")
        self.GA = QtWidgets.QPushButton(self.centralwidget)
        self.GA.setGeometry(QtCore.QRect(20, 610, 191, 71))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(28)
        self.GA.setFont(font)
        self.GA.setObjectName("GA")
        self.GA.clicked.connect(lambda:self.syenxA())
        self.GB = QtWidgets.QPushButton(self.centralwidget)
        self.GB.setGeometry(QtCore.QRect(240, 610, 191, 71))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(28)
        self.GB.setFont(font)
        self.GB.setObjectName("GB")
        self.GB.clicked.connect(lambda:self.syenxB())
        self.GC = QtWidgets.QPushButton(self.centralwidget)
        self.GC.setGeometry(QtCore.QRect(470, 610, 191, 71))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(28)
        self.GC.setFont(font)
        self.GC.setObjectName("GC")
        self.GC.clicked.connect(lambda:self.syenxC())
        self.GD = QtWidgets.QPushButton(self.centralwidget)
        self.GD.setGeometry(QtCore.QRect(700, 610, 191, 71))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(28)
        self.GD.setFont(font)
        self.GD.setObjectName("GD")
        self.GD.clicked.connect(lambda:self.syenxD())
        self.Hjixtop = QtWidgets.QLCDNumber(self.centralwidget)
        self.Hjixtop.setGeometry(QtCore.QRect(190, 710, 151, 61))
        self.Hjixtop.setObjectName("Hjixtop")
        self.Hjixtop.display(jixtop)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 720, 161, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.Htoptuaih = QtWidgets.QLCDNumber(self.centralwidget)
        self.Htoptuaih.setGeometry(QtCore.QRect(570, 710, 151, 61))
        self.Htoptuaih.setObjectName("Htoptuaih")
        self.Htoptuaih.display(toptuaih)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 720, 161, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Hcungx = QtWidgets.QLCDNumber(self.centralwidget)
        self.Hcungx.setGeometry(QtCore.QRect(950, 710, 151, 61))
        self.Hcungx.setObjectName("Hcungx")
        self.Hcungx.display(cungx)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(820, 720, 121, 41))
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Ggraxqjitde = QtWidgets.QPushButton(self.centralwidget)
        self.Ggraxqjitde.setGeometry(QtCore.QRect(930, 610, 181, 71))
        self.Ggraxqjitde.clicked.connect(self.graxqjitde)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setPointSize(28)
        self.Ggraxqjitde.setFont(font)
        self.Ggraxqjitde.setObjectName("Ggraxqjitde")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试题"))
        self.GA.setText(_translate("MainWindow", "A"))
        self.GB.setText(_translate("MainWindow", "B"))
        self.GC.setText(_translate("MainWindow", "C"))
        self.GD.setText(_translate("MainWindow", "D"))
        self.label_1.setText(_translate("MainWindow", "已答题数"))
        self.label_2.setText(_translate("MainWindow", "答对题数"))
        self.label_3.setText(_translate("MainWindow", "总题数"))
        self.Ggraxqjitde.setText(_translate("MainWindow", "下一题"))
        self.label_4.setText(_translate("MainWindow", "您的答案"))
        self.label_5.setText(_translate("MainWindow", "正确答案"))
    
    def graxqjitde(self):
        global deghauh
        global cungx
        global jixtop
        global toptuaih
        deghauh += 1
        jixtop += 1
        self.Hjixtop.display(jixtop)
        self.Htoptuaih.display(toptuaih)
        self.Hsyenx.clear()
        self.Htopqanh.clear()
        if deghauh<cungx:
            self.Hdekanh.setText(demiuk[deghauh]['dekanh'])
            self.GA.setEnabled(True)
            self.GB.setEnabled(True)
            self.GC.setEnabled(True)
            self.GD.setEnabled(True)
            self.Hkrexsek.clear()
        else:
            self.Hdekanh.setText('测试结束！')
            self.Hkrexsek.setText('正确率为：%f%%'%(100*toptuaih/cungx))
            self.Ggraxqjitde.setEnabled(False)

    def phuanh(self):
        global deghauh
        global jixtop
        global toptuaih
        if syenx==demiuk[deghauh]['topqanh']:
            toptuaih += 1
        self.Hkrexsek.setText(demiuk[deghauh]['krexsek'])
        self.GA.setEnabled(False)
        self.GB.setEnabled(False)
        self.GC.setEnabled(False)
        self.GD.setEnabled(False)
        self.Hsyenx.setText(syenx)
        self.Htopqanh.setText(demiuk[deghauh]['topqanh'])

    def syenxA(self):
        global syenx
        syenx = 'A'
        self.phuanh()
    def syenxB(self):
        global syenx
        syenx = 'B'
        self.phuanh()
    def syenxC(self):
        global syenx
        syenx = 'C'
        self.phuanh()
    def syenxD(self):
        global syenx
        syenx = 'D'
        self.phuanh()