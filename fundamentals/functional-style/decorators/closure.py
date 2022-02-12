# https://youtu.be/swU3c34d2NQ

message = "Hello"


def outer(message="Hi"):

    def inner():
        print(message)

    return inner


fn = outer()


print(fn)
print(fn.__name__)
fn()

f1 = outer("Prabhu")
f2 = outer("Ammu")
f1() # the inner func remembers message "Prabhu"
f2() # the inner func remembers message "Ammu"