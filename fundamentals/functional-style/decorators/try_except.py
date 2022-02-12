def div(a, b):
    try:
        return a/b
    except Exception as e:
        print(f"Division Error : {e}")


# div(10, 0)

"""
Defining Try Expect Decorator

"""


def try_except(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as E:
            print(f"Error: {E}")

    return inner


@try_except
def division(a, b):
    print(a/b)


division(10, 0)
