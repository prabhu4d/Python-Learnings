"""
list contains multiple types
array contains single type

"""

from array import *

signedInt = array('i', [1,-2,3,5])
print(signedInt)

unsignedInt = array('I', [1,2,3,5])
print(unsignedInt)

# buffer info
print(signedInt.buffer_info())
print(unsignedInt.buffer_info())