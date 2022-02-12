"""
decorators are inefficient, and it is new to python

class creates objects, like metaclass creates class

metaclass always inherit from type

Metaclasses are mainly used to override the special __new__() method

"""


class IsParticle(type):
    pass


class Particle(metaclass=IsParticle):
    def __init__(self):
        self.iam = "I am Particle"


print(isinstance(Particle, IsParticle))

p = Particle()

print(isinstance(p, IsParticle))
