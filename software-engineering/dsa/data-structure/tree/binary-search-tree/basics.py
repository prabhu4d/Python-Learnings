"""

"""

from typing import BinaryIO


class BST:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.data == data:
            return True

        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        """
        It is really difficult to understand removing item from BST
        """
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


    
def build_tree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    numbers = build_tree([80,40,120,20,60,100,40,10,30,50,70,90,110,130,150])
    print(numbers.in_order_traversal())
    print(numbers.search(30))
    numbers.delete(80)
    print(numbers.in_order_traversal())