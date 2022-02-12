"""
    __str__  -> only returns string object 

    __repr__ -> return any python expression such as str, list, dict

    Ref:
        https://www.journaldev.com/22460/python-str-repr-functions

"""

from typing import Union


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return "Person("+self.name+","+str(self.age)+")"

    def __repr__(self):
        return {"Name":self.name, "Age":self.age}


p = Person("Prabhu", 21)

print(p)

p.__str__()
str(p)

p.__repr__()
# repr(p)