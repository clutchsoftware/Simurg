import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton,QTextEdit
from PyQt5.QtCore import QSize  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
                             QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
                             QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QMenu,QToolBar)

from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
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
        self.setMinimumSize(QSize(1030, 650))
        self.setWindowTitle("Simurg") 
        self.toolbar_init()
        self.simurgSetIcon()
        self.textareaMain()
        self.textareaSimurg()
        self.selectItem()
        self.chooseSimurgFunciton()
        
        self.fileName = None
    
    def simurgSetIcon(self):
        self.setWindowIcon(QIcon(path+'/image/simurg.png')) 
        labelImage = QLabel(self)
        pixmap = QPixmap(path + '/image/simurg.png')
        labelImage.setPixmap(pixmap) 
        labelImage.resize(100,100) 
        labelImage.move(492,270)  

    def toolbar_init(self):
        text=QPlainTextEdit()
        outputText = QTextEdit()

        # Ana başlık
        file_toolbar = QToolBar("Dosya İşlemleri")
        file_menu = self.menuBar().addMenu("&Dosya İşlemleri") 

        # Dosya Aç
        open_file_action = QAction("Dosya Aç", self) 
        open_file_action.setStatusTip("Dosya Aç") 
        open_file_action.triggered.connect(self.chooseFile) 
        file_menu.addAction(open_file_action) 
  
        # Kaydet
        file_toolbar.addAction(open_file_action)
        save_file_action = QAction("Kaydet", self) 
        save_file_action.triggered.connect(self.file_save) 
        file_menu.addAction(save_file_action) 
        file_toolbar.addAction(save_file_action) 
  
        # Farklı Kaydet
        saveas_file_action = QAction("Farklı Kaydet", self) 
        saveas_file_action.triggered.connect(self.file_saveas) 
        file_menu.addAction(saveas_file_action) 
        file_toolbar.addAction(saveas_file_action) 

    def update_title(self): 
        self.setWindowTitle("%s - PyQt5 Notepad" %(os.path.basename(self.path)  
                                                  if self.path else "Untitled"))
                
    def _save_to_path(self, path): 
        text = self.text.toPlainText() 
        try: 
            with open(path, 'w') as f: 
                f.write(text) 

        except Exception as e: 
            self.dialog_critical(str(e)) 
  
        else: 
            self.path = path 
            self.update_title() 
            
    def file_save(self): 
        if self.fileName is None: 
            return self.file_saveas() 

        self._save_to_path(self.fileName) 
  

    def file_saveas(self): 
        fileName, _ = QFileDialog.getSaveFileName(self, "Save file", "",  
                             "Text documents (*.txt);All files (*.*)") 

        if not fileName: 
            return

        self._save_to_path(fileName) 


    def chooseSimurgFunciton(self):
        pybutton = QPushButton('Fonksiyonu Uygula', self)
        pybutton.resize(150,32)
        pybutton.move(725, 40)

    def chooseFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.text.setPlainText(open(self.fileName).read())
        if self.fileName:
            print(self.fileName)

    def textareaMain(self):
        self.text = QPlainTextEdit(self)
        self.text.move(10,90) #1.para sol sağ 2. para alt-üst
        self.text.resize(480,500)
       
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
        acts = list()
        es_anlamlilar = list()
        es_anlamlilar = es_anlamli_kelimeler(self.selected_word)
        

        if(len(es_anlamlilar) > 0):
            for i in es_anlamlilar:
                        acts.append(contextMenu.addAction(i))
        
        else:
            acts.append(contextMenu.addAction("-----------------------------"))
            acts.append(contextMenu.addAction("Eş anlamlı kelime bulunamadı."))
            acts.append(contextMenu.addAction("-----------------------------"))
        action = contextMenu.exec(self.mapToGlobal(pos))

        old_text = self.text.document().toPlainText()
        for i in range(len(acts)):
            if acts[i] == action:
                new_text = old_text[0:self.select_start] + es_anlamlilar[i] + old_text[self.select_end:len(old_text)]
                self.text.document().setPlainText(new_text)
                print(es_anlamlilar[i])
        """
        for i in range(len(acts)):
            if acts[i] == action:
                print(es_anlamlilar[i])"""

    def textareaSimurg(self):
        self.outputText = QTextEdit(self)
        self.outputText.move(540,90) #1.para sol sağ 2. para alt-üst
        self.outputText.resize(480,500)

    def selectItem(self):
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(75,40,300,31)
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
                black = QColor(255, 255, 255)
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