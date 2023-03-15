#question 1: Area of a circle
#Get the radius of the circle from the user and calculate the area of the circle. 
# Write a program that adds "'-" enough to underline the area of the circle.
#The Area of the Circle is 232 cm2.
#----------------------------------

import math
radius=float(input("Input the radius of cirle:"))
areaOfCircle=math.pi*radius**2

result="Area of the cirle the radius "+str(radius) +" is: "+str(areaOfCircle)+" cm²"
print(result)
print("-"*len(result))

# question 2:Take the person's first and last name and write a Greeting.
# Write a program that changes the order of the first and last name and adds 3 spaces between them.

name=input("Write name:")
surname=input("Write surname:")
print("Dear "+surname+"   "+name+",")

# question 3:Take the person's name, surname and address and write them one below the other. 
# Add "*" as much as the address under the address.

name2=input("Write name:")
surname2=input("Write surname:")
adres=input("Write your adres:")

print(name2)
print(surname2)
print(adres)
print("*"*len(adres))



# question 4: Take seconds from the user and display them as days, hours, minutes and seconds.
#1 day =86400 seconds, 1 hour =3600 seconds, 1 minute = 60 seconds
# inputSeconds=int(input("Inpur the second:"))

days=inputSeconds//86400
hours=(inputSeconds%86400)//3600
minutes=(inputSeconds%3600)//60
seconds=inputSeconds%60
print(str(days)+" day, "+str(hours)+" hour, "+str(minutes)+" minute, "+ str(seconds)+" second.")

#Question 5: Write a program that takes the user's first and last name.
# prints them in the middle of a rectangle. 
# (rectangle size according to first and last name length) 

name3=input("Write name:")
surname3=input("Write surname:")

fullName=name3+" "+surname3
print(fullName)
print("I**"+"*"*len(fullName)+"**I")
print("I  "+" "*len(fullName)+"  I")
print("I  "+fullName+"  I")
print("I  "+" "*len(fullName)+"  I")
print("I**"+"*"*len(fullName)+"**I")    

#Question 6:Write a simple chat program in which you will ask the user at least 6 questions.
# And give answers according to the answers.

print("Sorun Çözme Algoritmasina Hoşgeldiniz.")
cevap=input("Çalışmıyor mu?(e/h)").lower()
if cevap == "e":
    print("Onu kurcalanma!")
    print("Sorun yok!")
elif cevap =="h":
    cevap=input("Onu kurcaladın mı?(e/h)").lower()
    if cevap == "e":
        cevap=input("Kimse biliyor mu?(e/h)").lower()
        if cevap == "e":
            cevap=input("Başka birini suçlayabilir misin?(e/h)").lower()
            if cevap == "e":
                print("Sorun yok!")
            else:
                print("Geçmiş olsun")
        else:
            print("Sorun yok!")
    else :
        cevap=input("Seni suçlayacaklar mı?(e/h)").lower()
        if cevap == "e":
            cevap=input("Başka birini suçlayabilir misin?(e/h)").lower()
            if cevap == "e":
                print("Sorun yok!")
            else:
                print("Geçmiş olsun")
        else:
            print("Sorun yok!")
else:
    print("Sadece e ve h olarak cevap olarak kabul edilir.Bir daha deneyin!")
    
    
#GAYET BASARILI, EMEGINIZE SAGLIK!
