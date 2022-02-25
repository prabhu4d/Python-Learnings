"""
Lambda is anonymous functions, means you create a funtion without assigning 
into variable name

name = "Prabhu"
print(name) # using variables

print("Nature") # string literal
for onetime use there is no need to create variables

it lets us create an anonymous function, perfect for passing to other 
functions. It goes away, removed from memory as soon as it’s no longer 
needed.

lambda is restricted to single line expression


"""

# lambda


def calculate(operation):
    print(operation(10, 20))


calculate(lambda a, b: a + b)
calculate(lambda a, b: a * b)
