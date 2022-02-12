"""
    It removes the lead and trail character in the string\
    
"""

string = " Big Bang Theory "

print(string.strip())
print(string.strip('B')) # B is not removed because it has whitespace in left
print(string.strip(' B'))
print(string.strip('y '))

name = "Ammu"
print(name.strip('mu'))