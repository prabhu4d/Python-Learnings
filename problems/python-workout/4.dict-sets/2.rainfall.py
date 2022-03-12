def get_rainfall():
    rainfall = {}

    while True:
        city_name = input("Enter the City name: ")
        if not city_name:
            break

        mm_rain = int(input("Enter rain in mm: "))
        rainfall[city_name] = rainfall.get(city_name, []) + [int(mm_rain)]

    for city, rain in rainfall.items():
        print(f"{city} -> Total: {sum(rain)}mm, Average: {sum(rain)/len(rain)} ")


# get_rainfall()


# Beyond the Exercise

"""
Instead of printing just the total rainfall for each city, print the total rainfall and
the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40
for Boston, you would see that the total was 90 and the average was 30.
"""

"""
Open a log file from a Unix/Linux system—for example, one from the Apache
server. For each response code (i.e., three-digit code indicating the HTTP
request’s success or failure), store a list of IP addresses that generated that code.
"""

"""
Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results
"""

import os

sibling_file = os.path.dirname(__file__) + "/1.restaurant.py"

words_len_count = {}

with open(sibling_file) as file:
    content = file.read().split()
    count_content = 0
    for word in content:
        word_len = len(word)
        count_content += word_len
        words_len_count[word_len] = words_len_count.get(word_len, 0) + 1

    dicts_count = 0
    for key, value in words_len_count.items():
        dicts_count += key * value

    print(words_len_count)
    print(count_content, dicts_count)
