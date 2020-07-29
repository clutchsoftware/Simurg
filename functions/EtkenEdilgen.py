"""
    Yüklem durumundaki fiilin gösterdiği işi doğrudan doğruya öznenin kendisi yapıyorsa FİİL ETKEN çatılı demektir.
    Yani fiilin gerçek öznesi varsa(gizli özne olmaması lazım) ve “l,n” çatı ekini almamışsa FİİL ETKENDİR.
    Bir fiil “l,n” çatı ekini almışsa ve eylemin kim tarafından yapıldığı belli değilse o FİİL EDİLGENDİR. 
    Edilgen fiillere “kim tarafından” sorusunu yönelttiğimizde cevap alamayız.

    Yani yapılacak fonksiyon hem fiilin "l, n" çatı ekini almış olması hem de eylemin kim tarafından yapıldığı belli olduğu
    cümleleri belirleyip, düzeltmesigerekiyor.
    Örnek:
            Evi güzelce temizledi. (Etken, özne; O)
            Ev temizlendi.         (Edilgen, özne belli değil.)
            Evi güzelce temizlendi.(WTF?)

            Kadın, bulaşığı yıkadı.(Etken, özne; Kadın)
            Kadın, bulaşığı yıkandı.(Fiil edilgen ancak özne belli. HATA!)

            Sınavın iptal edileceğini söyledi.
            Sınavın iptal edileceğini söylendi.

            İSTİSNA
            Bahçedeki araçlar birer birer yıkandı.
            Bahçedeki araçlar görevli tarafından yıkandı. ÖZNE VAR FİİL -L/-N EKİ ALMIŞ.


            KÜTÜPHANE HATASI:
            text = "Bütün sokaklar temizlendi." #KÜTÜPHANE HATASI BÜTÜN KELİMESİNİ ÖZEL KELİME OLARAK ALIYOR!

"""
from trnlp import TrnlpWord
from SimurgKelimeTemizle import kelime_temizle

#text = "Ayberk tüm sınav sorularını çözdü."
#text = "Sınav sorularının tümü çözüldü."
#text = "Kitaptaki yanlışlar düzeltildi."
#text = "Fırından yüz adet ekmek alındı."
text = "Ahmet fırından yüz adet ekmek alındı."

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
    
fiil_listesi = fiil_yazdir()
#print("fiil listesi", fiil_listesi)


def fiil_kisi_ekini_bul(fiil_listesi): # şuan fiil liste halinde dönüyor ve tek elemandan oluşuyor. 2 elemanda sıkıntı olursa değiştir!
    fiil_koku = ""
    ek_bulunan_fiil = ""
    kisi_ekleri = ["{Ke1t}", "{Ke2t}", "{Ke3t}", "{Ke1ç}", "{Ke2ç}", "{Ke3ç}", "{İe1t}", "{İe2t}", "{İe3t}", "{İe1ç}", "{İe2ç}", "{İe3ç}"]
    for i in kisi_ekleri:
        if fiil_listesi != None:
            for j in fiil_listesi:
                if i in j:
                    fiil_koku = i
                    ek_bulunan_fiil = j
                else:
                    ek_bulunmayan_fiil = j
        else:
            ek_bulunan_fiil = ""
            ek_bulunmayan_fiil = ""
            fiil_koku = ""
    return ek_bulunan_fiil, fiil_koku, ek_bulunmayan_fiil

ek_bulunan_fiil, fiil_koku, ek_bulunmayan_fiil= fiil_kisi_ekini_bul(fiil_listesi)
#print("Kişi Ekleri Ek Bulunan Fill: ", ek_bulunan_fiil," Fiilin Eki: ", fiil_koku)
#print("Ek Bulunmayan Fiil: ", ek_bulunmayan_fiil)


def ozne_var_mi():
    """"
    return : özne bulunan cümleyi belirler.
    """
    ozne_bulunan_kelime = []
    filtre = ["özel", "zamir", "Ke", "İe"]
    counter = 0
    for i in ayrilmis_kelimeler:
        for j in filtre:
            i = str(i)
            if j in i:
                #print("isim buldu")
                #print("isim bulunan indeks:", str(counter))
                ozne_bulunan_kelime.append(ayrilmis_kelimeler[counter])
            
        counter += 1
    #return ayrilmis_kelimeler[counter-1]
    return ozne_bulunan_kelime

# fiil olan kelimelerin indeksleri
def fiil_olan_kelime_indeksleri():
    """"
    return : fiil olan kelimeleri liste halinde döndürür.
    """
    fiil_indeksleri = []
    fiil = "fiil"
    counter = 0
    for i in ayrilmis_kelimeler:
        i = str(i)
        if fiil in i:
            #print("fiil bulunan indeks:", str(counter))
            fiil_indeksleri.append(counter)
        counter += 1

    if len(fiil_indeksleri) > 0 :
        return fiil_indeksleri
    

fiil_indeksleri = fiil_olan_kelime_indeksleri()
#print("fiillerin bulundukları indeks: ", fiil_indeksleri)

"""
# trnlp kütüphanesi tarafından etiketlenmiş fiil değil. < 'çöz(fiil)+dü{GçDi}[2_1]' fiil kelimesinde l var > SADECE FİİL KELİMESİ OLMASI LAZIM.
def l_n_cati_eki(eksiz_fiil):
    cati_eki_l = "l"
    cati_eki_n = "n"
    if (cati_eki_l or cati_eki_n) in eksiz_fiil:
        uyarı = "Fiil -l, -n eklerini almıştır."
    else:
        uyarı = "Fiil -l, -n eklerini almamıştır."
    return uyarı
"""


def l_n_cati_eki(text):
    text_list = text.split(" ")
    cati_eki_l = "l"
    cati_eki_n = "n"
    for i in text_list:
        if (cati_eki_l or cati_eki_n) in i:
            uyarı = "Fiil -l, -n eklerini almıştır."
            l_n_flag = True
        else:
            uyarı = "Fiil -l, -n eklerini almamıştır."
            l_n_flag = False
    return uyarı, l_n_flag



#ek_kontrolu = l_n_cati_eki(ek_bulunan_fiil)
ek_kontrolu, l_n_flag = l_n_cati_eki(text)
#print(ek_bulunmayan_fiil," ",ek_kontrolu)

ozne_bulunan_kelime = ozne_var_mi()
if len(ozne_bulunan_kelime) > 0:
    #print("Bu cümlede özne bulunmaktadır!", "Bulunan filtre ekleri: ",ozne_bulunan_kelime)
    ozne_flag = True
else:
    ozne_flag = False
    #print("ÖZNE YOKTUR!")

"""
ÖZNE YOK VE FİİL -L/-N EKLERİNİ ALDIYSA: EDİLGEN
ÖZNE VAR VE FİLL -L/-N EKLERİNİ ALMADIYSA: ETKEN
BİZİM FONKSİYON: EDİLGEN GİBİ BAŞLAYIP ETKEN ŞEKİLDE BİTEN CÜMLEYİ BULACAK.
    YANİ İÇİNDE ÖZNE BULUNDURUP FİİL KÖKÜNDE -L/-N EKLERİ BULUNAN CÜMLELER.
"""
print("Örnek Cümle: ", text)

if ozne_flag == False and l_n_flag == True:
    print(text, " (EDİLGEN)")
elif ozne_flag == True and l_n_flag == False:
    print(text, " (ETKEN)")
elif ozne_flag == True and l_n_flag == True:
    print(text, " (ÇATI BAKIMINDAN UYUMSUZDUR!)")