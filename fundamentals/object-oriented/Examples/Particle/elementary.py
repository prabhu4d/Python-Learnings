from particle import Particle


class ElementaryParticle(Particle):
    roar = "I am Elementary Particle"

    def __init__(self, spin):
        super().__init__(2)
        self.s = spin
        self.is_fermion = bool(spin % 1.0)
        self.is_boson = not self.is_fermion
