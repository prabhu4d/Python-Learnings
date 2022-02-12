import re

bat = re.compile(r"Bat(wo)+man")
mo1 = bat.search("Adventures of Batman")
print(mo1 == None)

mo2 = bat.search("Adventures of Batwoman")
print(mo2.group())

mo3 = bat.search("Adventures of Batwowowoman")
print(mo3.group())
