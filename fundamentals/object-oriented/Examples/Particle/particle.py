from scipy import constants

class Particle(object):
    """A Particle is a constituent unit of the universe
    
    Attributes
    ---------

    c : charge in units of [e]
    m : mass in units of [kg]
    r : position in units of [meters]
    """

    roar = "I am a particle!"

    def __init__(self, charge=None, mass=None, position=None):
        """Initializes the particle with default values for
           charge c, mass m, and position r.
        """
        self.c = charge or 1
        self.m = mass or 1
        self.r = position or {'x': 1, 'y': 1, 'z': 1}

    def hear_me(self):
        myroar = f"""
        {self.roar}
        My Charge is {self.c}
        My Mass is {self.m}
        My X position is {self.r['x']}
        My Y position is {self.r['y']}
        My Z position is {self.r['z']}
        """
        print(myroar)

    def delta_x_min(self, delta_p_x):
        hbar = constants.hbar
        delx_min = hbar / (2.0 * delta_p_x)
        return delx_min


    @staticmethod
    def possible_flavors():
        return ["up", "down", "top", "bottom", "strange", "charm"]