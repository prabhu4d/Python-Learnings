"""
List is similar to Array

but it holds multiple data types
and it has built in beautiful functions

"""

a = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

# add an element in last
a.append(11)

# extenting an list with some list
a.extend([11, 22, 33])

# insert an element at specific index
a.insert(3, 333)

# remove a first element from the list
a.remove(11)

# remove a element by index
a.pop(2)

# remove the last element
a.pop()

# returning index value of the element
print(a.index(2))

# return number of times the element in the list
print(a.count(4))

# sort the list
a.sort()

# reversing a list
a.reverse()

# shallow copy
b = a.copy()
print(b)

# remove all the elements
# a.clear()

print(a)
