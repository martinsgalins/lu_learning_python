start = int(input('Start: '))
end = int(input('End: '))

i = start
summa = 0

while i <= end:

    if i % 13 == 0 or (99 < i < 1000 and i % 4 == 0):
        continue

    if 999 < i < 10000 and i % 7000 == 0:
        break

    summa += i
    i += 1

print(summa)
