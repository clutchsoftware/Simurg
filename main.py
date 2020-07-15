from SimurgCumleOlustur import cumle_olustur
from SimurgKelimeTemizle import kelime_temizle, metin_temizle 
import pandas as pd 
import csv

#Data set import
data = pd.read_csv("data/dogruBilinenYanlislar.csv") 
data_yanlis_listesi = list(data["yanlis"])
data_dogru_listesi = list(data["dogru"])

#text dosyasını okuma.
f = open("text.txt")
ana_metin = f.read()
parcalanmis_ana_metin_listesi = ana_metin.split(" ")
f.close()

#text içeriğini cümlelere ayırıyorum.
cumle_listesi = []
cumle_listesi = cumle_olustur(ana_metin)

#cümle içindeki kelimeleri dataset içinde ara. 
def kelime_benzeri():
    bulunan_kelimeler = []
    cumle_listesi_temp = []
    # data_yanlis_listesi = data["yanlis"]
    for i in range(len(cumle_listesi)):
        cumle_listesi_temp = cumle_listesi[i].split(" ")
        #cumle_listesi_1 = cumle_listesi[0].split(" ")
        #print(len(cumle_listesi_temp))
        cumle_uzunluklari = len(cumle_listesi_temp) #8-13-5
        for i in range(cumle_uzunluklari):
            if kelime_temizle(cumle_listesi_temp[i].lower()) in data_yanlis_listesi:
                bulunan_kelimeler.append(kelime_temizle(cumle_listesi_temp[i].lower()))
    return bulunan_kelimeler

bulunan_kelimeler = kelime_benzeri()

#bulunan kelimelerin dataset içinde indekslerini bul. 
def indeks_bul():
    counter = 0
    indeks_listesi = []
    for i in data_yanlis_listesi:
        for j in bulunan_kelimeler:
            if j in i:
                indeks_listesi.append(counter)
        counter += 1
    return indeks_listesi

indeks_listesi = indeks_bul() #indeks listesini hem data_yanlis_listesi hem de data_dogru_listesi için kullanabilisin.

#print(data_dogru_listesi[118])

dict = {}
for i in range(len(indeks_listesi)):
    dict[data_yanlis_listesi[indeks_listesi[i]]] = data_dogru_listesi[indeks_listesi[i]]

#print(dict.get("ahpap"))

# Tüm metininden yanlış yazılmış kelimelerin indeks listesini döndüren func
temizlenmis_ana_metin = metin_temizle(ana_metin)
ana_metindede_yanlis_kelime_indeks_listesi = []
def yanlis_kelime_indeksi():
    counter_yanlis_kelime = 0
    for i in temizlenmis_ana_metin:
        for j in data_yanlis_listesi:
            if i == j:
                ana_metindede_yanlis_kelime_indeks_listesi.append(counter_yanlis_kelime)
        counter_yanlis_kelime += 1
    return ana_metindede_yanlis_kelime_indeks_listesi

ana_metindede_yanlis_kelime_indeks_listesi = yanlis_kelime_indeksi()

"""
for i in range(len(ana_metindede_yanlis_kelime_indeks_listesi)):
    temp_string = ""
    temp_string = temizlenmis_ana_metin[ana_metindede_yanlis_kelime_indeks_listesi[i]]
    temp_string = temp_string+" ("+dict.get(temizlenmis_ana_metin[ana_metindede_yanlis_kelime_indeks_listesi[i]])+")"
    temizlenmis_ana_metin[ana_metindede_yanlis_kelime_indeks_listesi[i]] = temp_string
"""

for i in range(len(ana_metindede_yanlis_kelime_indeks_listesi)):
    temp_string = ""
    temp_string = " ("+dict.get(temizlenmis_ana_metin[ana_metindede_yanlis_kelime_indeks_listesi[i]])+")"
    temizlenmis_ana_metin[ana_metindede_yanlis_kelime_indeks_listesi[i]] = temp_string

for i in range(len(ana_metindede_yanlis_kelime_indeks_listesi)):
    parcalanmis_ana_metin_listesi[ana_metindede_yanlis_kelime_indeks_listesi[i]] = parcalanmis_ana_metin_listesi[ana_metindede_yanlis_kelime_indeks_listesi[i]] + str(temizlenmis_ana_metin[ana_metindede_yanlis_kelime_indeks_listesi[i]])

ana_metin_topla = ""
for i in parcalanmis_ana_metin_listesi:
    ana_metin_topla = ana_metin_topla +" "+ i

print(ana_metin)

print(ana_metin_topla.strip())