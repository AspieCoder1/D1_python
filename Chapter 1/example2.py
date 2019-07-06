# Give the first few terms of the fibbonacci sequence
def example2():
    n = 1
    A = 1
    B = 1
    print('A:{}, B:{}'.format(A, B))
    while n < 5:
        C = A + B
        print('C:{}'.format(C))
        A = B
        B = C
        n += 1


example2()
