import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton,QTextEdit
from PyQt5.QtCore import QSize  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
                             QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
                             QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QMenu)

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QColor, QPen,QCursor

sys.path.insert(1,'/home/tubi/Desktop/SimurgProje/Simurg/functions/')

from dogruYanlisKelime import dogruBilinenYanlislar
from SimurgKelimeTemizle import metin_temizle


class MainWindow(QMainWindow):
    fileName=""
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
        text=QPlainTextEdit()
        outputText = QTextEdit()

    def chooseSimurgFunciton(self):
        pybutton = QPushButton('Fonksiyonu Uygula', self)
        pybutton.resize(150,32)
        pybutton.move(460, 5)


    def choose_file_button(self):
        pybutton = QPushButton('Dosya Sec', self)
        pybutton.clicked.connect(self.chooseFile)
        pybutton.resize(100,32)
        pybutton.move(10, 5)

    def chooseFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.text.setPlainText(open(self.fileName).read())
        if self.fileName:
            print(self.fileName)
        print('Clicked Pyqt button.')

    def textareaMain(self):
        self.text = QPlainTextEdit(self)
        self.text.insertPlainText("Ana yazı buraya gelecek.\n")
        self.text.move(10,60) #1.para sol sağ 2. para alt-üst
        self.text.resize(525,450)
        #yazıldıkça veriyi çek.
        self.text.textChanged.connect(
            lambda: print(self.text.document().toPlainText()))
        self.text.selectionChanged.connect(self.handleSelectionChanged)
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.showMenu)

    def handleSelectionChanged(self):
        cursor = self.text.textCursor()
        print ("Selection start: %d end: %d" % 
           (cursor.selectionStart(), cursor.selectionEnd()))
        string=str(self.text.document().toPlainText())
        print("\033[1;31m"+string[cursor.selectionStart():cursor.selectionEnd()]+"\033[0m")
        word=string[cursor.selectionStart():cursor.selectionEnd()]
        redColor = QColor(255, 0, 0)
        blue = QColor(0, 0, 255)
        #self.outputText.setTextColor(redColor)
        #self.outputText.insertPlainText(" "+word)
        #self.outputText.setTextBackgroundColor(blue)
        #self.outputText.insertPlainText(" selam ")


    def showMenu(self,pos):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction("New")
        openAct = contextMenu.addAction("Open")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(pos))
        if action == quitAct:
            self.close()

    def textareaSimurg(self):
        self.outputText = QTextEdit(self)
        self.outputText.insertPlainText("Simurg sonucu buraya gelecek. Altı çizili bir şekilde.\n")
        self.outputText.move(545,60) #1.para sol sağ 2. para alt-üst
        self.outputText.resize(525,450)

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
        if(i==2):#DogruYanlişFonksiyonu
            metin=self.text.document().toPlainText()
            metin_dizisi=metin_temizle(metin)
            islem_goren_metin_dizisi=[]
            for i in metin_dizisi:
                kelimestr=str(dogruBilinenYanlislar(i))+" "
                islem_goren_metin_dizisi.append(kelimestr)
                if str(dogruBilinenYanlislar(i)) in "None" :
                    black = QColor(0, 0, 0)
                    self.outputText.setTextColor(black)
                    self.outputText.insertPlainText(i+" ")
                else:
                    redColor = QColor(255, 0, 0)
                    self.outputText.setTextColor(redColor)
                    self.outputText.insertPlainText(str(dogruBilinenYanlislar(i))+" ")
            

    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #def
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )