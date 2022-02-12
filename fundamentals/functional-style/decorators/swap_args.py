# https://youtu.be/yNzxXZfkLUA

def div(a, b):
    print(a/b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


def check_zero(func):
    def inner(a, b):
        if b == 0:
            print("Can't divide by zero")
        else:
            return func(a, b)
    return inner


div = smart_div(check_zero(div))

"""
div = smart_div(check_zero(div))

def div(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        print("Can't divide by zero")
    else:
        print(a / b)


"""


div(10, 0)

def div1(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        print("Can't divide by zero")
    else:
        print(a / b)

div1(0, 10)