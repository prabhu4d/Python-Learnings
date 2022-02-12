"""
  Telusko - https://youtu.be/TqqQld6m6A0
"""


def fact(n):
    if n == 0:
        return 1

    return n*fact(n-1)


print(fact(20))
