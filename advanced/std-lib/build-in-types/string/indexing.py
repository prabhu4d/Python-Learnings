name = "Prabhu"


print(name[0])

print(name[-1])  # name[len(name)-1]

# (stop - start) == len(s[start:stop])


# Stride or Step
q = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
print(q[2:-2:2])
print(q[1::2])
print(q[::-3])


# Slices are their own type and
# can be created independently of an indexing operation.

s1 = slice(1, 10, 2)
print(q[s1])
