"""
1. if a word starts with (a,e,i,o,u) add 'way' to the end of the word
   ex:
   air -> airway
2. else:
   - remove the first character
   - add first character + 'ay' at the end of the word

   ex:
   python -> ythonpay


"""


def pig_latin(word):
    end = ""
    if word[-1] in ".,:;!?":
        end = word[-1]
        word = word[:-1]
    if word[0] in "aeiouAEIOU":
        return f"{word}way{end}"

    return f"{word[1:]}{word[0]}ay{end}"


print(pig_latin("python!"))
print(pig_latin("air"))
