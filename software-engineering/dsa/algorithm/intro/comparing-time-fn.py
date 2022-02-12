"""
    1 <  log(n) < sqrt(n) < n < nlog(n) < n^2 < n ^3 < ... < 2^n < 3^n < ... < n^n

"""
from math import log2, sqrt, ceil, floor

def compare(i):
    print("---------------- Comparing Time Functions ----------------")
    print("log(n)   |  sqrt(n)   |   n   |  nlog(n)  |  n^2  |   2^n")
    for n in range(1,i+1):
        print(ceil(log2(n)), floor(sqrt(n)), n,ceil(n*log2(n)), n**2, 2**n)

compare(20)