from trnlp import *
import array as arr


girilen_Kelime = open("dosya.txt", "r")
veri_seti = open("uniq_final_final.txt","r")
veri_satiri = veri_seti.readlines()

nesne_Ilk = TrnlpToken()
nesne_Ilk.settext(girilen_Kelime.read())

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
        print(son_Kelime + " türkçedir.")

    else:
        print(son_Kelime + " türkçe değildir.")