import re

# Grouping Patterns
phone_number_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d{4})")
mobile = phone_number_regex.search("My number is 415-555-4242.")
print("Groups: ", mobile.groups())
print("Group 1", mobile.group(1))
print("Group 2", mobile.group(2))
area_code, main_number = mobile.groups()
print(f"Area Code : {area_code}, Main Number {main_number}")

# Matching () in grouping
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print("Phone number with ()", mo.group(1))