from trnlp import *
def es_anlamli_kelimeler(kelime):
    kelimes=list()
    kelime=kelime.lower()
    kelimeson=TrnlpWord()
    kelimeson.setword(kelime)
    kelime=kelimeson.get_stem
    #print(kelime)
    dosya = open('data/es_anlamli_Kelimeler.txt', 'r',encoding="utf-8") 
    Lines = dosya.readlines()
    count=0 
    for line in Lines:

        tindex=line.index("\t")
        if(line[0:tindex]==kelime):
            kelimes.append(line.strip()[tindex+1:len(line)-1])
            #print("Line{}: {}".format(count,line.strip()[tindex+1:len(line)-1]))
            count=count+1
    return kelimes