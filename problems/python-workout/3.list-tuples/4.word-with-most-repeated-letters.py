from collections import Counter


def most_repeated_letter_count(word):
    return Counter(word).most_common(1)[0][1]


def most_repeating_word(string):
    return max(string, key=most_repeated_letter_count)


WORDS = ["this", "is", "an", "elementary", "test", "example"]

print(most_repeating_word(WORDS))


# Beyond the Exercise

"""
Instead of finding the word with the greatest number of repeated letters, 
find the word with the greatest number of repeated vowels.
"""


def most_repeated_vowel(word):
    word = word.lower()
    count = 0
    for vowel in "aeiou":
        count += word.count(vowel)
    return count


def most_repeating_word_vowel(string):
    return max(string, key=most_repeated_vowel)


VOWELS = ["bbccdd", "aabbcc", "aaeeff", "aaooee", "iioodd"]

print(most_repeating_word_vowel(VOWELS))

"""
Write a program to read /etc/passwd on a Unix computer. The first field contains
the username, and the final field contains the user’s shell, the command inter-
preter. Display the shells in decreasing order of popularity, such that the most pop-
ular shell is shown first, the second most popular shell second, and so forth.
"""

"""
For an added challenge, after displaying each shell, also show the usernames
(sorted alphabetically) who use each of those shells

"""
