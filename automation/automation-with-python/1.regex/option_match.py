import re

bat = re.compile(r'Bat(wo)?man')
mo1 = bat.search('The Adventures of Batman')
print(mo1.group())

bat = re.compile(r'Bat(wo)?man')
mo1 = bat.search('The Adventures of Batwoman')
print(mo1.group())