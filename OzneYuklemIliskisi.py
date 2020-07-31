from trnlp import TrnlpWord
from SimurgKelimeTemizle import kelime_temizle


text = "İnsanlar buraya geldiler."
#text = "İnsanlar buraya geldi."
#text = "Birkaç kişiler geldiler."
#text = "Bizimkilerle sizin eve geldim."

def ozneYuklem(text):

    def cumle_ayirici(text):
        ayrilmis_metin = []
        obj = TrnlpWord()
        kelime_listesi = text.split(" ")
        for i in kelime_listesi:
            i = kelime_temizle(i)
            obj.setword(str(i))
            ayrilmis_metin.append(str(obj))
        return ayrilmis_metin
        
    ayrilmis_kelimeler = []    
    ayrilmis_kelimeler = cumle_ayirici(text)
    #print(ayrilmis_kelimeler)

    # -------------FİİL

    def fiil_yazdir():
        """"
        return : fiil olan kelimeleri liste halinde döndürür.
        """
        fiil_listesi = []
        fiil = "fiil"
        counter = 0
        for i in ayrilmis_kelimeler:
            i = str(i)
            if fiil in i:
                #print("fiil bulunan indeks:", str(counter))
                fiil_listesi.append(ayrilmis_kelimeler[counter])
            counter += 1

        if len(fiil_listesi) > 0 :
            return fiil_listesi
        

    fiil = fiil_yazdir()
    #print(fiil)

    def fiil_kisi_ekini_bul(fiil): # şuan fiil liste halinde dönüyor ve tek elemandan oluşuyor. 2 elemanda sıkıntı olursa değiştir!
        fiil_koku = ""
        kisi_ekleri = ["{Ke1t}", "{Ke2t}", "{Ke3t}", "{Ke1ç}", "{Ke2ç}", "{Ke3ç}"]
        for i in kisi_ekleri:
            if not fiil:
                fiil_koku="None"
            else:
                for j in fiil:
                    if i in j:
                        fiil_koku = i
                
        return fiil_koku

    fiil_koku = fiil_kisi_ekini_bul(fiil)
    #print(fiil_koku)

    # -------------İSİM

    def isim_yazdir():
        """"
        return : isim olan kelimeleri liste halinde döndürür.
        """
        isim_listesi = []
        isim = "isim"
        counter = 0
        for i in ayrilmis_kelimeler:
            i = str(i)
            if isim in i:
                #print("isim buldu")
                #print("isim bulunan indeks:", str(counter))
                isim_listesi.append(ayrilmis_kelimeler[counter])
            counter += 1
        #return ayrilmis_kelimeler[counter-1]
        return isim_listesi

    isim = isim_yazdir()
    #print(isim)

    def isim_kisi_eki_cogul_mu(isim):
        cekim_ekleri = ["lar", "ler"]
        isim_koku = ""
        for i in cekim_ekleri:
            for j in isim:
                if i in j:
                    isim_koku = i
        return isim_koku

    isim_koku = isim_kisi_eki_cogul_mu(isim)
    #print(isim_koku)



    #print("İsim çekim eki: {",isim_koku,"} Fill şahıs eki: ",fiil_koku)

    if (isim_koku == "lar" or isim_koku == "ler") and fiil_koku == "{Ke3ç}":
        #print(text," ( Özne-Yüklem arasında ek sorunu vardır. Lütfen değişiklik yapın. )")
        return 1
    else:
        #print(text," ( Özne-Yüklem arasında ek sorunu yoktur. ) ")
        return 0

#print(ozneYuklem(text))