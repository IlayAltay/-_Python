#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication,QLineEdit,QLabel,QTableWidget
from PyQt5.QtCore import QCoreApplication
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):               
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        linee=QLineEdit(self)
        linee.move(50,0)

        label1=QLabel('Status',self)
        label1.move(50,130)

        btn1=QPushButton('GO',self)
        btn1.move(50, 80) 
        btn1.clicked.connect(lambda: self.gorun(label1))
        
        tableWidget = QTableWidget(12, 3, self)
        tableWidget.move(300,100)
        tableWidget.setMinimumHeight(500)
        tableWidget.setMinimumWidth(600)
        tableWidget.setHorizontalHeaderLabels(["Num", "Adress", "Value"])
        tableWidget.setAlternatingRowColors(123)


        self.setGeometry(300, 300, 700, 900)
        self.setWindowTitle('Quit button')    
        self.show()
        
    def gorun(self,fr):
        print('GO!')
        fr.setText('Ready')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
