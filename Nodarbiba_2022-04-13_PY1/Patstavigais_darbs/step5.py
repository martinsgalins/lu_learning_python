number1 = int(input("Dālderi:"))
number2 = int(input("Graši:"))
number3 = int(input("Santīmi:"))
veciesantimi = number1*37*162+number2*162+number3
print("Jaunie dālderi:", int((veciesantimi-veciesantimi%100)/100))
print("Jaunie santīmi:", veciesantimi%100)