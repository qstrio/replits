class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

    
class circular_ll:
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def append(self, data):
    new_node = Node(data)
    if self.head:
      self.tail.next = new_node
      self.tail = new_node
      self.tail.next = self.head
    else:
      self.head = self.tail = new_node
      self.tail.next = self.head

  def __repr__(self):
    output = ''
    if self.head:
      output += '{} -> '.format(self.head.data)
      cur = self.head.next
      while cur != self.head:
        output += '{} -> '.format(cur.data)
        cur = cur.next
      output += '{}'.format(self.head.data)
    return output

  def insert(self, data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
      self.head = new_node
      self.tail.next = new_node
    else:
      self.head = self.tail = new_node
      self.tail.next = self.head

  def remove(self):
    output = None
    if not self.head:
      output = None
    else:
      # if not self.head.next:
      #   output = self.head.data
      #   self.head = self.tail = None
      #   print(3, 'test')
      # else:
      output = self.head.data
      if self.head.next == self.tail:
        self.head = self.tail = None
      else:
        self.head = self.head.next
        self.tail.next = self.head
    return output
    
    
if __name__ == '__main__':
  cll = circular_ll()
  cll.append(1)
  cll.append(2)
  cll.append(3)
  cll.insert(0)
  cll.insert(-5)
  print(cll.remove())
  print(cll.remove())
  print(cll.remove())
  print(cll.remove())
  print(cll.remove())
  print(cll)