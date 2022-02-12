"""

> Passing Immutable Data Type reference

"""


string = "Geeks"


def test(string):
    string = string + "forGeeks"
    print("Inside Function:", string)


# Driver's code
test(string)
print("Outside Function:", string)
