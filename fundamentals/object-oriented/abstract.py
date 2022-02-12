"""
ABC - Abstract Base Class

In python abstract is not builtin

Abstract class gives a restrict ways to create mandotary methods

* Abstract class is blueprint to create class
* Abstract method is declared, but it must be implement in Child Class
* Normal method in abstract class

"""

from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    def touchscreen(self):
        return "Touch Screen is Working"


class Laptop(Computer):
    def process(self):
        return "Running..."

    def touchscreen(self):
        return "Touch Screen is Not Available"


lap1 = Laptop()
print(lap1.process())
print(lap1.touchscreen())