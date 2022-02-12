"""
to understand recursion first understand stack

"""


def a():
    print("Start of a()")
    b()
    print("End of a()")


def b():
    print("Start of b()")
    c()
    print("End of b()")


def c():
    print("Start of c()")
    print("End of c()")


a()
