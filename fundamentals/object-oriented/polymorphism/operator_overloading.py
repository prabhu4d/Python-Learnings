"""
  >>> a = 10
  >>> b = 20

  >>> print(a + b)
  >>> # Magic Methods
  >>> print(int.__add__(a,b))

  operator is same but operands are different or many operands

"""


class Phone:
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f'Price : {self.price}'

    def __eq__(self, other):
        if(self.price == other.price):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.price < other.price):
            return True
        else:
            return False

    def __gt__(self, other):
        return not(self.__lt__(other))


mi = Phone(40000)
apple = Phone(50000)

# Printing
print("\nPrinting Objects")
print(mi)
print(apple)


# Logical Checking
if(mi == apple):
    print("MI and Apple Price are same")
elif(mi < apple):
    print("MI is lesser than Apple")
elif(mi > apple):
    print("MI is greater than Apple")
