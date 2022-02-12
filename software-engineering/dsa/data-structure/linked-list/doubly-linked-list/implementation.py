"""
    Doubly Linked List

    node -> data, next, prev

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        pointer = self.head
        while self.head:
            yield pointer.data
            pointer = pointer.next
            if pointer == self.head:
                break

    def __len__(self):
        return len(list(iter(self)))

    def __repr__(self):
        return " <---> ".join([str(item) for item in self])

    def __getitem__(self, index):
        self.checkIndex(index)
        pointer = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer.data

    def __setitem__(self, index, data):
        self.checkIndex(index)
        pointer = self.head
        for _ in range(index):
            pointer = pointer.next
        pointer.data = data

    def checkIndex(self, index):
        if not 0 <= index <= len(self):
            raise ValueError("Index out of range")
        return True

    def insert_at(self, index, data):
        self.checkIndex(index)
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
            newNode.prev = newNode
            newNode.next = newNode
        elif index == 0:
            newNode.prev = self.tail
            newNode.next = self.head
            self.head.prev = newNode
            self.head = self.tail.next = newNode
        else:
            pointer = self.head
            for _ in range(index-1):
                pointer = pointer.next
            newNode.next = pointer.next
            newNode.prev = pointer
            pointer.next = newNode
            if newNode.next is self.head:
                self.tail = newNode

    def insert_at_beginning(self, data):
        self.insert_at(0, data)

    def insert_at_ending(self, data):
        self.insert_at(len(self), data)

    # deleting
    def delete_at(self, index):
        self.checkIndex(index)
        l = len(self)
        if(l == 1):
            self.head = self.tail = None
        elif index == 0:
            self.tail.next = self.head.next
            self.head.next.prev = self.tail
            self.head = self.head.next
        else:
            pointer = self.head
            for _ in range(index):
                pointer = pointer.next
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            if index == l-1:
                self.tail = pointer.prev

    def delete_at_beginning(self):
        self.delete_at(0)

    def delete_at_ending(self):
        self.delete_at(len(self)-1)

    def details(self):
        print("\nhead : ", self.head.data)
        print("tail : ", self.tail.data)
        print(self)


if __name__ == "__main__":
    d = DLL()
    d.insert_at_beginning(0)
    for i in range(10,60,10):
        d.insert_at_ending(i)
    d.details()
    d.insert_at_beginning(-10)
    d.details()
    d.insert_at(3,1000)
    d.details()
    d.delete_at_beginning()
    d.details()
    d.delete_at_ending()
    d.details()
    d.delete_at(4)
    d.details()
