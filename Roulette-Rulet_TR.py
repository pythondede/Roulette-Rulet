import random
import time
import math

donme_sayisi = []


def rulet_dondur():
         print("Basit Poker Oyun Denemesi")
         sayi_sor = int(input("0-36 arasi bir sayi giriniz:\n"))
         if sayi_sor in range(0, 37):
                  print("Dogru sayi girildi")
         else:
                  print("Yanlis sayi girildi, tekrar deneyiniz")
                  return rulet_dondur()

         print("\n\nMasa donmeye basliyor...\n\nDeneme Sayıları:")
         time.sleep(0)
         deneme = 0
         for i in range(1000):
                  sayi = random.randint(0, 36)
                  deneme = deneme + 1
                  print(sayi, sep="", end="\t",)

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

def def_tekrar():
         print ("\tOyun tekrar basliyor...\n\n")
         time.sleep(1)
         rulet_dondur()

rulet_dondur()
