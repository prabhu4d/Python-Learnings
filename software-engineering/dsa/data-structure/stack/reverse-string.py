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
        top_data = self.top.data
        self.top = self.top.nextNode
        return top_data

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


def reverse_string(x):
    s = Stack()

    for char in x:
        s.push(char)

    l = s.length()
    rev_str = ''
    while l != 0:
        rev_str += s.pop()
        l -= 1

    return rev_str


text = "We will conquere COVID-19"
print(reverse_string(text))
