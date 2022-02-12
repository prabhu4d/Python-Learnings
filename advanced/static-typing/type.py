"""
    Basically python is a dynamic typing

    it takes input a string we have to convert into int or float.
    some function require int or float or string or some other data types


    Ref:
        
    Sebastiaan Mathôt --> https://youtu.be/rytP_vIjzeE
        
"""
from typing import Union, Callable, Any, List, Dict

def factorial(n: Union[int, float]) -> int:

    if n is None:
        return None
    n = int(n)
    if n < 0:
        return False
    if n == 0:
        return 1
    
    return n * factorial(n-1)


print(factorial(5.7))

def map_int_list(fun: Callable, l:List[int]) -> List[int]:
    return [fun(e) for e in l]

def map_int_dict(fun: Callable, d:Dict[Any, int]) -> Dict[Any, int]:
    return {key: fun(e) for key, e in d.items()}

print(map_int_list(factorial, [0,1,2,3,4,5]))
print(map_int_dict(factorial, {'one':1, 'five':5}))