def add(a, b):
    print("add in", __name__)
    return a+b


def sub(a, b):
    print("sub in", __name__)
    return a-b


def main():
    add(10, 15)
    sub(10, 15)


main()
