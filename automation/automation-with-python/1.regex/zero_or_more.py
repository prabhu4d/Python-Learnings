import re

hi = re.compile(r"(Hi)* I am Prabhu")
mo = hi.search("HiHiHi I am Prabhu. How are you?")
print(mo.group())
