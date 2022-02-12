"""
LEGB - Local, Enclosing,  Global, Built-in

"""
import builtins

# print(dir(builtins))


# global variable
x = "global x"


def outer():
    # local varibale for outer
    # enclosing variable for inner
    x = "local x for outer()"

    def inner():
        # local variable for inner
        x = "local x for inner()"
        print(x)

    inner()
    print(x)


outer()
print(x)


"""
changing global variable inside the function

"""
print("\n- - - Changing Global Scope")

a = "A in Global Space"
b = "B in Global Space"


def changeScope():
    global a
    a = "changing global a inside the function"
    b = "it is local b"
    print(a)
    print(b)


changeScope()
print(a)
print(b)


"""
changing enclosing varibale in nested function using nonlocal

"""
print("\n- - - Changing enclosing scope variable")


def outerFn():
    fn = "outerFn"

    def innerFn():
        nonlocal fn
        fn = "innerFn"
        print(fn)

    innerFn()
    print(fn)


outerFn()
