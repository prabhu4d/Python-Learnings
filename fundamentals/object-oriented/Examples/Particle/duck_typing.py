"""
duck typing - not checking the object type, only check attributes and methods

isinstance() function can be used to achieve explicit type checking

"""
from scipy import constants
from particle import Particle


class Electron(object):
    def __init__(self, charge=None):
        self.c = charge or constants.electron_volt


def total_charges(particles):
    total = 0
    for p in particles:
        # if isinstance(p, Particle):
        #     total += p.c
        total += p.c
    return total


p1 = Particle(1, constants.m_p, 0)
e1 = Electron()
e2 = Electron()

particles = [p1, e1, e2]
print(total_charges(particles))
