from PyQt5 import QtCore, QtGui, QtWidgets
import random,sys


class Ui_MainWindow(object):
    
    def __init__(self):
        self.wins= 0
        self.loss= 0
        self.tie= 0
        self.random_num=0
        self.gen_choice=0


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 350)
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
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.Exit.setObjectName("Exit")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(120, 80, 75, 23))
        self.Play.setObjectName("Play")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(50, 130, 47, 13))
        self.Result.setObjectName("Result")
        self.Result.adjustSize()
        self.Result_Overall = QtWidgets.QLabel(self.centralwidget)
        self.Result_Overall.setGeometry(QtCore.QRect(50, 190, 47, 13))
        self.Result_Overall.setObjectName("Result_Overall")
        self.Result_Overall.adjustSize()
        self.Choices = QtWidgets.QLabel(self.centralwidget)
        self.Choices.setGeometry(QtCore.QRect(50, 150, 47, 13))
        self.Choices.setObjectName("Choices")
        self.Choices.adjustSize()
        self.Stats = QtWidgets.QLabel(self.centralwidget)
        self.Stats.setGeometry(QtCore.QRect(50, 170, 47, 13))
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
       

        ##self.Play_Again.clicked.connect(self.Actions)
        self.Play.clicked.connect(self.Actions)
        self.Exit.clicked.connect(self.quit)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Option_label.setText(_translate("MainWindow", "Choose from the options :"))
        self.Option_box.setItemText(0, _translate("MainWindow", "Rock"))
        self.Option_box.setItemText(1, _translate("MainWindow", "Paper"))
        self.Option_box.setItemText(2, _translate("MainWindow", "Scissors"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Play.setText(_translate("MainWindow", "Play"))
        self.Result.setText(_translate("MainWindow", "Result "))
        self.Result_Overall.setText(_translate("MainWindow", "Result Overall "))
        self.Stats.setText(_translate("MainWindow", "Stats : Win  Loss  Tie "))
        self.Choices.setText(_translate("MainWindow", " Player Choice & Generated Choice"))
        self.Choices.adjustSize()
        self.Stats.adjustSize()
        self.Result.adjustSize()
        self.Result_Overall.adjustSize()
    
    def quit(self):
        sys.exit()
    
   
    
    def Actions(self):
        x=str(self.Option_box.currentText())
        self.Result.setText(str(x))
        self.random_num = random.randrange(1,4)
        self.Stats.setText(str(self.random_num))

        if x == "Rock":
            self.gen_choice= self.random_num
            
            ##self.Result.setText("Inside if")
            ##self.Result.adjustSize()
            ##print("if condition R Main")
            if self.gen_choice==1:
                self.Result.setText("The match was tied ")
                self.Result.adjustSize()  
                self.tie+=1
                #print(" \n The match was tied")
                self.Result.setText("The match was tied ")
                self.Result.adjustSize()  
            elif self.gen_choice==2:
                self.loss+=1
                ##print(" \n You lost this round")
                self.Result.setText("You lost this round ")
                self.Result.adjustSize()
            elif self.gen_choice==3:
                self.wins+=1
                ##print(" \n You won this round")
                self.Result.setText("You won this round ")
                self.Result.adjustSize()
        elif x == "Paper":
            self.gen_choice= self.random_num
            if self.gen_choice==1:
                self.wins+=1
                #print(" \n You won this round")
                self.Result.setText("You won this round ")
                self.Result.adjustSize()
            elif self.gen_choice==2:
                self.tie+=1
                #print(" \n The match was tied")
                self.Result.setText("The match was tied ")
                self.Result.adjustSize()
            elif self.gen_choice==3:
                self.loss+=1
                #print(" \n You lost this round")
                self.Result.setText("You lost this round ")
                self.Result.adjustSize()
        elif x =="Scissors":
            self.gen_choice= self.random_num
            if self.gen_choice==1:
                self.loss+=1
                ##print(" \n You lost this round")
                self.Result.setText("You lost this round ")
                self.Result.adjustSize()
            elif self.gen_choice==2:
                self.wins+=1
                ##print(" \n You won this round")
                self.Result.setText("You won this round ")
                self.Result.adjustSize()
            elif self.gen_choice==3:
                self.tie+=1
                #print(" \n The match was tied")
                self.Result.setText("The match was tied ")
                self.Result.adjustSize()

        if self.gen_choice==1:
            self.gen_choice='Rock'
            ##print("R last condition ")
        elif self.gen_choice==2:
            self.gen_choice='Paper'
            ##print("P last condition ")
        elif self.gen_choice==3:
            self.gen_choice='Scissor'
            ##print("S last condition ") 

        if self.wins == self.loss:
            self.Result_Overall.setText(" You are Tied overall with the tin can !!")
        elif self.wins > self.loss:
            self.Result_Overall.setText(" You are Winning overall against the tin can !!")
        elif self.wins < self.loss:
            self.Result_Overall.setText(" You are Loosing overall against the tin can !!")


        self.Choices.setText(" For this round" + " Player choice : " + str(x) + " Computer Generated : " + str(self.gen_choice) )
        
        self.Stats.setText(' wins =' + str(self.wins) + ' Loss = ' + str(self.loss) + ' Tie = ' + str(self.tie))
        self.Stats.adjustSize()
        self.Choices.adjustSize()
        self.Result_Overall.adjustSize()
        

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
