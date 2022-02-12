from random import randint as ri


def atm(note):
    amounts = [100, 200, 500, 1000, 2000]
    for i in range(note):
        yield amounts[ri(0, 4)]


for amount in atm(10):
    print(amount)
