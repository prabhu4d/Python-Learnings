"""

"""


class Calcy:
    def add(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif c == None:
            return a + b


calc1 = Calcy()
print(calc1.add(10, 20, 30))
