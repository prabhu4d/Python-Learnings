"""
    generator gives iterator in function

    iterator only defined in class

    yield

    Ref:
        https://youtu.be/mziIj4M_uwk
        
"""

def power(num):
    n = 0
    while n<num:
        yield n**2
        n += 1

p = power(10)

print(p)

print([i for i in p])