"""
decrators is wrapper function and it give the features

It is also similar to HOC in React

"""

def div(a,b):
  print(a/b)

def smartDiv(func):
  def inner(a,b):
    if a<b:
      a,b = b,a
    return func(a,b)
  return inner

div = smartDiv(div)
div(2,4)
div(4,2)