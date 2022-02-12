"""
    after 30th term the function get slow because of recursion^recursion

"""

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

for i in range(10):
    print(i, fib(i))