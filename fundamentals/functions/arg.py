"""

variables in function declaration -> formal arguments
values in function call -> actual arguments

Types
  position
  keyword
  default
  variable length

"""


def add(x1, x2, x3=0):
    return x1+x2+x3


print(add(44, 55))


def div(x, y):
    return x/y


print(div(y=100, x=10))


# multiple args
def mul(*x):
    tot = 1
    for i in x:
        tot *= i
    print(tot)


mul(2, 3, 4, 5, 6, 7, 8, 9, 10)

# keyworded variable length arguments


def bio(name, **data):
    print(name)
    for key, value in data.items():
        print(f"{key} -> {value}")


bio("Prabhu", age=22, interested="Data Scientist")
