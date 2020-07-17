  
  
f = open("../data/out_of_digits_dataset.txt", "r")
lines = f.readlines()
kelime = "eme"
kelimelerbacıden
kelime_uzunluğu = len(kelime)
print(kelime_uzunluğu)
print("basladi")
"""
recursive

dizinde bulunan kelime kesildiktens sonra kalan kelime öbeğinden hiç anlamlı birşey çıkmıyorsa kesilen
parça yanlış kesimliştir

"""
kelimeler = list()

for x in range(kelime_uzunluğu+1):
    
    aranacak = kelime[kelime_uzunluğu-x : kelime_uzunluğu]
    print(aranacak)
    isHave = False
    
    for line in lines:
        
        
        if(aranacak == line[0:len(line)-2 ]):
            
            kelime = kelime[0:kelime_uzunluğu-x]
            kelimeler.append(aranacak)
            isHave=True
            x=0
            break
    
    


    
        
        

    
        
print(kelimeler)
    
