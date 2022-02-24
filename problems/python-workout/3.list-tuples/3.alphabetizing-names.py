PEOPLE = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
]


# lambda works fine, but it is less readable

# for person in sorted(people, key=lambda x: [x["last"], x["first"]]):
#     print(f"{person['last']}, {person['first']}: {person['email']}")

from operator import itemgetter

# for person in sorted(people, key=itemgetter("last", "first")):
#     print(f"{person['last']}, {person['first']}: {person['email']}")


def alphabetizing_names(list_of_dict):
    return sorted(list_of_dict, key=itemgetter("last", "first"))


print(alphabetizing_names(PEOPLE))


# Beyonf the exercise

"""
1. Given a sequence of positive and negative numbers, sort them by absolute 
value
"""


def abs_sort(numbers):
    return sorted(numbers, key=lambda x: abs(x))


print(abs_sort([1, 2, -1, -3, -10, -4, 5]))


"""
2. Given a list of strings, sort them according to how many vowels they 
contain.
"""


def vowels_sort(strings):
    def count_vowel(string):
        string = string.lower()
        count = 0
        for vowel in "aeiou":
            count += string.count(vowel)
        return count

    return sorted(strings, key=count_vowel)


print(vowels_sort(["ammu", "airplane", "abi", "banana"]))


"""
3. Given a list of lists, with each list containing zero or more numbers, 
sort by the sum of each inner list’s numbers.
"""


def list_of_list(lists):
    return sorted(lists, key=lambda x: sum(x))


print(list_of_list([[1, 2], [0, 1], [10, 20], [5, 4]]))
