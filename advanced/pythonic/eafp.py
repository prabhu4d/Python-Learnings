"""
Duck Typing
  * if a object has a method of duck than it is duck typing and it is not necessary to be a Duck


EAFP -> Easier to Ask for Forgiveness than Permissions
  * here we directly do the operation(try) without checking, and if operation fails we ask sorry(except)


LBYL -> Look Before You Leap
  * we checking(if) before doing an operation

"""


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    pass
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    # Pythonic (EAFP)
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)


d = Duck()
p = Person()

print("\nDuck Typing")
quack_and_fly(d)
quack_and_fly(p)


# Dict
print("\nDict")
coimbatore = {"state": "TamilNadu", "country": "India"}

# Non Pythonic
if "pincode" in coimbatore:
    print(coimbatore["pincode"])
else:
    print("No pincode in Coimbatore")


# Pythonic
try:
    print(coimbatore['pincode'])
except KeyError as e:
    print(f"🟥 Keyword {e} not found")
