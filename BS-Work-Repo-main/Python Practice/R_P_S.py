# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'R_P_S.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random,sys


wins=0
loss=0
tie=0
random_num=0
gen_choice=0
Ch='y'


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 307)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Option_label = QtWidgets.QLabel(self.centralwidget)
        self.Option_label.setGeometry(QtCore.QRect(40, 30, 131, 21))
        self.Option_label.setObjectName("Option_label")
        self.Option_box = QtWidgets.QComboBox(self.centralwidget)
        self.Option_box.setGeometry(QtCore.QRect(180, 30, 69, 22))
        self.Option_box.setObjectName("Option_box")
        self.Option_box.addItem("")
        self.Option_box.addItem("")
        self.Option_box.addItem("")
        self.Play_Again = QtWidgets.QPushButton(self.centralwidget)
        self.Play_Again.setGeometry(QtCore.QRect(60, 190, 75, 23))
        self.Play_Again.setObjectName("Play_Again")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.Exit.setObjectName("Exit")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(120, 80, 75, 23))
        self.Play.setObjectName("Play")
        self.Stats = QtWidgets.QLabel(self.centralwidget)
        self.Stats.setGeometry(QtCore.QRect(50, 130, 47, 13))
        self.Stats.setObjectName("Stats")
        self.Stats.adjustSize()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
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
        self.Option_label.setText(_translate("MainWindow", "Choose from the options :"))
        self.Option_box.setItemText(0, _translate("MainWindow", "Rock"))
        self.Option_box.setItemText(1, _translate("MainWindow", "Paper"))
        self.Option_box.setItemText(2, _translate("MainWindow", "Scissors"))
        self.Play_Again.setText(_translate("MainWindow", "Play Again"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.Stats.setText(_translate("MainWindow", "Stats : Win  Loss  Tie "))
        self.Stats.adjustSize()
    
    def rpsgen():
        random_num = random.randrange(1,3)
        ##print ("Working")
        return random_num
    
    
    def actions():
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

