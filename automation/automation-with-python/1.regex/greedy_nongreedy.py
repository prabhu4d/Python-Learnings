import re

message = "HiHiHiHiHi"

greedy = re.compile(r'(Hi){3,5}')
mo1 = greedy.search(message)
print(mo1.group())

nongreedy = re.compile(r'(Hi){3,5}?')
mo2 = nongreedy.search(message)
print(mo2.group())