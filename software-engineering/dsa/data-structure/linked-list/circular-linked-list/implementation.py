"""
    Circular Linked List feature is we don't need to traversal the list to add element in the last node

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while self.head:
            yield node.data
            node = node.next
            if node == self.head:
                break
    
    def __len__(self):
        return len(list(iter(self)))

    def __repr__(self):
        if self.head is None:
            h = "None"
            t = "None"
        else:
            h = str(self.head.data)
            t = str(self.tail.data)
        ll = " -> "+" -> ".join([str(item) for item in self]) + " -> "
        space = "^"+" "*(len(ll)-2)+"|"+"\n"+"|"+" "*(len(ll)-2)+"v"
        line = "-"*(len(ll)-2)
        return "head : "+h+", tail : "+t+"\n"+ll+"\n"+space+"\n"+line

    def __getitem__(self, index):
        if not 0 <=index <=len(self)-1:
            raise ValueError("Index out of Range")
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data

    def __setitem__(self, index, data):
        if not 0 <=index <=len(self)-1:
            raise ValueError("Index out of range")
        node = self.head
        for _ in range(index):
            node = node.next
        node.data = data

    # Adding Nodes
    def insert_at(self, index, data):
        if not 0 <= index <= len(self):
            raise ValueError("Index out of range")
        newNode = Node(data)
        if self.head is None:
            newNode.next = newNode
            self.head = self.tail = newNode
        elif index == 0:
            newNode.next = self.tail.next
            self.head = self.tail.next = newNode
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            newNode.next = node.next
            node.next = newNode
            if index == len(self)-1:
                self.tail = newNode
        
    def insert_at_beginning(self, data):
        self.insert_at(0, data)
    
    def insert_at_ending(self, data):
        self.insert_at(len(self), data)

    
    # Deleting Nodes
    def delete_at(self, index):
        l = len(self)
        if not 0 <=index <= l:
            raise ValueError("Index out of range")
        if self.head == self.tail:
            self.head = self.tail = None
        elif index == 0:
            self.tail.next = self.head.next
            self.head = self.tail.next
        else:
            node = self.head
            for _ in range(index-2):
                node = node.next
                print("node.data ",node.data)
            print("node.next.data ",node.next.data)
            print("node.next.next.data ", node.next.next.data)
            node.next = node.next.next
            if index == l:
                self.tail = node
    
    def delete_at_beginning(self):
        self.delete_at(0)

    def delete_at_ending(self):
        self.delete_at(len(self))


if __name__ == "__main__":
    c = CLL()
    for i in range(10,110,10):
        c.insert_at_ending(i)

    print(c)