number1 = int(input("Mark in Math: "))
number2 = int(input("Mark in Physics: "))
number3 = int(input("Mark in Chemistry: "))

if number1>65 and number2>65 and number3>50:
        print("OK")
elif number1+number2>140:
        print("OK2")
elif number1+number2+number3>190:
        print("OK3")
else:
        print("Not OK")