#Derslerim
"""ornek = ('Firat\'in diye ayirdigimizda bir metod bunu engelleyebilir') #tek tirnak (') isaretinin soluna ters bolu isareti koyuldugunda tum satiri kapsar

print ("Firat","Cakir", sep ="0") #sep içine ne koyarsak virgül yerine o geçer
print ("Firat Cakir", end =":") #end içine ne koyarsak sonuna o geçecek"""


#vize ve final ortalamasini bulduran program
"""print("1 vize ve 1 final notu girilecektir. Gecme notu 50'dir.")
vizePuani = int(input("Vize notunuzu giriniz :"))
vizePuani *= 0.4
finalPuani = int(input("Final notunuzu giriniz :"))
finalPuani *= 0.6
toplamOrt= vizePuani+finalPuani

if vizePuani >40 or vizePuani<0 or finalPuani >60 or finalPuani <0:
    print("LUTFEN GECERLI BIR VIZE VE/VEYA FINAL PUANI GIRINIZ!")
else:
    if toplamOrt >= 50 and finalPuani >=30:
        print("Ortalamaniz :",toplamOrt)
        print("TEBRIKLER! Dersi gectiniz.")
    elif toplamOrt >= 0 and finalPuani <30:
        print("Ortalamaniz :",toplamOrt)
        print("Dersten kaldiniz...")
    if toplamOrt >= 90:
        print("A aldiniz...")
    elif toplamOrt >= 75 and toplamOrt < 90:
        print("B aldiniz...")
    elif toplamOrt >= 60 and toplamOrt< 75:
        print("C aldiniz...")
    elif toplamOrt >= 50 and toplamOrt< 60:
        print("D aldiniz...")
    else:
        print("F aldiniz ve kaldiniz, seneye bir daha deneyin...")"""

#listeler(lists)
"""listeler = ["Firat","Cakir","Yazilim",2004] 
#listeler metodu koseli parantez ile baslar, sinirsiz ekleme yapilabilir ve guncellenebilir.

listeler.append("all*h 0 Firat 1")
listeler[4] = "Yagmur <3"
listeler[:2] = ["Yagmur", "Ibil"]
listeler[0:4] = []
print(listeler)"""

#demetler(Tuple)
"""demetler = ("Fratos", "Cakirovski")
#demetler metodu normal parantez ile baslar, yan yana eklenen stringlerden olusur.
#demetlerdeki veri degistirilemez ve guncellenemez! Listeler ile arasindaki tek fark budur.

print(demetler)"""


"""dbSifresi = 1234

istenenSifre = int(input("Lutfen sifrenizi giriniz :"))

control = dbSifresi == istenenSifre

print(control)"""

#girilen sifre ve kullanici adini sorgulayip donut aldiran program.
"""database_passwd = 123456789
database_nicknm = "Fratos"

requested_nicknm = input("Lutfen kullanici adinizi giriniz :")
requested_passwd = int(input("Lutfen sifrenizi giriniz :"))

control = database_nicknm==requested_nicknm and database_passwd==requested_passwd

if control == True:
    print("Giris isleminiz basarili...")
else:
    print("GIRILEN ISIM YA DA SIFRE YANLIS, LUTFEN BIR DAHA DENEYINIZ!!!")"""
    


