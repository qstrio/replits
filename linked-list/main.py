class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  # def __repr__(self):
  #   return 'coding is fun'

class Linked_list:
  def __init__(self, head = None):
    self.head = head

  def append(self, data):
    new_node = Node(data)

    if self.head:
      cur = self.head

      while cur.next:
        cur = cur.next

      cur.next = new_node
    else:
      self.head = new_node

  def __repr__(self):
    cur = self.head
    output = ''
    while cur:
      output += str(cur.data)  + ' -> '
      cur = cur.next
    return(output[:len(output) - 3])

  def insert (self, data, insert_index):
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
      cur.next = new_node

  def delete(self, delete_index):
    cur = self.head
    if delete_index == 0:
      self.head = cur.next
      cur = None
    else:
      index = 0
      while cur.next and index < delete_index-1:
        cur = cur.next
        index += 1
      delete_node = cur.next
      cur.next = delete_node.next
      delete_node = None
    
      

alphabet = Linked_list()

alphabet.insert("a", 0)
alphabet.insert("b", 1)
alphabet.append("c")
alphabet.append("d")
alphabet.append("e")
alphabet.insert("h", 3)
alphabet.delete(2)
alphabet.delete(0)
print(alphabet)


'''
numbers = Linked_list()


numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers)
'''
# num1 = Node(1)

# num2 = Node(2)

'''
link num3's next pointer to num4
'''

# num3 = Node(3)

# num4 = Node(4)

# num1.next = num2
# num2.next = num3
# num3.next = num4

# cur = num1

# output = ''

# while num1:
#   print('this is none')

# while cur:
#   output += str(cur.data)  + ' -> '
#   cur = cur.next
# print(output[:len(output) - 3])
  

'''
create a node that stores 3
THen create another node that stores 4
'''

# print(num1)

