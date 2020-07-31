import os
from trnlp import *

path = os.getcwd()
veri_seti = open(path + "/data/benzersiz_Kelimeler.txt","r")
veri_satiri=[]
def kelime_Turkcemi(girilen_Kelime):
    veri_seti = open(path + "/data/benzersiz_Kelimeler.txt","r")
    veri_satiri = veri_seti.readlines()

    nesne_Ilk = TrnlpToken()
    nesne_Ilk.settext(girilen_Kelime)

    for aranan_Kelime in  nesne_Ilk.wordtoken:
        nesne_Final = TrnlpWord()
        nesne_Final.setword(aranan_Kelime)
        son_Kelime = nesne_Final.get_stem.lower()

        if (nesne_Final.get_stem == ''):
            son_Kelime = aranan_Kelime

        kelime_Turkcemi = False 

        for gezilen_Satir in veri_satiri:
            if(son_Kelime==gezilen_Satir[0:len(gezilen_Satir)-1 ]):
                kelime_Turkcemi = True
                break
        
    if kelime_Turkcemi :
        veri_satiri.clear()
        return "True"

    else:
        veri_satiri.clear()
        return "False"
