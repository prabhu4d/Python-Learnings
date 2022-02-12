"""

"""

def subString(string):
    sub_string = []
    for i in range(len(string)):
        sub_string.append(string[i:])
    return sub_string

def allSubStrings(string):
    sub_string = []
    for i in range(len(string)):
        sub = string[i:]
        for j in range(len(sub)):
            sub_string.append(sub[j:])

    return sub_string

s1 = subString("AMMU")
s2 = allSubStrings("AMMU")

print(s1)
print(s2)