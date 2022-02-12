class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        node = Node(data, None)
        if self.front == None:
            self.front = node
        else:
            self.rear.nextNode = node
        self.rear = node
        self.size += 1

    def dequeue(self):
        if len(self) == 0:
            raise Exception(" Queue is empty")
        result = self.front.data
        self.front = self.front.nextNode
        self.size -= 1
        if self.isEmpty:
            self.rear = None
        return result

    def peek(self):
        if len(self) == 0:
            raise Exception("Queue is empty")
        return self.front.data


q = Queue()
for i in range(10):
    q.enqueue(i)
