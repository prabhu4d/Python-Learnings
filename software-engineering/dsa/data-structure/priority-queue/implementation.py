from math import log
from random import randint


class PQ:
    def __init__(self):
        self.array = []

    def heapify(self, array, size, node):
        self.rootnode = node
        self.leftnode = node*2 + 1
        self.rightnode = node*2 + 2

        if self.leftnode < size and array[self.rootnode] < array[self.leftnode]:
            self.rootnode = self.leftnode

        if self.rightnode < size and array[self.rootnode] < array[self.rightnode]:
            self.rootnode = self.rightnode

        if self.rootnode != node:
            temp = array[node]
            array[node] = array[self.rootnode]
            array[self.rootnode] = temp
            self.heapify(array, size, self.rootnode)

    def insert(self, data):
        self.array.append(data)
        size = len(self.array)
        if size > 1:
            for i in range((size//2-1), -1, -1):
                self.heapify(self.array, size, i)

    def delete(self, num):
        size = len(self.array)
        for i in range(size):
            if self.array[i] == num:
                lastnode = self.array[size-1]
                self.array[size-1] = self.array[i]
                self.array[i] = lastnode
                self.array.remove(size-1)
                break

        size = len(self.array)
        for i in range((size//2)-1, -1, -1):
            self.heapify(self.array, size, i)

    def show(self):
        print(self.array)

    def showHeapTree(self):
        length = len(self.array)
        level = int(log(length+1, 2))
        for i in range(level):
            string = ''
            innerlevel = 2**i
            firstSpace = 2**(i+1)
            space = length//firstSpace
            string += "  "*space+str(self.array[innerlevel-1])
            for j in range(innerlevel-1):
                string += (length//innerlevel)*"  "
                string += str(self.array[innerlevel+j])
            print(string)


if __name__ == "__main__":
    pq = PQ()
    for i in range(20):
        pq.insert(randint(0, 50))
    pq.show()
    pq.showHeapTree()
