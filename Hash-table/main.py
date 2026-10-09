# Node class for the pair
class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

  def __repr__(self):
    return str((self.key, self.value))

# Hash Table class
class Hash_Table:
  def __init__(self, capacity=4):
    self.table = [0] * capacity
    self.size = 0

  def __len__(self):
    return self.size

  # A method that will convert the key into numbers
  def hash_code(self, key):
    return hash(key) % len(self.table)

  # Put method that will a new pair to the hash table
  def put(self, key, value):
    if not key:
      return

    # create a node for the pair
    node = Node(key, value)
    hash_index = self.hash_code(key)

    # Check if the linked list is 0 or not
    if not self.table[hash_index]:
      self.table[hash_index] = node
      self.size += 1
    else:
      temp = self.table[hash_index]

      while temp.next:
        if temp.key == key:
          temp.value = value
          return
        temp = temp.next

      temp.next = node
      self.size += 1

  # Get method that will return the value by the key
  def get(self, key):
    if not key:
      return None

    hash_index = self.hash_code(key)

    temp = self.table[hash_index]

    while temp:
      if temp.key == key:
        return temp.value
      temp = temp.next

    return None

  # items method that will return all the pairs in a list
  def items(self):
    output = []
    for i in range(len(self.table)):
      temp = self.table[i]
      while temp:
        output.append((temp.key, temp.value))
        temp = temp.next
    return output

  # keys method that will return all the keys in a list
  def keys(self):
    output = []
    for i in range(len(self.table)):
      temp = self.table[i]
      while temp:
        output.append(temp.key)
        temp = temp.next
    return output

  # keys method that will return all the keys in a list
  def values(self):
    output = []
    for i in range(len(self.table)):
      temp = self.table[i]
      while temp:
        output.append(temp.value)
        temp = temp.next
    return output

ht = Hash_Table()
ht.put('food', 'Ramen')
ht.put('name', 'Dako')
ht.put('car', 'Tesla')
ht.put('food', 'Steak')
print(ht.items())
print(ht.keys())
print(ht.values())
print(ht.get('food'))
print(ht.get('name'))
print(ht.get('car'))
print(ht.get('s'))
