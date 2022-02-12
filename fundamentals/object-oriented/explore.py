"""
Everythings is object in python

to get docstring of class use help(value)
>>> help(a)

to list all attributes and methods of a class, use dir()
>>> dir(a)

• A __self__ attribute is available for implicit passing into methods.


"""

a = 1

# help(a)
# print(dir(a))


def hello(name):
    return f"Hello {name}"


# print(dir(hello))