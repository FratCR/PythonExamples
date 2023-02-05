"""name = "Fırat"
surname = "Çakır"
age = "18"

write = "Benim adım " + name + " ve soyadım " + surname + ". " + "Yaşımsa " + age + "."
#print(write)

print(write[0:5])
print(write[6:21])
print(write[:10])
print(write[6:])

# print(write[-30:-1])
# print(write[0:35:3])

print(write[::1])
print(write[::-1])

name = "Firat" 
surname = "Cakir"
age = "18"

print ("My name is {} {}".format(name,surname))
print ("My name is {1} {0}".format(name,surname))
print ("My name is {s} {n}".format(n=name,s=surname))
print ("My name is {} {}. I'm {} years old".format(name,surname,age))
print ("My name is {0} {1}. I'm {2} years old. {2}".format(name,surname,age))

# number = 7/3
# print("The result is {n:1.3}".format(n=number))
n=name 
s=surname
a=age
print(f"My name is {n} {s} and I'm {a} years old.")
"""

yazi= "Sarımsakları saklasakta mı saklamasak. Yoksa saklamasakta mı saklasak."

#sonuc = yazi.upper() #hepsini büyütür
#sonuc = yazi.lower() #hepsini küçültür
#sonuc = yazi.title() #her kelimenin başını büyütür
#sonuc = yazi.capitalize() # baş harfi büyütüyor
#sonuc = yazi.islower() #hepsi küçük mü diye sorgular
#sonuc = yazi.strip() # parantezin içinde ne varsa yazıdan onu siler
#sonuc = yazi.split(".")  # parantez içindekileri araya koyuyor
#sonuc = "-".join(yazi) #bununla başlatıyor
#sonuc = yazi.index("Yoksa") #bu indexi sorguluyor
#sonuc = yazi.startswith("S") #başını sorguluyor
#sonuc = yazi.endswith(".") #sonunu sorguluyor
#sonuc = yazi.swapcase() #her harfi tersine çeviriyor
sonuc = yazi.replace("Yoksa","Yahut") #yer değiştirir
sonuc = yazi.replace("ı","i").replace(".","...")

print(sonuc)