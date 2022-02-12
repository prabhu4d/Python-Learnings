"""

    Linearly search the element in the given array

    best case - O(1)
    worst case - O(n)

"""
from random import randint

array = [randint(0,100) for _ in range(100)]
key = int(input("Enter element : "))

found = False
for i in range(100):
    if key == array[i]:
        found = True
        break

if found == True:
    print("Element at index  " ,i)
else:
    print("Element not found in array")