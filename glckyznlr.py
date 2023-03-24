"""set1 = set([5,7,9])
set2 = set([5,6,7])
print(set1.symmetric_difference(set2))""" 
#farkli olan sayilari gösteren fonksiyon

# del komutunu kullanarak istedigimiz herhangi bir seyi silebiliriz

#listeler
"""liste = ["a","b","c"]
liste.index("b")"""

"""set1 = set([5,7,9])
set2 = set([5,6,7])
print(set1.union(set2))"""
#union metoduyla her bir farklı degeri alan, aynilari es gecen bir metoddur

"""liste = ["a","b","c"]
liste.extend(liste)
print(liste)"""

"""liste = [1,1,2,3,4,5,1,2,1]
print(liste.count(1))"""
#count metodu bir listede kac tane o elemandan oldugunu gosterir
#pop metodu listeden spesifik index numarali bir elemani siler
#append metodu listeye sondan bir ekleme yapmamizi saglar

"""def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
islem(4)"""
    
"""sayilar = [10,20,30,40]
for i in sayilar:
    if i ==30:
        break #islemi tamamen durdurur
        #continue #islemi atlatip devam ettirir
    print(i)"""
    
"""def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

islem(1,3)"""

"""A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())"""
    
"""def mesaj():
    print("Merhaba!")    
    
mesaj()"""

"""sayilar = [10,20,30]
 
for i in sayilar:
    if i > 20:
        print(i/2)"""
        
"""A = []
B = []

for i in [1,"a",12,"b"]:
    if type(i) == int:
        B.append(i)
    else:
        A.append(i)

print (A[1])"""

"""def harf_say(x):
    len(x)
 
(harf_say("Merhaba!")) #bir cikti uretmez ama basina print eklersek "None" ciktisi verir"""

"""a = [2,4,6,8]
for i in a:
    print(i**2) #alt alta karelerini verir"""
    
"""def islem(x, y):
    print(x - y)

islem(3) #hata verdi"""

#kare alma fonksiyonu

"""def kare_al(x):
    print(x**2)

kare_al(4)"""

"""def kare_al(x):
    print("Girilen sayinin karesi:", x**2)
    # str(x**2) olarak yazinca "+" koyarsak da olur
kare_al(3)"""

"""def carpma(x,y = 1):
    print(x*y)
    
carpma(134,256)"""

"""for i in ["a",11]:
    print(i) # --> a (alt satira geçerek) 11"""
    
"""def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

print(islem(1,3)) #  x ve y toplanir, 4 cikar"""

"""A = []

for i in [1,2,3,4]:
    A.append(i)

print(A[0])"""

"""A = "*A*"
if type(A) == str:
    A = A.strip("*")
    print(A) #hata verdi"""
    
"""from functools import reduce
print(reduce(lambda a,b: a+b, ["a","4","a"]))
# a4a ciktisini verir"""

"""print(list(filter(lambda x: x < 2, [1,2,3,4,5]))) #[1] ciktisini veren lambda fonksiyonu"""

"""A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))  
        # her bir kisinin adinin yanina sirasiya 1,2 ve 3 konulur"""
        
"""from functools import reduce
A = ["Veri","Bilimi","Okulu"]
print(reduce(lambda a,b: a+b, list(map(lambda x: x[0], A))))
#ciktisi VBO oluri, sadece ilk harfleri alir"""

"""print(list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50]))))
#sadece 20'den buyuk olanlari 10'a bolup gosterir"""

"""def yap(x,y,z):
    try:
        print(x/y*z) # bunun olmasi icin denenir
    except ZeroDivisionError:
        print("gecersiz islem") # olmazsa da bu hata ciktisini verir

yap(1,2,0) #lakin burada hata alinacak bir sey yok ve float olarak 0.0 degerini verir"""

"""a = [1,2,3]
print(list(map(lambda x: x*2, a))) # butun liste ogelerini teker teker fonksiyona ekler ve onlari carpar"""

"""A = []
for i in ["ali","veli","isik"]:
    A.append(i.replace("i","a")) # butun i harflerini, a harfine ceviren fonksiyondur
print(A)"""

"""import numpy as np
a = np.array([1,1,1])
b = np.array([2])
# numpy kutuphanesi sayesinde butun veriler carpilir ve array olarak getirilir
print(a+b) # [3 3 3] bu ciktiyi verir"""

"""class VeriBilimci():
    bolum = ""
    deneyim_yili = 2
    Sql_biliyor = "Evet"
    bildigi_diller = []

class VeriBilimci():
    def __init__(self): # bu fonksiyon sayesinde classin icine degismeyen bir yapi actik
        self.bildigi_diller = [] # ve böylece bu classa sahip ogeler olusturunca hepsinin degismesini engelledik
        self.bolum = ""
         
ali = VeriBilimci()
ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)"""

"""class VeriBilimci():
    yazilimcilar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
    def dil_ekle(self, yeni_dil): #tek bir metod sayesinde istedigimiz icerigi boyle ekleyebiliyoruz
        self.bildigi_diller.append(yeni_dil)
        
#print(dir(VeriBilimci)) # VeriBilimcinin icerigine bakiyoruz

Firat = VeriBilimci()
Firat.dil_ekle("Python")
print(Firat.bildigi_diller)"""

"""class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""
        self.PhoneNumber = int()
        
class DataScientist(Employees):
    def __init__(self):
        self.Languages = ""
        
veribilimci1 = DataScientist

class Marketing(Employees): # tekrar isim gibi seyleri yazmamak icin ici ice tanimlama yapabiliriz
    def __init__(self):
        self.MarketEffect = ""
        
mar1 = Marketing"""

# yan etkili ve yan etkisiz fonksiyonlarin olayi sudur; yan etkisi varsa disaridan bir sey bu fonksiyona etki eder, yan etkisi yokken de icinde olan icinde kalır, disaridan bir sey onu degistiremez

