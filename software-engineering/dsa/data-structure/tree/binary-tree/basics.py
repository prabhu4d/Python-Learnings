"""


"""

class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=' ')


if __name__ == "__main__":
    nodes = []
    for i in range(7):
        nodes.append(BinaryTree(i))
    for j in range(7//2):
        nodes[j].left = nodes[2*j + 1]
        nodes[j].right = nodes[2*j + 2]

    print([nodes[i].data for i in range(7)])
