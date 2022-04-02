"""
https://www.programiz.com/python-programming/datetime
"""

import datetime

now = datetime.datetime.now()
today = datetime.date.today()

print(now)
print(today)

str_date = "Mar 25, 2022 at 00:00 UTC"
str_date = str_date.split()
m = str_date[0]
d = str_date[1][:-1]
y = str_date[2]
t = str_date[4]

new_time = f"{d} {m} {y} {t}"
print("New Time -> ", new_time)

print(str_date)
print("Attributes", dir(datetime))
print(datetime.datetime.strptime(new_time, "%d %b %Y %H:%M"))
