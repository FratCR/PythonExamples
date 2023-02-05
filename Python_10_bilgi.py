#degisken.append komutu ile arraylere yeni array ekleyebiliriz
#degisken.pop() komutu ise arreylerden (paketlerden) sonuncuyu silmeye yariyor

#isim = "Firat Cakir"
#isimTip = type(isim)
#isimUzunlugu = len(isim)
#print(isim, isimTip, isimUzunlugu)

#ad = input('Lutfen adinizi giriniz :')
#soyad = input('Lutfen soyadinizi giriniz :')
#print("Adiniz :", ad)
#print("Soyadiniz :", soyad)
#def VeriYazdir():
#   print(ad , ' ' ,soyad)
#VeriYazdir()

# Sonuc = 12*12
# print(Sonuc%5)
# print(pow(12,2,5))

#sayi1 = 15
#sayi2 = 12
#sayi3 = 4
#if sayi1 > sayi2 and sayi1 > sayi3:
#    print("En buyuk sayi :",sayi1)
#elif sayi2>sayi1 and sayi2>sayi3 :
#    print("En buyuk sayi :",sayi2)
#else:
#    print("En buyuk sayi :",sayi3)

#kisi1 = "Firat"
#kisi2 = "Ali"
#if kisi1 == kisi2:
#    print("Ayni kisilerdir")
#else:
#    print("Kisiler ayni degildir")

#for number in range(1,100):
#    print("Sayi1 :",number)
#    print("Sayi2 :",100-number)
#    print("---------------")

#for number in range (1,21):
#    kalan = number % 2
#    if kalan == 0:
#        print("Sayi Cifttir :", number)
#    else:
#        print("Sayi Tektir :", number)

#dizi = [["Firat", 2.8, 110],["Mustafa", 3.6, 102],["Kadir", 3.8, 108]]
#dizi.append(["Aktila", 4.0, 109])
#dizi=[0][1]=3.2
#print (dizi[1:2])
#print (len(dizi*5))

#string = "Firat"
#len(string) --> CALISMADI!!!

#dizi = [1, "a",3,"ert",23,"yeni", True]
#if dizi[6]:
#    print ("Sart saglandi")
#    print ("--------------------")
#    for element in dizi:
#        print(element)

#dizi = [2,5,7,3,1]
#for number in range(0, len(dizi)):
#    print ("Sayi ", number+1,"= ", dizi[number])

#tekSayilar = []
#ciftSayilar = []
#ciftSayilarinToplami = 0
#tekSayilarinToplami = 0
#for number in range(1,21):
#    kalan = number % 2
#    if kalan == 0:
#        print("Sayi Cift")
#        ciftSayilar.append(number)
#    else:
#        print("Sayi Tek")
#        tekSayilar.append(number)
#print ("Cift Sayilar",ciftSayilar)
#print ("-----------------------------")
#print ("Tek Sayilar",tekSayilar)
#for ciftNumber in ciftSayilar:
#    ciftSayilarinToplami += ciftNumber
#for tekNumber in tekSayilar:
#    tekSayilarinToplami += tekNumber
#print("Cift Sayilarin Toplami =", ciftSayilarinToplami)
#print("Tek Sayilarin Toplami =", tekSayilarinToplami)

#ogrenciler = [["Firat",55],["Yagmur",85],["Ayana",90]]
#for ogrenci in ogrenciler:
#    if ogrenci[1] > 60:
#        print (ogrenci[0],"Dersten Gecti")
#    else:
#        print (ogrenci[0],"Dersten Kaldi")
