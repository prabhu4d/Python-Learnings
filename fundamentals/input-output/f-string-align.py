"""
The format code #<10 means that the string should be placed, leftaligned, in a 
field of 10 characters, with # placed wherever the word doesn’t fill it. The 
format code #>10 means the same thing, but right-aligned.


"""

firstname = "Krishna"
lastname = "Moorthy"

print(f'Hello {firstname: <10} {lastname: >10} Welcome')