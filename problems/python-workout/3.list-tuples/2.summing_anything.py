"""
summing anything from the given arguments

mysum(1,2,3) => 6
mysum('abc', 'def') => 'abcdef'
mysum([1,2,3], [4,5,6]) => [1,2,3,4,5,6]


"""

# *items -> splat operator, tuple


def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item

    return output


print(mysum(10, 20, 30, 40))
print(mysum("a", "b", "c", "d"))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))

# beyond the exercise
def mysum_bigger_than(*items):
    if not items:
        return items
    first = output = items[0]
    for item in items[1:]:
        if item > first:
            output += item
    return output


print(mysum_bigger_than())
print(mysum_bigger_than(10, 20, 1, 9))
print(mysum_bigger_than([1, 2], [0, 1], [3, 4]))
print(mysum_bigger_than("o", "k", "p"))


def sum_numeric(*items):
    if not items:
        return items

    output = 0
    for item in items:
        if type(item) == int:
            output += item
        elif type(item) == float:
            output += int(item)
        else:
            if type(item) == str and item.isdigit():
                output += int(item)

    return output


print(sum_numeric(1, 2, "4", "four", 3.3))


def single_dict(items):
    if not items:
        return items

    single = {}
    for item in items:
        if type(item) == dict:
            for elem in item:
                if not elem in single:
                    single[elem] = item[elem]
                elif type(item[elem]) == list:
                    single[elem].append(item[elem])
                else:
                    single[elem] = [single[elem], item[elem]]

    return single


print(
    single_dict(
        [
            {"name": "prabhu", "age": 23},
            {"name": "abirami", "age": 24},
            {"animal": "elephant", "king": True},
        ]
    )
)
