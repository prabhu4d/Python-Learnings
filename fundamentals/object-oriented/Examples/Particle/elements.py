from scipy import constants
import particle as p
from elementary import ElementaryParticle

# Accessing class variable without object
print(p.Particle.roar)

# creating an object
higgs = p.Particle(1, 1, 0)
print(higgs.roar)


# methods
m_p = constants.m_p
r_p = {'x': 1, 'y': 1, 'z': 53}
a_p = p.Particle(1, m_p, r_p)
a_p.hear_me()

# subclass
ele1 = ElementaryParticle(1.5)
ele1.hear_me()