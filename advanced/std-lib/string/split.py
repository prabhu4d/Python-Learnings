name = "I love you Prabhu"

print(name.split('o'))

print(name)

def with_space():
    """
    whenever we call split(" ") with space it split based on space in string

    if we call simply split() it remove the whitespace it may be 1 space, 
    2 space or 2 tabs
    
    """

    sample = "Hai Bro, I  am    Prabhu"

    print("with space", sample.split(" "))
    print("without space", sample.split())

with_space()