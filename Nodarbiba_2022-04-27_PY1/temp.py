def convert_temperature(value, unit):

    if unit == 'C':
        return value * 9 / 5 + 32

    elif unit == 'F':
        return (value - 32) * 5 / 9

    else:
        raise ValueError('Invalid argument (unit)')


res = convert_temperature(-41, 'C')
print(round(res))





