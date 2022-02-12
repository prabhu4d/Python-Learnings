"""

spalt operator

"""

def mysum(numbers, start=0):
    print("type numbers", type(numbers))
    for number in numbers:
        start += number

    return start

print(mysum([10,20,30], -1))
print(mysum([1,2,3], 10))