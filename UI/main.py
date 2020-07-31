import sys
import os
import time

path = os.getcwd()
sys.path.insert(1,path + '/functions/')

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize, QDir, Qt,QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QBrush, QIcon, QPainter, QColor, QPen,QCursor
from KelimeTurkceMi import kelime_Turkcemi
from dogruYanlisKelime import dogruBilinenYanlislar
from SimurgKelimeTemizle import metin_temizle,kelime_temizle
from SimurgCumleOlustur import cumle_olustur
from EtkenEdilgen import etkenEdilgen
from OzneYuklemIliskisi import ozneYuklem
from EsAnlamli import *

class Kelime:
    def __init__(self, indis, kelime, renk, cumleindis,cumlerenk):
        self.indis = indis
        self.kelime = kelime
        self.renk = renk
        self.cumleindis=cumleindis
        self.cumlerenk=cumlerenk

class Cumle:
    def __init__(self, indis, cumle, renk):
        self.indis = indis
        self.cumle = cumle
        self.renk = renk


class MainWindow(QMainWindow):
    fileName=""
    sonuc_text=[]
    sonuc_cumle_text=[]
    RedColor=QColor(255, 0, 0)
    OrangeColor=QColor(110, 125, 0)
    YellowColor=QColor(250, 230, 94)
    PurpleColor=QColor(0, 0, 255)
    WhiteColor=QColor(0, 0, 0) #Darkmode için (255,255,255) olmalıdır.
    TransparentColor=QColor("transparent")
    olusturuldu=0

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
        self.showLegand()
        
        self.fileName = None

    def showLegand(self):
        self.label = QLabel(' - Doğru Bilinen Yanlış Kelimeler', self)
        self.label.move(47,606)
        self.label.adjustSize()

        self.label2 = QLabel(' - Etken-Edilgen Kuralına Uymayan Cümleler', self) 
        self.label2.move(47,626)
        self.label2.adjustSize()

        self.label3 = QLabel('- Kelime Kökeni Türkçe Mi? ', self) 
        self.label3.move(580,606)
        self.label3.adjustSize()

        self.label4 = QLabel('- Özne Yüklem Uyumsuzluğu', self) 
        self.label4.move(580,626)
        self.label4.adjustSize()
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red))
        painter.drawRect(10, 610, 30,10)

        painter2 = QPainter(self)
        painter2.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter2.setBrush(QBrush(Qt.yellow))
        painter2.drawRect(10, 630, 30,10)

        painter3 = QPainter(self)
        painter3.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter3.setBrush(QBrush(Qt.blue))
        painter3.drawRect(540, 610, 30,10)

        painter4 = QPainter(self)
        painter4.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter4.setBrush(QBrush(Qt.darkYellow))
        painter4.drawRect(540, 630, 30,10)
    
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
       
        self.text.textChanged.connect(self.sonucDizisiOlustur)
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
        geek_list = ["Lütfen Bir Fonksiyon Seçin","Doğru Bilinen Yanlışlar","Kelime Türkçe Mi?","Özne-Yüklem Uyumsuzluğu","Etken Edilgen Çatı Uyumsuzluğu"]
        self.combo_box.addItems(geek_list)
        self.combo_box.setCurrentIndex(0)
        self.combo_box.currentIndexChanged.connect(self.selectionchange)
    
    def selectionchange(self,i):
        print ("Items in the list are :")
        for count in range(self.combo_box.count()):
            print (self.combo_box.itemText(count))
        print ("Current index",i,"selection changed ",self.combo_box.currentText())

        if(i==1):#DogruYanlişFonksiyonu
            self.outputText.clear()
            self.dogruYanlis()
        if(i==2):#KelimeTurkcemiFonksiyonu
            self.outputText.clear()
            self.turkceKelime()
        if(i==3):#OzneYüklemUyumsuzluğu
            self.outputText.clear()
            self.ozneYuklemKontrol()
        if(i==4):#EtkenEdilgenÇatıUyumsuzluğu
            self.outputText.clear()
            self.etkenEdilgenKontrol()
    
    islem_goren_metin_dizisi={}

    def etkenEdilgenKontrol(self):
        if(self.olusturuldu==0):
            self.sonucDizisiOlustur()
        count=0
        for i in self.sonuc_cumle_text:
            print(str(i.cumle)+str(i.indis))
            s=etkenEdilgen(i.cumle) 
            if s==0:
                if(self.sonuc_cumle_text[count].renk==self.TransparentColor):
                    self.sonuc_cumle_text[count].renk=self.TransparentColor
            else:
                self.sonuc_cumle_text[count].renk=self.YellowColor
                for z in self.sonuc_text:
                    if(z.cumleindis==count):
                        z.cumlerenk=self.YellowColor
                    print(z.cumlerenk)

            count=count+1
        self.ciktiYazdir() 

    def ozneYuklemKontrol(self):
        if(self.olusturuldu==0):
            self.sonucDizisiOlustur()
        count=0
        for i in self.sonuc_cumle_text:
            print(str(i.cumle)+str(i.indis))
            s=ozneYuklem(i.cumle) 
            if s==0:
                if(self.sonuc_cumle_text[count].renk==self.TransparentColor):
                    self.sonuc_cumle_text[count].renk=self.TransparentColor
            else:
                self.sonuc_cumle_text[count].renk=self.OrangeColor
                for z in self.sonuc_text:
                    if(z.cumleindis==count):
                        z.cumlerenk=self.OrangeColor
                    print(z.cumlerenk)

            count=count+1
        self.ciktiYazdir()       

    def turkceKelime(self):
        self.outputText.clear()
        metin_dizisi=[]
        metin_dizisi.clear()
        islenmemis_metin=[]

        islenmemis_metin=str(self.text.document().toPlainText()).split(" ")
        metin=self.text.document().toPlainText()
        metin_dizisi=metin_temizle(metin)

        if(self.olusturuldu==0):
            self.sonucDizisiOlustur()

        count=0
        for i in self.sonuc_text:
            s=kelime_Turkcemi(i.kelime) 
            if s in "True" :
                if(self.sonuc_text[count].renk==self.WhiteColor):
                    self.sonuc_text[count].renk=self.WhiteColor
            else:
                self.sonuc_text[count].renk=self.PurpleColor 
            count=count+1
        self.ciktiYazdir()    

    def dogruYanlis(self):
        self.outputText.clear()
        
        metin_dizisi=[]
        metin_dizisi.clear()

        islenmemis_metin=str(self.text.document().toPlainText()).split(" ")
        metin=self.text.document().toPlainText()
        metin_dizisi=metin_temizle(metin)
        
        count=0
        if(self.olusturuldu==0):
            self.sonucDizisiOlustur()
        for i in self.sonuc_text:
            if str(dogruBilinenYanlislar(kelime_temizle(i.kelime))) in "None" :
                if(self.sonuc_text[count].renk==self.WhiteColor):
                    self.sonuc_text[count].renk=self.WhiteColor
            else:
                self.sonuc_text[count].renk=self.RedColor
                self.sonuc_text[count].kelime=str(dogruBilinenYanlislar(kelime_temizle(i.kelime)))
            count=count+1
        self.ciktiYazdir()

    
    def sonucDizisiOlustur(self):
        self.sonuc_text.clear()
        self.sonuc_cumle_text.clear()
        self.olusturuldu=1
        sayacCumle=0
        sayacKelime=0
        cumle_isle=cumle_olustur(self.text.document().toPlainText())
        for i in cumle_isle:
            self.sonuc_cumle_text.append(Cumle(sayacCumle,i,self.WhiteColor))
            x=str(i).split(" ")
            for j in x:
                self.sonuc_text.append(Kelime(sayacKelime,j,self.WhiteColor,sayacCumle,self.TransparentColor))
                sayacKelime=sayacKelime+1
                
            sayacCumle=sayacCumle+1
       
        #metin_isle=str(self.text.document().toPlainText()).split(" ")
        
        #for a in metin_isle:
         #   self.sonuc_text.append(Kelime(sayac,a,self.WhiteColor))
          #  sayac=sayac+1
    
    def ciktiYazdir(self):
        self.outputText.clear()
        for a in self.sonuc_text:
            
            self.outputText.setTextBackgroundColor(a.cumlerenk)
            self.outputText.setTextColor(a.renk)
            self.outputText.insertPlainText(a.kelime+" ")   
     
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #def
    mainWin = MainWindow()
    mainWin.move(400,250)

    splash = QSplashScreen(QPixmap(path+'/image/clutch.jpg'))
    splash.resize(1030,700)
    splash.move(400,210)
    splash.show()
    QTimer.singleShot(1500, splash.close)
    mainWin.show()
    sys.exit( app.exec_() )