"""
A default dictionary return defaults value if the key doesn't exits

"""

from collections import defaultdict

fruits = defaultdict(lambda: "apple is enterprise fruits")

fruits["banana"] = "it is good to health, 100x times strength than apple"


print(fruits["banana"])
print(fruits["mango"])
