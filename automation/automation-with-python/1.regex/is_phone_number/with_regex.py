import re

phone_number_regex = re.compile(r"\d\d\d-\d\d\d-\d{4}")
print("type of phone_number_regex", type(phone_number_regex))
mobile = phone_number_regex.search("My number is 415-555-4242.")
print("type of mobile", type(mobile))
print("Phone Number Found: ", mobile.group())

