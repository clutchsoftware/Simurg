  
  
import os

"""
recursive

INPUT: bileşik olduğu duüşünülen kelime
OUTPUT: parçalara ayrılmış kelimenin listesi

dizinde bulunan kelime kesildiktens sonra kalan kelime öbeğinden hiç anlamlı birşey çıkmıyorsa kesilen
parça yanlış kesimliştir

fonkisyon verilen kelimenin sonundan başlayarak anlamlı kelimeler aramaya başlıyor.
buldu kelimeyi ana kelimeden çıkartıp kalınından anlamı kelime bulmya çalışıyor.
bulamazsa aramayı devam ettiriyor.



"""
print(os.getcwd())
f = open("data/out_of_digits_dataset.txt", "r",encoding="utf-8")
lines = f.readlines()

def kelime_bul (kelime):
    for line in lines:
        if(kelime == line[0:(len(line)-2) ]):
            return True
    return False


def kelime_ayir (kelime):

    kelimeler = list()
    aranacak_harf_sayisi = 4;
    x=0
    for x in range(aranacak_harf_sayisi,len(kelime)+1):
        
        aranacak = kelime[len(kelime)-x : len(kelime)]
        print(aranacak)
        
        for line in lines:
            x=x+1
            if(aranacak == line[0:(len(line)-2) ]):
                print("eslesme sagalndı :"+aranacak+", len():"+str(len(aranacak))+" line="+line[0:(len(line)-2) ])
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
                

                
                
    print("x= ",x)
    return kelimeler

son_liste = kelime_ayir("evetv")
son_liste.reverse()
print(son_liste)

"""

v2

  
  
import os


recursive

INPUT: bileşik olduğu duüşünülen kelime
OUTPUT: parçalara ayrılmış kelimenin listesi

dizinde bulunan kelime kesildiktens sonra kalan kelime öbeğinden hiç anlamlı birşey çıkmıyorsa kesilen
parça yanlış kesimliştir

fonkisyon verilen kelimenin sonundan başlayarak anlamlı kelimeler aramaya başlıyor.
buldu kelimeyi ana kelimeden çıkartıp kalınından anlamı kelime bulmya çalışıyor.
bulamazsa aramayı devam ettiriyor.




v2


print(os.getcwd())
f = open("data/out_of_dataset.txt", "r",encoding="utf-8")
lines = f.readlines()


def kelime_bul (kelime):
    for line in lines:
        if(kelime == line[0:(len(line)-1) ]):
            return True
    return False

def kelime_ayir (kelime):

    kelimeler = list()
    aranacak_harf_sayisi = 4;
    x=0
    for x in range(aranacak_harf_sayisi,len(kelime)+1):
        
        aranacak = kelime[len(kelime)-x : len(kelime)]
        print(aranacak)
        
        for line in lines:
            x=x+1
            if(aranacak == line[0:(len(line)-1) ]):
                print("eslesme sagalndı :"+aranacak+", len():"+str(len(aranacak))+" line="+line[0:(len(line)-1) ])
                kelime = kelime[0:(len(kelime)-len(aranacak))]
                
                if(len(kelime) > 0):
                    kalan_kelime_listesi = kelime_ayir_fonk(kelime)
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
                

                
                
    print("x= ",x)
    return kelimeler

def kelime_ayir_fonk(ayrilacak_kelime):
    kelimes = list()
    if( kelime_bul(ayrilacak_kelime) ):
        kelimes.append(ayrilacak_kelime)
        return kelimes
    else:
        return kelime_ayir( ayrilacak_kelime )

deger = kelime_ayir_fonk("denemeörnek")

print(deger)

"""
