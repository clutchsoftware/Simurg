"""
Kelimeler sonunda istenmeyen noktalama işaretlerini silen fonksiyon.
ASCII table
 33-47   -> ! - /
 58-64   -> : - @
 91-96   -> [ - '
 123-126 -> { - ~
"""
filtre1 = [i for i in range(33,48,1)]
filtre2 = [i for i in range(58,65,1)]
filtre3 = [i for i in range(91,97,1)]
filtre4 = [i for i in range(123,127,1)]
metin_listesi = []
temizlenmis_metin = []


def remove_at(kelime, indeks):
    """
    parametre: indeks(int) ve kelime(str)
    return: belirlenen indeks temizleyerek kelimeyi geri döndürür. (str)
    """
    return kelime[:indeks] + kelime[indeks+1:]

def kelime_temizle(kelime): 
    temp_kelime = ""
    indeks = 0
    for i in kelime:
        #ord() string convert ascii, chr() ascii convert string
        if ord(i) in filtre1:
            temp_kelime = remove_at(kelime, indeks)

        if ord(i) in filtre2:
            temp_kelime = remove_at(kelime, indeks)
            
        if ord(i) in filtre3:
            temp_kelime = remove_at(kelime, indeks)
            
        if ord(i) in filtre4:
            temp_kelime = remove_at(kelime, indeks)

        indeks = indeks + 1
    if len(temp_kelime) > 0:
        return temp_kelime
    else:
        return kelime

def metin_temizle(metin):
    metin_listesi = metin.split(" ")
    for i in metin_listesi:
        temizlenmis_metin.append(kelime_temizle(i).lower())
    return temizlenmis_metin

"""!!!!
if 32 in filtre1 or filtre2:
    print("true")

    0 or 0 = 1 ekrana true yazdırır.
"""
