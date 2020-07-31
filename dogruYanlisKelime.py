from SimurgCumleOlustur import cumle_olustur
from SimurgKelimeTemizle import kelime_temizle, metin_temizle 
import pandas as pd 
import csv
import os
path=os.getcwd()
def dogruBilinenYanlislar(kelime):
    #Data set import
    data = pd.read_csv(path+"/data/dogruBilinenYanlislar.csv") 
    data_yanlis_listesi = list(data["yanlis"])
    data_dogru_listesi = list(data["dogru"])

    list_kelime = list(kelime)

    def kelime_benzeri():
        if kelime_temizle(kelime.lower()) in data_yanlis_listesi:
            return (kelime_temizle(kelime.lower()))
        return "None"

    bulunan_kelimeler = kelime_benzeri()

    def indeks_bul():
        counter = 0
        indeks_listesi = []
        for i in data_yanlis_listesi:
            if bulunan_kelimeler in i:
                indeks_listesi.append(counter)
            counter += 1
        return indeks_listesi

    indeks_listesi = indeks_bul() #indeks listesini hem data_yanlis_listesi hem de data_dogru_listesi için kullanabilisin.

    dict = {}
    for i in range(len(indeks_listesi)):
        dict[data_yanlis_listesi[indeks_listesi[i]]] = data_dogru_listesi[indeks_listesi[i]]

    temp_string = dict.get(bulunan_kelimeler)
    return(temp_string)


#cevap = dogruBilinenYanlislar("acenta.")
#print(cevap)