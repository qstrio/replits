class Node:
  def __init__(self, data, prev=None, next=None):
    self.data = data
    self.prev = prev
    self.next = next

class Double_LinkedList:
  def __init__(self, head=None):
    self.head = head

  def __repr__(self):
    output = ''
    cur = self.head
    while cur:
      output += str(cur.data) + ' -> '
      cur = cur.next
    return output[:len(output) - 4]

  def append(self, data):
    new_node = Node(data)
    if self.head:  
      h = self.head
      while h.next:
        h = h.next
      h.next = new_node
      new_node.prev = h
    else:
      self.head = new_node

  def insert(self, data, insert_index):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
    else:
      index = 0
      cur = self.head
      while cur.next and index < insert_index -1:
        cur = cur.next
        index += 1
      new_node.next = cur.next
      cur.next.prev = new_node
      cur.next = new_node
      new_node.prev = cur

  def delete(self, delete_index):
    cur = self.head
    if delete_index == 0:
      self.head = cur.next
      cur.next.prev = None
      cur = None
    else:
      index = 0
      while cur.next and index < delete_index -1:
        cur = cur.next
        index += 1
      delete_node = cur.next
      delete_node.next.prev = cur
      cur.next = delete_node.next
      delete_node = None
      
  def get_tail(self):
    '''This function will return the tail pointer'''
    cur = self.head
    while cur.next:
      cur = cur.next
    return cur

  def tail_to_head(self):
    '''This function will return the tail data all the way to the head'''
    cur = self.get_tail()
    output = ''
    
    while cur:
      output += '{} -> '.format(cur.data)
      cur = cur.prev

    return output[:len(output) - 4]
    
    
  
    

numbers = Double_LinkedList()
numbers.append("a")
numbers.append("b")
numbers.append("c")
numbers.append('d')
numbers.insert('bb', 2)
# numbers.delete(2)
print(numbers)
print(numbers.tail_to_head())
# tail = numbers.get_tail()
# print(tail.data)
# 1 -> 2 -> 3 -> 4


# class Person:
#   def __init__(self, height, nationality, birthday):
#     self.height = height
#     self.nationality = nationality
#     self.birthday = birthday

#   def get_height(self):
#     return self.height

# luke_skywalker = Person(180, 'American', '1922/12/25')
# print(luke_skywalker.get_height())

name = '{} is fun, do you think so {}'.format(1, 'Test1')
print(name)