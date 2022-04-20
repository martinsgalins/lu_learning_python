## visas Python funkcijas
https://docs.python.org/3/library/functions.html

#### round(number[, ndigits])
##### Funkcija round(number[, ndigits]) veics skaitlu noapalosanu, parametros jaiedod skaitlis un uz cik simboliem janoapalo.
#### piemers
```
number1 = float((input("Ievadiet skaitli:")))
print("Noapalots skaitlis ir:", round(number1, 2))
```

## bin(x)
##### piemers
```
number1 = int((input("Ievadiet veselu decimalo skaitli skaitli:")))
print("skaitlis binaraja sistema ir:", bin(number1))
```

## divmod(a, b)
##### piemers1
```
number1 = float((input("Ievadietskaitli1:")))
number2 = float((input("Ievadietskaitli2:")))
print("skaitlu dalijums ar atlikumu ir:", divmod(number1,number2))
```

##### piemers2
```
number1 = float((input("Ievadietskaitli1:")))
number2 = float((input("Ievadietskaitli2:")))
dalijums = divmod(number1,number2)
print("skaitlu dalijums ir:", dalijums[0])
print("skaitlu dalijuma atlikums ir:", dalijums[1])
```