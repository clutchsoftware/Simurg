from trnlp import *
import array as arr


f = open("dosya.txt", "r")
veri_seti = open("uniq_final_final.txt","r")
satir = veri_seti.readlines()

obj = TrnlpToken()
obj.settext(f.read())

liste = list()
liste2 = list()
for x in  obj.wordtoken:
    obj2 = TrnlpWord()
    obj2.setword(x)
    a = obj2.get_stem

    if (obj2.get_stem == ''):
        a = x

    isTurkish = False 

    for lines in satir:
        if(a==lines[0:len(lines)-1 ]):
            isTurkish = True
            break
    
    if isTurkish :
        print(a + " türkçedir.")

    else:
        print(a + " türkçe değildir.")



            
            

        
    










"""import turkishnlp
from turkishnlp import detector
obj = detector.TurkishNLP()
obj.create_word_set()



f = open("dosya.txt", "r")
print(obj.is_turkish(f.read()))"""