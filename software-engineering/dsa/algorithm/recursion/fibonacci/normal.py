"""
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11

"""

def fib(n):
    n1 = 0
    n2 = 1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(1,n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n2

for i in range(10):
    print(i, fib(i))