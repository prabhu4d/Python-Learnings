"""
Implementing stack using list is inefficient
because list is a dynamic array internally.

Python provides deque to implement stack

"""
from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def length(self):
        return len(self.container)


s = Stack()

s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.length())
print(s.is_empty())