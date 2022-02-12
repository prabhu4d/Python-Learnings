"""
used to seperate string based on delimiter

"""

course_id = "course-v1:OneData+PY101+23DEC2021"

a, b, c = course_id.partition(":")

print(a)
print(b)
print(c)