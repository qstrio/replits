from Dll import Dll, Node


class Hash_Table:
  def __init__(self, capacity):
    self.capacity = capacity
    self.table = [0] * capacity
    self.size = 0

  def hash_code(self, data):
    return hash(data) % self.capacity

  def insert(self, key, value):
    hash_index = self.hash_code(key)

    ll = self.table[hash_index]

    # Initalizing a new LinkedList
    if not ll:
      new_node = Node(key, value)
      dll = Dll()
      dll.head = dll.tail = new_node
      self.table[hash_index] = dll
    else:
      node = ll.head
      
      while node:
        if node.key == key:
          node.value = value
          return
        node = node.next
        
      new_node = Node(key, value)
      ll.tail.next = new_node
      new_node.prev = ll.tail
      ll.tail = new_node

  def get(self, key):
    hash_index = self.hash_code(key)

    ll = self.table[hash_index]

    if not ll:
      return

    node = ll.head

    while node:
      if node.key == key:
        return node.value

      node = node.next

  def pop(self, key):
    hash_index = self.hash_code(key)

    ll = self.table[hash_index]

    if not ll:
      return

    node = ll.head

    if node.key == key:
      ll.head = ll.head.next
      if ll.head:
        ll.head.prev = None 
      return node.value
    else:
      node = node.next

      while node:
        if node.key == key:
          node.prev.next = node.next
          if node.next:
            node.next.prev = node.prev
          return node.value
        node = node.next

  def items(self):
    output = []

    for i in range(self.capacity):
      node = self.table[i]

      if node:
        node = node.head
        while node:
          output.append((node.key, node.value))
          node = node.next

    return output
      
      
# Testing
if __name__ == '__main__':
  ht = Hash_Table(4)

  hobbies = {
    'name': 'cool kid',
    'age': 16,
    'game': 'Minecraft',
    'food': 'Ramen',
    'sport': 'Basketball',
    'country': 'Canada'
  }

  for key, val in hobbies.items():
    ht.insert(key, val)

  assert ht.get('name') == 'cool kid'
  print('...ok')

  assert ht.get('country') == 'Canada'
  print('...ok')

  assert ht.pop('name') == 'cool kid'
  print('...ok')

  assert ht.pop('name') == None
  print('...ok')

  assert ht.pop('sport') == 'Basketball'
  print('...ok')

  assert ht.pop('name') == None
  print('...ok')