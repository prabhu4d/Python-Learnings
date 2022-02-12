"""
  A function call itself is called recursion
"""


import sys
print(sys.getrecursionlimit())

# we can use global variable i


def hello(i=0):
    print("Hello ", i)
    i += 1
    hello(i)


hello()
