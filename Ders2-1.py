#ders iceriklerim
"""sayi1=12
sayi2=29
print(sayi1,sayi2)
sayi1,sayi2=sayi2,sayi1
print(sayi1,sayi2)"""

"""a,b=10,15
print("{} < {}".format(a,b),a < b)
print("{} < {}".format(b,a),b < a)"""

"""#girilen yasa göre resit olup olmadigini bulan program.
print("Lutfen yasinizi giriniz :")
sayi1 = int(input())
if sayi1 >= 18:
    print("Resitsiniz")
elif sayi1<18 and sayi1>=0:
    print("Resit degilsiniz")
else:
    print("LUTFEN POZITIF BIR SAYI GIRINIZ!")"""
    
"""# girilen aya göre mevsim bulan program.
ay = input("Lutfen bulundugunuz ayi giriniz :")
ay = ay.capitalize()

if ay == "Aralik" or ay == "Ocak" or ay == "Subat":
    print("Kis mevsimindesiniz...")
elif ay == "Mart" or ay == "Nisan" or ay == "Mayis":
    print("Ilkbahar mevsimindesiniz...")
elif ay == "Haziran" or ay == "Temmuz" or ay == "Agustos":
    print("Yaz mevsimindesiniz...")
elif ay == "Eylul" or ay == "Ekim" or ay == "Kasim":
    print("Sonbahar mevsimindesiniz...")
else:
    print("LUTFEN KURALLARA UYGUN, GECERLI BIR ISLEM YAPINIZ!!!")"""
    
"""# 6 katli binada her katta 4 daire vardir. Daire numarasina gore kat bulan program.
print("Lutfen 1 ile 28 arasindaki daire numaranizi giriniz :")
daireNo = int(input())

if daireNo < 5 and daireNo > 0:
    print("Zemin katta oturuyorsunuz.")
elif daireNo < 9 and daireNo > 4:
    print("1. Katta oturuyorsunuz.")
elif daireNo < 13 and daireNo > 8:
    print("2. Katta oturuyorsunuz.")
elif daireNo < 17 and daireNo > 12:
    print("3. Katta oturuyorsunuz.")
elif daireNo < 21 and daireNo > 16:
    print("4. Katta oturuyorsunuz.")
elif daireNo < 25 and daireNo > 20:
    print("5. Katta oturuyorsunuz.")
elif daireNo < 29 and daireNo > 24:
    print("6. Katta oturuyorsunuz.")
else:
    print("Lutfen gecerli bir sayi giriniz!")"""
    
#Donguler
"""x=0
for x in range(1,101):
    print("{}i".format(x))"""

"""for i in {1,2,3,4,5}:
    print(i*i)"""