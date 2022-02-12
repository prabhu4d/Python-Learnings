"""
In python every thing is object
number, string, list,...

it as inbuilt garbage collector

"""


def address(var, value):
    print(f"Address : {var} = {value} -> ", id(value))


a = 10
address("a", a)

# copying a to b
b = a
address("b", b)

# copying b to c
c = b
address("c", b)

# changing value of a
a = 11
address("a", a)
address("10", 10)

"""
every value is object
and variable are just pointing to the address of that value

"""