class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
  
  def push(self, data):
    node = Node(data)
    node.next = self.head
    self.head = node
    self.size += 1

  def pop(self):
    if self.is_empty():
      return

    del_node = self.head
    self.head = self.head.next
    self.size -= 1
    return del_node.data

  def is_empty(self):
    return True if not self.head else False

  def peek(self):
    if self.is_empty():
      return
    return self.head.data

  def check_size(self):
    return self.size