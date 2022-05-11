a = int(input('Start: '))
b = int(input('End: '))

def print_interval(a,b):
    i = a
    while i < b:
        print(i)
        i += 1

print_interval(a,b)