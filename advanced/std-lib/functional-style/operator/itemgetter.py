from operator import itemgetter

"""
instead of [] we use itemgetter function

itemgetter returns a callable functions, by using it we call to fetch the data 
from sequence

"""

name = "ABCD"

last_string = itemgetter(-1)

print("Type last_string", type(last_string))

print(last_string(name))
