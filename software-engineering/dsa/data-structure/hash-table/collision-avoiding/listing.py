

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [[] for i in range(self.MAX)]

    def hashing(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.hashing(key)
        found = False
        for T, ele in enumerate(self.array[h]):
            if len(ele) == 2 and ele[0] == key:
                self.array[h][T] = (key, value)
                found = True
        if not found:
            self.array[h].append((key, value))

    def __getitem__(self, key):
        h = self.hashing(key)
        for T, ele in enumerate(self.array[h]):
            if len(ele) == 2 and ele[0] == key:
                return ele[1]

    def __delitem__(self, key):
        h = self.hashing(key)
        for T, ele in enumerate(self.array[h]):
            if len(ele) == 2 and ele[0] == key:
                del self.array[h][T]

    def showAll(self):
        for i in self.array:
            print(i)
