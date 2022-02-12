"""
decorator is alternative to metaprogramming in python

in Person class there is no gender attribute, we can add it using decorator


"""


def add_gender(cls):
    cls.gender = "Female"
    return cls


@add_gender
class Person(object):
    def __init__(self, name):
        self.name = name


p1 = Person("Prabhu")
print(p1.name, p1.gender)
