import sys
import os
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
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter, QColor, QPen,QCursor
path = os.getcwd()
sys.path.insert(1,path + '/functions/')
from dogruYanlisKelime import dogruBilinenYanlislar
from SimurgKelimeTemizle import metin_temizle
from EsAnlamli import *

class MainWindow(QMainWindow):
    fileName=""
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(1080, 720))    
        self.setWindowTitle("Simurg") 
        self.setWindowIcon(QIcon(path+'/image/simurgMainLogo.png')) 
        labelImage = QLabel(self)
        pixmap = QPixmap(path+'/image/simurglogo.png')
        labelImage.setPixmap(pixmap) 
        labelImage.resize(100,100) 
        labelImage.move(460,5)   
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
        self.text.move(10,60) #1.para sol sağ 2. para alt-üst
        self.text.resize(525,450)
       
        self.text.textChanged.connect( #yazıldıkça veriyi çek.
            lambda: print(self.text.document().toPlainText()))
        self.text.selectionChanged.connect(self.handleSelectionChanged)
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.showMenu)

    def handleSelectionChanged(self):
        cursor = self.text.textCursor()
        self.select_start = cursor.selectionStart()
        self.select_end = cursor.selectionEnd()

        print ("Selection start: %d end: %d" % 
           (cursor.selectionStart(), cursor.selectionEnd()))
        string=str(self.text.document().toPlainText())
        print("\033[1;31m"+string[cursor.selectionStart():cursor.selectionEnd()]+"\033[0m")
        word=string[cursor.selectionStart():cursor.selectionEnd()]
        self.selected_word=string[cursor.selectionStart():cursor.selectionEnd()]
        redColor = QColor(255, 0, 0)
        blue = QColor(0, 0, 255)

    def showMenu(self,pos):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction("Default")
        acts = list()
        es_anlamlilar = list()
        es_anlamlilar = es_anlamli_kelimeler(self.selected_word)
        for i in es_anlamlilar:
            acts.append(contextMenu.addAction(i))

        action = contextMenu.exec(self.mapToGlobal(pos))
        """
        for i in range(len(acts)):
            if acts[i] == action:
                print(es_anlamlilar[i])"""

    def textareaSimurg(self):
        self.outputText = QTextEdit(self)
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
            self.outputText.clear()
            self.dogruYanlis()
    

    def dogruYanlis(self):
        self.outputText.clear()
        islem_goren_metin_dizisi=[]
        metin_dizisi=[]
        metin_dizisi.clear()
        islenmemis_metin=str(self.text.document().toPlainText()).split(" ")
        metin=self.text.document().toPlainText()
        metin_dizisi=metin_temizle(metin)
        count=0
        for i in metin_dizisi:
            
            islem_goren_metin_dizisi.append(str(dogruBilinenYanlislar(i))+" ")
    
            if str(dogruBilinenYanlislar(i)) in "None" :
                black = QColor(0, 0, 0)
                self.outputText.setTextColor(black)
                self.outputText.insertPlainText(islenmemis_metin[count]+" ")
            else:
                redColor = QColor(255, 0, 0)
                self.outputText.setTextColor(redColor)
                self.outputText.insertPlainText(str(dogruBilinenYanlislar(i))+" ")
            count=count+1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #def
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )