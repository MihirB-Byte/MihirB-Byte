# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtd_basics.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(340, 290, 101, 31))
        self.button1.setObjectName("button1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(300, 130, 111, 41))
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button1.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "button"))
        self.label1.setText(_translate("MainWindow", "Label in qtd"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tut on Pyqt5")
        msg.setText("this is the main text")
        msg.setIcon(QMessageBox.Warning) ### shows other messeages as well like critical, question,information ###  
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Open | QMessageBox.Save) ### other options available as well###
        msg.setDefaultButton(QMessageBox.Save) ### set to Highlights the default button###
        msg.setInformativeText("informative text ") #Extra line of information#
        msg.buttonClicked.connect(self.popup_button)

        msg.setDetailedText("details")


        x= msg.exec_()
        
    def popup_button(self,i):
        print(i.text())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

