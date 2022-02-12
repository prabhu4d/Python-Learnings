"""

It uses unicode as default encoding, not ASCII


"""


def size(a):
    return a.__sizeof__()


english = "English"
தமிழ் = "தமிழ்"


print(size(english))
print(size(தமிழ்))


for a in [english, தமிழ்]:
    for i in a:
        print(f"{i} -> {size(i) - 49}")
