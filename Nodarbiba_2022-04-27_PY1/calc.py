number1 = float(input("Enter number1:"))
operator = input("Enter operator(*,/,+,-):")
if operator == "*" or "/" or "+" or "-":
    number2 = float(input("Enter number2:"))
    if number2 == 0 :
        print("Invalid operation, cannot devide to 0!")
    else:      
            if operator == "*" :
                print("Result is:",number1*number2)
            elif operator == "-" :
                print("Result is:",number1-number2)
            elif operator == "+" :
                print("Result is:",number1+number2)
            else:
                print("Result is:",number1/number2)        
else:
    print("Invalid operator!")