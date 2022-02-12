"""

indexing will return any type, but slice only return same type

a = "abcd"
a[1] => b

a = ["a", "b", "c"]

print(type(a[1:2]), type(a[1]))



# Staying in Bounds

a = "abcd"
# throws IndexError
# print(a[5])

# when retrieving with a slice, Python is more forgiving, ignoring any index
# beyond the data structure’s boundaries:
print(a[:6])


"""


def firstlast(sequence):
    return sequence[:1] + sequence[-1:]


print(firstlast([1, 2, 3, 4, 5]))

# Beyond the Exercises


def square(number):
    return number ** 2


print(square(10))
print(square(11.11))


def largest_element(sequence):
    return max(sequence)


print(largest_element("Prabhu"))
print(largest_element(["ammu", "12"]))
print(largest_element(("ammu", "12")))


def even_odd_sums(sequence):
    evens = sequence[0::2]
    odds = sequence[1::2]
    return [sum(evens), sum(odds)]


print(even_odd_sums([10, 20, 30, 40, 50, 60]))


def plus_minus(sequence):
    string = ""
    for i, ele in enumerate(sequence):
        if i % 2 == 0:
            string += str(ele) + "+"
        else:
            string += str(ele) + "-"

    return string[:-1]


print(plus_minus([10, 20, 30, 40, 50, 60]))


def myzip(sq1, sq2):
    l = []
    for i in range(len(sq1)):
        l.append((sq1[i], sq2[i]))

    return l


print(myzip([10, 20, 30], "abc"))
