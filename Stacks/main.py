class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next



class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, data):
    new_node = Node(data)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if not self.head:
      return None
    else: 
      delete_node = self.head
      self.head = self.head.next
      self.size -= 1
      return delete_node.data

  def peek(self):
    if self.head:
      return self.head.data

  def check_size(self):
    return self.size

  def is_empty(self):
    return True if not self.head else False

  def __len__(self):
    return self.size

  def __repr__(self):
    output = ''
    cur = self.head
    while cur:
      output += str(cur.data) + ' - > '
      cur = cur.next
    return output
    
stack = Stack()
stack.push(10)
stack.push(20)
# print(stack.pop())
# print(stack.pop())
print(stack.is_empty())
# print(stack.check_size())
print(len(stack))


# Stack with list
class Stack2:
  def __init__(self):
    self.stack = []
    self.size = 0

  def push(self, data):
    self.stack.append(data)
    self.size += 1

  def pop(self):
    if self.stack:
      self.size -= 1
      return self.stack.pop()

  def is_empty(self):
    return True if not self.stack else False

  def peek(self):
    if self.stack: return self.stack[-1]

  def get_size(self):
    return self.size

  def get_stack(self):
    return self.stack
