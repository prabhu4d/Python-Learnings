"""
  Doubly Linked List

  None <-> 10 <-> 20 <-> 30 <-> 40 <-> None

"""

class Node:
  def __init__(self, data = None, prevNode = None, nextNode = None):
    self.data = data
    self.prevNode = prevNode
    self.nextNode = nextNode

