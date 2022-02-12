"""
if a child class don't have __init__ it calls parent __init__

if child has __init__ it doesn't call parent __init__. in order to call parent __init__ use super().__init__

"""


class A:
    def __init__(self):
        print("A __init__")


class B1(A):
    def __init__(self):
        print("B1 __init__")


class B2(A):
    def __init__(self):
        super().__init__()
        print("B2 __init__")


class B:
    def __init__(self):
        print("B __init__")


# Method Resolution Order
class C(A, B):
    def __init__(self):
        super().__init__()
        print("C __init__")


a = A()
b1 = B1()
b2 = B2()

c = C()
