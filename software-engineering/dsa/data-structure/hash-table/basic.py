"""
  Hash Table is used to map a value with key (string)

  It uses Hash function to generate the location of the value

"""


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.array = [None for i in range(self.MAX)]

    def getHash(self, key):
        h = 0
        for i in key:
            h += ord(i)

        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.array[h] = value

    def __getitem__(self, key):
        h = self.getHash(key)
        return self.array[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        self.array[h] = None
