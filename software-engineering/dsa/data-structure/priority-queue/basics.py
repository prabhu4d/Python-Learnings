"""
  implementing PQ in Heap (python module)

  Ref : https://realpython.com/python-heapq-module/

  Formula:
    left child = 2*k + 1
    right child = 2*k + 2
    parent node = (k-1) / 2

"""

import heapq
from math import log
from random import randint as rr


class Heap:
    def __init__(self):
        self.data = []

    def insert(self, ele):
        heapq.heappush(self.data, ele)

    def pop(self):
        print(heapq.heappop(self.data))

    def show(self):
        print(self.data)

    def showHeapTree(self):
        length = len(self.data)
        level = int(log(length+1, 2))
        for i in range(level):
            string = ''
            innerlevel = 2**i
            firstSpace = 2**(i+1)
            space = length//firstSpace
            string += "  "*space+str(self.data[innerlevel-1])
            for j in range(innerlevel-1):
                string += (length//innerlevel)*"  "
                string += str(self.data[innerlevel+j])
            print(string)


if __name__ == "__main__":
    h = Heap()
    for i in range(63):
        h.insert(rr(1, 100))
    h.show()
    h.showHeapTree()
    input()
