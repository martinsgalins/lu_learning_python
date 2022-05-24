import random
random_number = random.randint(0,100)
saraksts = []
saraksts2 = []
for _ in range(10):
    random_number = random.randint(0,100)
    saraksts.append(random_number)
print(saraksts)


for x in saraksts: ##can_divide = [number for number in random_numbers if number % 3 == 0] list comprehension
    if x % 3  == 0:
        saraksts2.append(x)
print("dalas ar 3: ",saraksts2)
