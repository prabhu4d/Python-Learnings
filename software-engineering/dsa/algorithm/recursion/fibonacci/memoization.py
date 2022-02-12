"""
    storing the values of nth term, so it will not compute again

    Ref:
        https://youtu.be/Qk0zUZW-U_M

"""

fibonacciCache = {}

def fib(n):
    if n in fibonacciCache:
        return fibonacciCache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        values = fib(n-1)+fib(n-2)
    
    fibonacciCache[n] = values
    return values

for i in range(0,101):
    print(i, fib(i))