"""
    Node = data + nextNode_address

"""


class Node:

    # initiating the Node Object
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def printNode(self):
        nodeValue = self.data
        nextNodeAddress = hex(id(self.nextNode))

        print(nodeValue, nextNodeAddress)


def LinkedListDetails(x, name):

    def printAddress(x):
        return (hex(id(x)))

    print("\n -----------------------------------------")
    print("The Address of "+name+" is : ", printAddress(x))
    print(name+" Value : ", x.data)
    print(name + " Next Address : ", printAddress(x.nextNode))


n3 = Node(30, None)
n2 = Node(20, n3)
n1 = Node(10, n2)


LinkedListDetails(n1, "n1")
LinkedListDetails(n2, "n2")
LinkedListDetails(n3, "n3")
