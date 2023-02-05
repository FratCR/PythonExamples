#def Topla(birinciSayi,ikinciSayi):
#    return birinciSayi + ikinciSayi
#print(Topla(17,3))

#yas = int(input("Lutfen yasinizi giriniz : "))
#stringYas = str(yas)
#print(type(stringYas))

#import keyword
#print(keyword.kwlist)

#print ("Ankara","Istanbul","Izmir", sep="-")
#print ("Ankara "*400)

#guzelCumle = ("{} ilim {} gerek. Ilim {} bilmek {}")
#yeniCumle = guzelCumle.format("Ilim", "ilmek", "kendini", "demek.")
#print (yeniCumle)

#floatDegeri = 1.318
#intDonusum = int(floatDegeri)
#print (intDonusum)
#tekrarDonusum = float(intDonusum)
#print (tekrarDonusum)

#cumle = "kos tazi kos"
#donusum = cumle.replace ("k","h")
#print (donusum)

#def Donustur(cumle, degistirilecekHarf, yerineGelecekHarf):
#    return cumle.replace(degistirilecekHarf, yerineGelecekHarf)
#cumle = input("Lutfen cumle girin : ")
#degistirilecekHarf = input ("Degistirmek istediginiz harfi yaziniz : ")
#yerineGelecekHarf = input ("Yerine koymak istediginiz harfi yaziniz : ")
#sonuc = Donustur (cumle, degistirilecekHarf, yerineGelecekHarf)
#print (sonuc)

#toplam = input ("Lutfen sadece 1 adinizi ve soyadinizi giriniz : ")
#if (len(toplam)-1) < 10:
#    print ("Adiniz ve soyadiniz 10 harften azdir")
#elif (len(toplam)-1)>=10 and (len(toplam)-1)<=15 :
#    print ("Adiniz ve soyadiniz 10-15 harf arasindadir")
#else:
#    print ("Adiniz ve soyadiniz 15 harften buyuktur")

#try:
#    text_file = open("file.txt","r")
#except:
#    print("Boyle bir dosya yok")
#finally:
#    print("Her turlu calisiyorum")

#try:
#    sayi1 = int(input("Ilk sayiyi giriniz :"))
#    sayi2 = int(input("Ikinici sayiyi giriniz :"))
#    print(sayi1/sayi2)
#except ZeroDivisionError:
#    print("HATALI ISLEM!")
#except ValueError:
#    print("LUTFEN SAYISAL BIR VERI GIRINIZ!!!")
#finally:
#    print("Program her turlu calismaktadir")

#name = "Hello World"
#for count in range (1,101):
#    print (count, "- ",name)

#name = "Hellraiser"
#count = 1
#while count < 101:
#    print(count, "- ", name)
#    count += 1

#harfler = ["a","e","i","u","o"]
#sayac = 0
#for harf in harfler:
#    print("Dizi elemani = ",harf)
#    sayac +=1
#    print("Sirasi = ", sayac)
#    print("-----------------------")
##print("Toplam eleman sayisi : "sayac)

#liste = []
#for sayi in range (1,101):
#    if (sayi%17 == 0):
#        liste.append(sayi)
#print("1 ile 100 arasinda 17'nin tam katlari :",liste)