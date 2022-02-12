"""
a = "string 1"
a += "string 2"

whenever we call += it creates a new string object,
it is memory expensive and computation also

use:
a = []
a.append("string 1")
a.append("string 2")
" ".join(a)

because list are mutable

"""


def pl_sentence(sentence):
    output = []
    for word in sentence.split():
        if word[0] in 'aeiou':
            output.append(f'{word}way')
        else:
            output.append(f'{word[1:]}{word[0]}ay')
      
    return ' '.join(output)

print(pl_sentence("this is test sentence"))