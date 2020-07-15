from trnlp import *
def es_anlamli_kelimeler(kelime):
    
    kelime=kelime.lower()
    kelimeson=TrnlpWord()
    kelimeson.setword(kelime)
    kelime=kelimeson.get_stem
    print(kelime)
    dosya = open('kelime-esanlamlisi.txt', 'r') 
    Lines = dosya.readlines()
    count=0 
    for line in Lines:
        tindex=line.index("\t")
        if(line[0:tindex]==kelime):
            print("Line{}: {}".format(count,line.strip()[tindex+1:len(line)-1]))


es_anlamli_kelimeler("zürriyetler")



#a="zurriyet\taasdasd\n"
#tindex=a.index("\t")
#print(a[0:tindex])
#print(a[tindex+1:len(a)-1])