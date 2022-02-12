"""
OOPs in Programming Paradigm which encapsulates variables and functions for creating a complex apps

Class is a ProtoType
Object is a instance (entity) of that Prototype

Namespace is an area where you can create and store object/variable
  - Class Namespace - it is also called static variable
  - Object Namespace

Methods
  3 types of methods

  1. Instance Methods
    - Accessor
    - Mutators
  2. Class Methods
  3. Static Methods

"""


class Computer:
    # static variable
    count = 0
    info = "4th Gen - Electronic Computers"

    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu
        if(ram > 16):
            self.ai_ability = "My Computer is able to do AI Projects"
        else:
            self.ai_ability = "My Computer can do Web, App Projects. but not AI Projects"

        # object created by inner class
        self.laptop = self.Laptop()

        # to track number of objects created
        Computer.count += 1

    def whoIam(self):
        print(self)

    def config(self):
        print(f"Config is {self.ram} RAM & {self.cpu} CPU")

    def compareRAM(self, otherComputer):
        if(self.ram > otherComputer.ram):
            print(
                f"I have {self.ram - otherComputer.ram} extra RAM than yours")
        else:
            print(
                f"You have {otherComputer.ram - self.ram} extra RAM than mine")

    # Accessor
    def getRam(self):
        return self.ram

    # Mutator
    def setRam(self, value):
        self.ram = value

    @classmethod
    def getInfo(cls):
        return cls.info

    @staticmethod
    def staticInfo():
        print("Static Method in Computer Class")

    # Inner Class
    class Laptop:
        def __init__(self):
            self.brands = ["Dell", "HP", "iMac", "Lenovo"]


# Creating a Object
comp1 = Computer(8, "i5 7th gen")
comp2 = Computer(32, "i9 1st gen")

# passing object in self
# Computer.config(comp1)

# now self = comp1
print("\nConfig")
comp1.config()
comp2.config()

# print(comp1)
comp1.whoIam()


# Address
print("\nAddress")
print(f"Computer class {id(Computer)}")
print(f"comp1 obj      {id(comp1)}")
print(f"comp2 obj      {id(comp2)}")

# Comparing RAM
print("\nRAM comparisions")
comp1.compareRAM(comp2)
comp2.compareRAM(comp1)

# class info
print(Computer.getInfo())

# Static info
Computer.staticInfo()

print("\nInner Class")
print(comp1.laptop.brands)
# Accessing Brands outside of the outer class
print(Computer.Laptop().brands)
