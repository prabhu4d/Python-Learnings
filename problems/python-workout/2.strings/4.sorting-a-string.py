"""

"""

def strsort(sentence):
    sentence = sentence.split()
    sorted_sentence = []
    for word in sentence:
        sorted_sentence.append(''.join(sorted(word)))

    return ' '.join(sorted_sentence)

print(strsort("Hello John How are you"))