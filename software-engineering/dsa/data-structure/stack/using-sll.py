"""
head -> top

"""


class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        data = self.top.data
        self.top = self.top.nextNode
        return data

    def length(self):
        pointer = self.top
        count = 0
        while pointer:
            count += 1
            pointer = pointer.nextNode

        return count

    def is_empty(self):
        return self.length() == 0

    def peek(self):
        return self.top.data


s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.peek())
print(s.length())
print("popped element is ", s.pop())
print(s.peek())
