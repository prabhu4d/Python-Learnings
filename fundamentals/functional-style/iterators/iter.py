"""
    iterator protocol
        __iter__
        __next__

    it returns only one data at a time

    actually for loop is implemented with iterable object

    Ref:
        https://www.programiz.com/python-programming/iterator
"""

class integral:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.num:
            result = 0.1 + self.n
            self.n += 0.1
            return result
        else:
            raise StopIteration

i = iter(integral(1))
