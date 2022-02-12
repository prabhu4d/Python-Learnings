"""
  1pm 7-Oct-2020

  Tree
    >>> Tree is non linear data structure it means it is hierarchal DS

  Tree Components
    node
    edge

  node = data, parent, children
"""

from os import sendfile


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def showParent(self):
        return self.parent.data

    def showChildren(self):
        return [i.data for i in self.children]


if __name__ == "__main__":
    # level 0
    root = Tree('Electronics')

    # level 1
    laptop = Tree('Laptop')
    phone = Tree('Phone')
    tablet = Tree('Tablet')
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tablet)

    # level 2
    laptop.add_child(Tree('HP'))
    laptop.add_child(Tree('Dell'))
    laptop.add_child(Tree('Samsung'))
    phone.add_child(Tree('MI'))
    phone.add_child(Tree('Apple'))
    tablet.add_child(Tree('iPad Pro'))

    print(laptop.get_level())
