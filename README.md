# Simurg

[![N|Solid](https://github.com/clutchsoftware/Simurg/blob/master/image/simurg.png?raw=true)](https://clutchsoftware.github.io) 

<!--Python için bul (NSOLİD)
#BADGES'ları ekle -->

# ➤ Hepimiz Yazıyoruz
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)]()

Zaman zaman hepimiz yazı yazarız. Bu, kimi zaman bir makale kimi zamansa bir elektronik posta olur. Yazarken kimi yerde bilmeden hatalar yapar, kimi yerdeyse doğru sandığımız yapıları kullanırız. Bu tür durumların önüne geçmek için ise bir <b>yazım yardımcısı</b> gereksinimi hissederiz.

Simurg işte tam da o gereksinimi hissettiğimiz anda metinlerimizi düzenlemek için CLUTCH Yazılım Ekibi tarafından oluşturuldu.

# ➤ Simurg'un Kanatları
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)]()

➤ <b> Temel Fonksiyonlar</b>

* [Eş Anlamlıyı Getir](#Eş-Anlamlıyı-Getir)
* [Doğru Bilinen Yanlışları Gör](#Doğru-Bilinen-Yanlışları-Gör)
* [Kelime Kökeni Sorgula](#Kelime-Kökenini-Sorgula)
* [Etken Edilgen Çatı Uyumsuzluğunu Farket](#Etken-Edilgen-Çatı-Uyumsuzluğunu-Farket)
* [Özne Yüklem İlişkisini Gözden Geçir](#Özne-Yüklem-İlişkisini-Gözden-Geçir)
* [Birleşik Kelimeleri Kopar](#Birleşik-Kelimeleri-Kopar)

➤ <b> Yardımcı Fonksiyonlar</b>
    
* [Simurg Kelime Temizle](#Simurg-Kelime-Temizle)
* [Simurg Cümle Oluştur](#Simurg-Cümle-Oluştur)

## Eş Anlamlıyı Getir
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

>Metinlerimizi oluştururken kelime dağarcığımızın yetersizliği nedeniyle bazı kelimeleri birden fazla kez kullanabiliriz. Bu kullanım fazlalığı ise metin içindeki akışı bozabilir. Bozulan akışı düzeltmek için kelimelerin eş anlamlılarına hakim olmamız gerekir. Bu gereksinimi ortadan kaldırmak için ise Simurg'un **Eş Anlamlıyı Getir** fonksiyonunu geliştirdik. 

![Alt Text](https://github.com/clutchsoftware/clutchsoftware.github.io/blob/master/esanlamli.gif?raw=true)

```python
Örnek metin:
Öğrenci sınavın son sorusundaydı ama ne yapacağı hakkında en ufak fikri yoktu. Öğrenci son bir çırpınış sergileyerek arkadaşıyla göz göze gelmeye çalıştı.
```

```python
from EsAnlamli import es_anlamli_kelimeler

es_anlamli_kelime_listesi = es_anlamli_kelimeler("öğrenci")
print(es_anlamli_kelime_listesi)
```

```python
Output:

['talebe', 'şakirt', 'boşgut', 'mektep çocuğu', 'mektepli', 'okul çocuğu', 'okullu', 'tilmiz']
```

## Doğru Bilinen Yanlışları Gör
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

>Gündelik hayatta konuşurken bizim de fark etmediğimiz bazı kelime veya tamlamalar yanlış olmasına rağmen doğruymuşcasına zihnimize yerleşmiştir. Yanlışlarımızı fark edip doğrularını öğrenmek ve metinlerimizde bu yanlışların önüne geçmek için Simurg'un **Doğru Bilinen Yanlışları Gör** fonksiyonunu geliştirdik.


![Alt Text](https://github.com/clutchsoftware/clutchsoftware.github.io/blob/master/dogrubilinen.gif?raw=true)


```python
Örnek metin:
Eğer acenta hakkı elde edebilirsek işleri yoluna koyabiliriz.
```

```python
from dogruYanlisKelime import dogruBilinenYanlislar

metin = "Eğer acenta hakkı elde edebilirsek işleri yoluna koyabiliriz."
duzeltilmis_metin = dogruBilinenYanlislar(metin)
print(duzeltilmis_metin)
```

```python
Output:
"Eğer acente hakkı elde edebilirsek işleri yoluna koyabiliriz."
```

## Kelime Kökeni Sorgula
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

>Çağımız şartları gereği dilimize birçok yabancı kelime nüfuz etmektedir. Dilimizin benliğini koruma bilincine sahip olmanın ne kadar önemli olduğunun farkındayız. Bu farkındalığı uygulamak için Simurg'un **Kelime Kökeni Sorgula** fonksiyonunu geliştirdik.

![Alt Text](https://github.com/clutchsoftware/clutchsoftware.github.io/blob/master/kelimeturkcemi.gif?raw=true)

```python
Örnek metin:
kayıt - log
```

```python
from KelimeturkceMi import kelime_Turkcemi

kelime = "kayıt"
kelime_turkce_mi = kelime_Turkcemi(kelime)
print(kelime_turkce_mi)

kelime2 = "log"
kelime_turkce_mi_2 = kelime_Turkcemi(kelime2)
print(kelime_turkce_mi_2)

```

```python
Output:
True
False
```

## Etken Edilgen Çatı Uyumsuzluğunu Farket
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

> Farkında olmasakta uzun cümleler kurduğumuzda cümlenin etken edilgen çatı uyumsuzluğunu göz ardı edebiliriz. Bu da bizim anlaşılabilirliği düşük cümleler kurmamıza sebebiyet verir. Cümlelerimizin anlaşılabilirliğini yükseltmek için Simurg'un **Etken Edilgen Çatı Uyumsuzluğunu Farket** fonksiyonunu geliştirdik.

![Alt Text](https://github.com/clutchsoftware/clutchsoftware.github.io/blob/master/etkenedilgen.gif?raw=true)

```python
Örnek metin:
(YANLIŞ) Evden ne kadar erken çıksak da uçağa hareket saatinden önce yetişilemedi.
(DOĞRU) Evden ne kadar erken çıksak da uçağa hareket saatinden önce yetişemedik.
```

```python
from EtkenEdilgen import etkenEdilgen

metin = "Evden ne kadar erken çıksak da uçağa hareket saatinden önce yetişilemedi."
etken_edilgen_uyumu = etkenEdilgen(metin)
print(etken_edilgen_uyumu)

metin2 = "Evden ne kadar erken çıksak da uçağa hareket saatinden önce yetişemedik.."
etken_edilgen_uyumu_2 = etkenEdilgen(metin2)
print(etken_edilgen_uyumu)

```

```python
Output:
1
0
```

## Özne Yüklem İlişkisini Gözden Geçir
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

>Bir topluluk adına veya çoğul konuştuğumuzda özne ve yüklem arasındaki ilişki uyumsuzluğunun gözden geçirilmesi gerekebilir. Çünkü bu tip durumlarda sıklıkla özne yüklem uyumsuzluğu hatası yapılır. Bu hatayı ortadan kaldırmak için Simurg'un **Özne Yüklem İlişkisini Gözden Geçir** fonksiyonunu geliştirdik.

![Alt Text](https://github.com/clutchsoftware/clutchsoftware.github.io/blob/master/ozneyuklem.gif?raw=true)

```python
Örnek metin:
(YANLIŞ) İnsanlar buraya geldiler.
(DOĞRU) İnsanlar buraya geldi.
```

```python
from OzneYuklemIliskisi import ozneYuklem

metin = "İnsanlar buraya geldiler."
ozne_yuklem_uyumu = ozneYuklem(metin)
print(ozne_yuklem_uyumu)

metin2 = "İnsanlar buraya geldi."
ozne_yuklem_uyumu2 = ozneYuklem(metin2)
print(ozne_yuklem_uyumu2)

```

```python
Output:
1
0
```

## Birleşik Kelimeleri Kopar
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)

> Bazen yazılarımızın, metinlerimizin yetişmesi için hızlı yazmaya çalışırız. Bu hız esnasında birleşik olmaması gereken kelimeleri birleşik bir halde yazabiliriz. Bu tür durumlar kimi zaman gözden kaçabilir. Bunların düzeltilmesi için ise Simurg'un **Birleşik Kelimeleri Kopar** fonksiyonunu geliştirdik.

```python
Örnek metin:
(YANLIŞ) TürkçeDoğalDilİşleme
(DOĞRU) Türkçe Doğal Dil İşleme
```

```python
from KelimeAyirma import kelime_ayir_fonk

metin = "TürkçeDoğalDilİşleme"
ayrik_kelime = kelime_ayir_fonk(metin)
print(ayrik_kelime)

```

```python
Output:
['türkçe', 'doğal', 'dil', 'işleme']
 türkçe doğal dil işleme
```

## Simurg Kelime Temizle
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/grass.png)

> Simurg yapısı gereği hazır fonksiyonlara ihtiyaç duymaktadır. Bu hazır fonksiyonlarda bir tanesi olan **Simurg Kelime Temizle** kelimelerin başında veya sonunda bulunan noktalama işaretlerini temizleyerek kullanıma hazır kelimleri döndürür.

```python
from SimurgKelimeTemizle import kelime_temizle

kelime = "acikhack."
temiz_kelime = kelime_temizle(kelime)
print(temiz_kelime)

```

```python
Output:
"acikhack"
```


## Simurg Cümle Oluştur
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/grass.png)

> Simurg yapısı gereği hazır fonksiyonlara ihtiyaç duymaktadır. Bu hazır fonksiyonlarda bir tanesi olan **Simurg Cümle Oluştur** metnin içinde bulunan noktalama işaretleri ile ayrılmış kelimeleri ayırarak her bir kelimeyi listeye ekleyip bir kelime listesi oluşturur.

```python
from SimurgCumleOlustur import cumle_olustur

metin = "Acikhack'in yapmış olduğu yarışmaya katılacağız. Bunun için çok heyecanlıyız."
cumle_listesi = cumle_olustur(metin)
print(cumle_listesi)

```

```python
Output:
["Acikhack'in yapmış olduğu yarışmaya katılacağız.", 'Bunun için çok heyecanlıyız.']
```

