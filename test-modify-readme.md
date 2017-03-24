# ![Test Logo](http://i.imgur.com/jSTFbtN.jpg) Test Logo

[**Open the google.com**](http://www.google.com)<br>
[**Google Sayfasını aç**](http://www.google.com)
<br>
<br>

In this line **"I will try to make some words bold"**<br>
Bu satırda **"Bazı kelimeleri koyu yapmaya çalışacağım"**

In this line *"I will try to make some words italic"*<br>
Bu satırda *"Bazı kelimeleri eğik yazmaya çalışacağım"*
<br>
<br>

# This is a h1 tag
## This is a h2 tag
### This is a h3 tag
#### This is h4 tag
###### This is h5 tag
###### This is h6 tag


# Bu satır h1 başlığını gösterir
## Bu satır h2 başlığını gösterir
### Bu satır h3 başlığını gösterir
#### Bu satır h4 başlığını gösterir
##### Bu satır h5 başlığını gösterir
###### Bu satır h6 başlığını gösterir

<br>
<br>


* Unit 1
* Unit 2
  * Unit 2a
  * Unit 2b


* Konu1
* Konu2
  * Konu2 Alt Konu1
  * Konu2 Alt konu2
<br>
<br>


### Comment entred (raw view)
<!--Comment Area Test Entry from Atom thought GitHubDesktop -->
<!--Atom editörü kullanalarak GitHubDesktop üzerinden yorum alanına giriş yapılması-->
<br>
<br>

#### Blackquotes Test
>This is a Blackquotes

>Bu bir Blackquotestur
<br>
<br>

#### Syntax Hightlight
```python
def rulet_dondur():
         print("Basit Poker Oyun Denemesi")
         sayi_sor = int(input("0-36 arasi bir sayi giriniz:\n"))
         if sayi_sor in range(0,36):
                  print("Dogru sayi girildi")
         else:
                  print("Yanlis sayi girildi, tekrar deneyiniz")
                  return rulet_dondur()

         print("\n\nMasa donmeye basliyor...\n\nCikan sayilar;")
         time.sleep(0)
         deneme = 0
         for i in range(1000):
                  sayi = random.randint(0,36)
                  deneme = deneme +1
                  print(sayi,sep="",end="\t",)

                  if sayi == sayi_sor:
                           donme_sayisi.append(deneme)
                           toplam_cevirme_sayisi = sum(donme_sayisi)
                           ortalama_tutturma = toplam_cevirme_sayisi / len(donme_sayisi)
                           toplam_tutturma = len(donme_sayisi)
                           print("\n\n\t[%d]cevirme sonunda girmis oldugunuz [%d] akamini tuturdunuz"%(deneme,sayi_sor))
                           print("\tGecmisteki tutturma denemeleri\t")
                           print("\t"+str(donme_sayisi))
                           print("\tToplam [%d] defa cevirdiniz [%d] defa tutturdunuz" % (toplam_cevirme_sayisi,math.ceil(toplam_tutturma)))
                           print("\tOrtalama [%d] defa cevirdiginizde tutturuyorsunuz"% math.ceil(ortalama_tutturma))

                           return def_tekrar()
```
<br>
<br>
#### Task List , Gorev Listesi Test
- [x] @mentions, #refs, test 1234
- [x] Tamamlanmis gorevler
- [x] Completed Task
- [ ] Incomplete Task
- [ ] Tamamlanmamiş görev
- [ ] Tamamlanmamış diğer görev

<br>
<br>
