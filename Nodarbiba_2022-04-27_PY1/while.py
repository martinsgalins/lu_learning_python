
number1 = int(input("Enter pyramid height:"))
i = 0
while i <= number1:
    print(" "*(number1-i), "*"*i*2)
    i += 1