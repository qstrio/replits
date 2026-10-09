# Node class
class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None


# Double LinkedList class
class Dll:
  def __init__(self):
    self.head = None
    self.tail = None