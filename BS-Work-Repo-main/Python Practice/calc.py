# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

num = 0.0
newNum = 0.0
sumIt = 0.0
sumAll = 0.0
operator = ""

opVar = False

class Ui_MainWindow(object):
    
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(269, 308)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(60, 130, 41, 41))
        self.five.setObjectName("five")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(60, 180, 41, 41))
        self.two.setObjectName("two")
        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(110, 230, 41, 41))
        self.dot.setObjectName("dot")
        self.dot.clicked.connect(self.clicked)
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(160, 180, 41, 41))
        self.multiply.setObjectName("multiply")
        self.eql = QtWidgets.QPushButton(self.centralwidget)
        self.eql.setGeometry(QtCore.QRect(210, 230, 41, 41))
        self.eql.setObjectName("eql")
        self.eql.clicked.connect(self.clicked)
        self.slash = QtWidgets.QPushButton(self.centralwidget)
        self.slash.setGeometry(QtCore.QRect(160, 230, 41, 41))
        self.slash.setObjectName("slash")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(60, 80, 41, 41))
        self.eight.setObjectName("eight")
        self.brac2 = QtWidgets.QPushButton(self.centralwidget)
        self.brac2.setGeometry(QtCore.QRect(210, 130, 41, 41))
        self.brac2.setObjectName("brac2")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(210, 80, 41, 41))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.clicked)
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(160, 80, 41, 41))
        self.minus.setObjectName("minus")

        self.line = QtWidgets.QLineEdit(self.centralwidget)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(40)
        self.line.setFont(font)
        self.line.resize(230, 70)

        """
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 241, 61))
        self.lcdNumber.setObjectName("lcdNumber") """
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(110, 180, 41, 41))
        self.three.setObjectName("three")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(110, 80, 41, 41))
        self.nine.setObjectName("nine")
        self.brac1 = QtWidgets.QPushButton(self.centralwidget)
        self.brac1.setGeometry(QtCore.QRect(210, 180, 41, 41))
        self.brac1.setObjectName("brac1")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 180, 41, 41))
        self.one.setObjectName("one")
        self.Zero = QtWidgets.QPushButton(self.centralwidget)
        self.Zero.setGeometry(QtCore.QRect(10, 230, 41, 41))
        self.Zero.setObjectName("Zero")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(110, 130, 41, 41))
        self.six.setObjectName("six")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 80, 41, 41))
        self.seven.setObjectName("seven")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(160, 130, 41, 41))
        self.plus.setObjectName("plus")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 130, 41, 41))
        self.four.setObjectName("four")
        self.double_zero = QtWidgets.QPushButton(self.centralwidget)
        self.double_zero.setGeometry(QtCore.QRect(60, 230, 41, 41))
        self.double_zero.setObjectName("double_zero")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 269, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicked(self):
        self.line.setText(num)
        self.update()   

    def update(self):
        self.line.adjustSize()     
    
    def Num(self):
        global num
        global newNum
        global opVar

        sender = self.sender()

        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)
        else:
            self.line.setText(setNum)
            opVar = False


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.five.setText(_translate("MainWindow", "5"))
        self.five.setShortcut(_translate("MainWindow", "5"))
        self.two.setText(_translate("MainWindow", "2"))
        self.dot.setText(_translate("MainWindow", "."))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.eql.setText(_translate("MainWindow", "="))
        self.slash.setText(_translate("MainWindow", "/"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.brac2.setText(_translate("MainWindow", "("))
        self.clear.setText(_translate("MainWindow", "C"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.three.setText(_translate("MainWindow", "3"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.brac1.setText(_translate("MainWindow", ")"))
        self.one.setText(_translate("MainWindow", "1"))
        self.Zero.setText(_translate("MainWindow", "0"))
        self.six.setText(_translate("MainWindow", "6"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.four.setText(_translate("MainWindow", "4"))
        self.double_zero.setText(_translate("MainWindow", "00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

