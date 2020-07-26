import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
                             QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
                             QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton)

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.setStyleSheet("background-color: white;") 
        self.setMinimumSize(QSize(1080, 720))    
        self.setWindowTitle("Simurg") 
        self.choose_file_button()
        self.textareaMain()
        self.textareaSimurg()
        self.selectItem()
        self.chooseSimurgFunciton()

    def chooseSimurgFunciton(self):
        pybutton = QPushButton('Fonksiyonu Uygula', self)
        pybutton.resize(150,32)
        pybutton.move(460, 5)


    def choose_file_button(self):
        pybutton = QPushButton('Dosya Seç', self)
        pybutton.clicked.connect(self.chooseFile)
        pybutton.resize(100,32)
        pybutton.move(10, 5)

    def chooseFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        print('Clicked Pyqt button.')

    def textareaMain(self):
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Ana yazı buraya gelecek.\n")
        self.b.move(10,60) #1.para sol sağ 2. para alt-üst
        self.b.resize(525,450)

    def textareaSimurg(self):
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("Simurg sonucu buraya gelecek. Altı çizili bir şekilde.\n")
        self.b.move(545,60) #1.para sol sağ 2. para alt-üst
        self.b.resize(525,450)

    def selectItem(self):
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(150,5,300,30)
        geek_list = ["Lütfen Bir Fonksiyon Seçin","Kelime Türkçe Mi?","Doğru Bilinen Yanlışlar","Özne-Yüklem İlişkisi"]
        self.combo_box.addItems(geek_list)
        self.combo_box.setCurrentIndex(0)
        self.combo_box.currentIndexChanged.connect(self.selectionchange)
    
    def selectionchange(self,i):
        print ("Items in the list are :")
        for count in range(self.combo_box.count()):
            print (self.combo_box.itemText(count))
        print ("Current index",i,"selection changed ",self.combo_box.currentText())
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #def
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )