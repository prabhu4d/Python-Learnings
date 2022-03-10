def checksum(data):
    total = 0
    for char in data:
        total += ord(char)
    return total


hi = "Hi Boopathi"
a = checksum(hi)
print(a)
