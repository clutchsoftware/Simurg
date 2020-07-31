import re
def cumle_olustur(text):
    """
    parametre:  Cümlelere ayrılacak yazı.(str)
    return:     Cümlelere ayrılmış liste.(list)
    """
    sentences = re.split(r' (?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)', text)
                            
    cumle_listesi = []
    counter = 0
    for stuff in sentences:
        x = stuff.split(".")
        for i in x:
            temp_str = (str(x[counter])+".") 
            temp_str = temp_str.strip()
            cumle_listesi.append(temp_str)
            counter = counter + 1 
        #cumle_listesi.append(stuff)

    cumle_listesi.pop() # cumle_listesi listenin son elemanı '.' olarak kaldığından son elemanı siliyorum.
    #return cumle_listesi
    #soru işareti
    cumle_listesi_soru = []

    for i in cumle_listesi:
        sentences = re.split(r' (?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)', i)
        counter = 0
        for stuff in sentences:
            x = stuff.split("?")
            for i in x:
                temp_str = (str(x[counter])+"?") 
                temp_str = temp_str.strip()
                cumle_listesi_soru.append(temp_str)
                counter = counter + 1 
                #cumle_listesi.append(stuff)
   
    counter = 0
    for i in cumle_listesi_soru:
        temp = i
        if i[-1]=="?" and i[-2]==".":
            #print("soru istareti")
            i = i[:-1]
            cumle_listesi_soru[counter] = i
        counter = counter + 1

    return cumle_listesi_soru


def bol(kelime):
    lis= list()
    x = [".","!","?"] # ayrılması gerekenler
    i=0
    while( len(kelime) > 0 and i<len(kelime)):

        if( len(kelime) > 0 and kelime[0] == " "):
                kelime = kelime[1:len(kelime)]

        if ( kelime[i] in x):
            lis.append(kelime[0:i+1])
            kelime=kelime[i+1:len(kelime)]
            i=0
            continue

        i=i+1


    if("" in lis):
        lis.remove("")

    return lis


text = "Merhaba nasılsın? Sağ ol, iyiyim. Herkes nereye gitti? Ben burda tek kaldım. Ben de bu konular hakkında bilgim yok. Biraz araştırma yapman lazım."

#print(cumle_olustur(text))
