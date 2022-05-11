start_number = int(input("Start:"))
end_number = int(input("End:"))
i = start_number
result = 0
while i <= end_number:
    if i > 99 and i < 1000 and (i%13 == 1 or i%4 == 1):
        result += i
        print("if",i)
    elif i > 999 and i < 10000 and i%7 == 0 and i%1000 == 0:
        print("elif1",i)
        break
    elif i > 99 and i < 1000 and (i%13 == 0 or i%4 == 0):
        print("elif2",i)
        pass
    else:
        print("else",i)
        result += i
    i += 1
print(result)

    
