"""

"""


class A:
    def show(self):
        print("A Show")


class B(A):
    def show(self):
        print("B Show")


a = A()
b = B()

a.show()
b.show()