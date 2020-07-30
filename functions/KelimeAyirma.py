import os
from pathlib import Path

"""
recursive

asil işi yapan kelim_ayir_fonk() ve onun çağırdığı kelime_ayir()

INPUT: bileşik olduğu duüşünülen kelime
OUTPUT: parçalara ayrılmış kelimenin listesi

dizinde bulunan kelime kesildiktens sonra kalan kelime öbeğinden hiç anlamlı birşey çıkmıyorsa kesilen
parça yanlış kesimliştir

fonkisyon verilen kelimenin sonundan başlayarak anlamlı kelimeler aramaya başlıyor.
buldu kelimeyi ana kelimeden çıkartıp kalınından anlamı kelime bulmya çalışıyor.
bulamazsa aramayı devam ettiriyor.



"""

f = open("data/out_of_dataset.txt", "r",encoding="utf-8")
lines = f.readlines()


def kelime_bul (kelime):
    for line in lines:
        if(kelime == line[0:(len(line)-1) ]):
            return True
    return False

def kelime_ayir (kelime):

    kelimeler = list()
    nums = [9,7,5,3,2]
    for aranacak_harf_sayisi in nums:
        if(kelime_bul(kelime)):
            kelimeler.append(kelime)
            return kelimeler


        
        
        for x in range(aranacak_harf_sayisi,len(kelime)+1):
            
            aranacak = kelime[len(kelime)-x : len(kelime)]
            print(aranacak)
            
            for line in lines:
                
                if(aranacak == line[0:(len(line)-1) ]):
                    print("eslesme sagalndı :"+aranacak+", len():"+str(len(aranacak))+" line="+line[0:(len(line)-1) ])
                    kelime = kelime[0:(len(kelime)-len(aranacak))]
                    
                    if(len(kelime) > 0):
                        kalan_kelime_listesi = kelime_ayir(kelime)
                        if( len(kalan_kelime_listesi) == 0 ):
                            kelime = kelime + aranacak
                        else:
                            kelimeler.append(aranacak)
                            
                            for k in kalan_kelime_listesi:
                                if k not in kelimeler:
                                    kelimeler.append(k)
                                    kelime = kelime[0:len(kelime)-len(k)]
                                    
                            
                            x = aranacak_harf_sayisi 
                            if(len(kelime)==0):
                                return kelimeler
                    else:
                        kelimeler.append(aranacak)
                        return kelimeler
                    

                    

    return kelimeler

def kelime_ayir_fonk(ayrilacak_kelime):
    kelimes = list()
    kelimes = kelime_ayir(ayrilacak_kelime)
    if(len(kelimes) == 0):
        kelimes.append(ayrilacak_kelime)
        return kelimes
    kelimes.reverse()
    return kelimes

         
def bol(kelime,key):
    lis= list()
    lis=kelime.split(key)
    if("" in lis):
        lis.remove("")
    
    return lis



def cumle_kelime_ayir(cumle):
    cumle_list = bol(cumle," ")
    rett = list()
    for i in range(len(cumle_list)):
        temp = kelime_ayir_fonk(cumle_list[i])
        for t in temp:
            rett.append(t)
    return rett


"""
kelim_e = "neyseiyiakşamlar"
listtt = kelime_ayir_fonk(kelim_e)

cumlee = ""
for i in listtt:
    cumlee = cumlee + " " + i
print(listtt)

print(cumlee)
"""