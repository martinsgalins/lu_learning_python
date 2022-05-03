start_number = int(input("Start:"))
end_number = int(input("End:"))
divinder = int(input("Divinder:"))
i = start_number
result = 0
while i <= end_number:
    if i%divinder == True:
        result += 1  
    i += 1
print(result, "numbers between",start_number, "and",end_number,"can be devided by",divinder)


    
    
    
