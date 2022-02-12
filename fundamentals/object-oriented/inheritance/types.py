"""
Inheritance 
  * a class which Inherits attributes and methods from parent class

"""


class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B:
    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


# Single Inheritance
class A1(A):
    def feature11(self):
        print("Feature 11")

    def feature21(self):
        print("Feature 21")


# Multi Level Inheritance
class A2(A1):
    def feature12(self):
        print("Feature 12")

    def feature22(self):
        print("Feature 22")


# Multiple Inheritance
class C(A, B):
    def feature5(self):
        print("feature 5")


# Base Class
a = A()
a.feature1()

b = B()
b.feature3()

# Single Inheritance
a1 = A1()
a1.feature1()

# Multi level
a2 = A2()
a2.feature1()

# Multiple Inheritance
c = C()
c.feature1()
c.feature3()
