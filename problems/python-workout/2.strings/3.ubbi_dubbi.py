"""
add 'ub' before the vowel character

"""

def ubbi_dubbi(word):
    ubbi = []
    for char in word:
        if char in 'aeiou':
            ubbi.append(f'ub{char}')
        else:
            ubbi.append(char)
    return ''.join(ubbi)


print(ubbi_dubbi('airplane'))