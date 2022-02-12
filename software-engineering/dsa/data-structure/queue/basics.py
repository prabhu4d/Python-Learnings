from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dequeue(self):
      self.buffer.pop()

    def length(self):
      return len(self.buffer)

    def isEmpty(self):
      return len(self.buffer) == 0


q = Queue()

q.enqueue(23)
q.enqueue(24)
q.enqueue(25)
q.length()
q.isEmpty()
q.dequeue()
q.length()
