number1 = int(input("Mark in Math: "))
number2 = int(input("Mark in Physics: "))
number3 = int(input("Mark in Chemistry: "))

if ((number1>65 and number2>65 and number3>50) or (number1+number2>140) or (number1+number2+number3>190)) :
        print("OK")
else:
        print("Not OK")