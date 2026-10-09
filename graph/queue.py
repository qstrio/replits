class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def enqueue(self, data):
    node = Node(data)

    if self.is_empty():
      self.head = self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      return
    del_node = self.head
    self.head = self.head.next
    self.size -= 1
    return del_node.data

  def is_empty(self):
    return True if self.size == 0 else False

  def peek(self):
    if self.is_empty():
      return
    return self.head.data

  def check_size(self):
    return self.size