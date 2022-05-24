a = [1, 5, 6, 34, 0, 999,87]
b = 0 #skaitli lielaki par pirmo
c = 0 #skaitli mazaki par pedejo
print("pirma un pedeja summa: ", a[0]+a[-1])
for number in a:
    if number > a[0]:
        b += 1
print("#skaitli lielaki par pirmo: ", b)
for number in a:
    if number < a[-1]:
        c += 1
print("#skaitli mazaki par pedejo: ", c)
