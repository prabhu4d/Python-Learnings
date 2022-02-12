"""
tuple is similar to list it is immutable
tuple are created using , not ()

"""
n1 = 1, 2, 3, 4
print(type(n1))

n2 = (1)
print(type(n2))

n3 = (1,)
print(type(n3))

tup = ('Prabhu', 100, 'John', 200)
print(tup)

# packing and unpacking

t = ('Prabhu', 'John', 'Tamil')
print(t)
(n1, n2, n3) = t
print(n2)

# comparing

a = (4, 2)
b = (2, 3)

if(a > b):
    print("a is bigger")
else:
    print("b is bigger")

# delete

del a
# print(a)

# slicing
a = (0, 1, 2, 3, 4, 5, 6)
print(a[2:5])
