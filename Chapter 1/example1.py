def Happy(a):
    total = 0
    num = a
    while total != 1:
        total = 0
        split_num = [int(d) for d in str(num)]
        for i in split_num:
            total += i**2
        num = total
        if total ** 2 == a**2:
            return '{} is unhappy'.format(a)
    return '{} is happy'.format(a)


print(Happy(70))
print(Happy(4))
