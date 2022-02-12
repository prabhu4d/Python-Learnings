"""

"""


class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer.data
            pointer = pointer.nextNode

    def __repr__(self) -> str:
        return " -> ".join([str(item) for item in self])

    def __len__(self):
        return len(list(iter(self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("Index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("Index out of range")
        pointer = self.head
        for i in range(index):
            pointer = pointer.nextNode
        pointer.data = data

    def printNodes(self, address=False):
        if self.head == None:
            print("LinkedList is Empty")
            return

        def nodeAddress(x):
            return hex(id(x))
            
        pointer = self.head
        list_string = ''
        if(address == True):
            while pointer:
                print("Node Address : "+str(nodeAddress(pointer))+" || Node Data : " +
                      str(pointer.data) + " || Next Node Address : "+str(nodeAddress(pointer.nextNode)))
                print("                |                  ")
                print("                |                  ")
                pointer = pointer.nextNode
            print("\n -->* None Address is : ", hex(id(None)))
        else:
            while pointer:
                list_string += str(pointer.data) + " --> "
                pointer = pointer.nextNode
            print(list_string)

    def get_length(self):
        count = 0
        pointer = self.head

        while pointer:
            pointer = pointer.nextNode
            count += 1

        print("\nLinked List length is : ", count)
        return count

    # Inserting Data
    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_at_ending(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        pointer = self.head
        while pointer.nextNode:
            pointer = pointer.nextNode
        pointer.nextNode = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_ending(data)

    def insert_at(self, index, data):
        if (index < 0) or (index >= self.get_length()):
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        pointer = self.head
        while pointer:
            if index-1 == count:
                pointer.nextNode = Node(data, pointer.nextNode)
                break
            pointer = pointer.nextNode
            count += 1

    def insert_at_value(self, value, data):
        pointer = self.head
        while pointer:
            if(pointer.data == value):
                pointer.nextNode = Node(data, pointer.nextNode)
                break
            pointer = pointer.nextNode

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.nextNode
            return

        pointer = self.head
        count = 0
        while pointer:
            if count == index-2:
                pointer.nextNode = pointer.nextNode.nextNode
                break
            pointer = pointer.nextNode
            count += 1

    def remove_head(self):
        self.head = self.head.nextNode

    def remove_tail(self):
        if self.get_length() == 1:
            print("There is only have head no tail")
            return
        pointer = self.head
        while pointer.nextNode:
            temp = pointer
            pointer = pointer.nextNode
        temp.nextNode = pointer.nextNode

    def remove_at_value(self, value):
        pointer = self.head
        if pointer is None:
            return
        if pointer.data == value:
            pointer = pointer.nextNode
        while pointer.nextNode:
            if pointer.data == value:
                pointer.nextNode = pointer.nextNode.nextNode
                break
            pointer = pointer.nextNode


if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_ending(100)
    l.insert_at_ending(200)
    l.insert_at_begining(0)
    l.insert_values([111, 222])
    l.insert_at(3, 333)
    l.insert_at_value(222, 108)
    l.remove_at(7)
    l.remove_head()
    l.remove_tail()
    l.remove_at_value(333)
    l.printNodes(True)
    l.get_length()
