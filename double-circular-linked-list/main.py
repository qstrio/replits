class Node:
  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

  def __repr__(self):
    return str(self.data)


class C_D_LL:
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def insert(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prev = new_node
      new_node.next = self.head
      self.head = new_node
      new_node.prev = self.tail
      self.tail.next = new_node

  def tail_to_head(self):
    output = ''
    cur = self.tail
    if self.tail:
      output += '{} -> '.format(cur)
      cur = cur.prev
      while cur != self.tail:
        output += '{} -> '.format(cur)
        cur = cur.prev
      output += '{}'.format(self.tail)
    return output 
  

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      new_node.next = self.head
      self.head.prev = new_node
  
  def remove(self):
    delete_node = self.head
    if not self.head:
      return None
    elif self.head == self.tail:
      self.head = None
      self.tail = None
      return delete_node
    else:
      self.head = self.head.next
      self.head.prev = self.tail
      self.tail.next = self.head
      return delete_node
      
  def pop(self):
    delete_node = self.tail
    if not self.head:
      return None
    elif self.head == self.tail:
      self.head = None
      self.tail = None
      return delete_node
    else:
      self.tail = self.tail.prev
      self.tail.next = self.head
      self.head.prev = self.tail
      return delete_node

  def __repr__(self):
    output = ''
    cur = self.head
    if self.head:
      output += '{} -> '.format(cur)
      cur = cur.next
      while cur != self.head:
        output += '{} -> '.format(cur)
        cur = cur.next 
      output += '{}'.format(self.head)
    return output 
    
  
cdll = C_D_LL()
cdll.insert(10)
cdll.insert(9)
cdll.insert(8)
# print(cdll.tail_to_head())
# print(cdll)
cdll.append(7)
cdll.append(6)
print(cdll)
# print(cdll.remove())
# print(cdll.remove())
# print(cdll.remove())
# print(cdll.remove())
# print(cdll.remove())

# print(cdll.pop())
# print(cdll.pop())
# print(cdll.pop())
# print(cdll.pop())
# print(cdll.pop())
# print(cdll.pop())
print(cdll)


      


      
      
      
    

