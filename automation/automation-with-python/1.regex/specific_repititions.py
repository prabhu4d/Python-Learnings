import re

appa = re.compile(r"(p){2,}")
mo1 = appa.search("I love you apppppa")
print(mo1.group())
