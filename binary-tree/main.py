from random import randint

class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

  def __repr__(self):
    return str(self.data)

class BST:
  #This is a binary search tree 
  def __init__(self):
    self.root = None

  def search_helper(self, node, val):
    #base case: if the node is empty, return False
    if not node:
      return False

    #now the program will check the value and the node value
    if val == node.data:
      return True
    elif val < node.data:
      return self.search_helper(node.left, val)
    else:
      return self.search_helper(node.right, val)
      
      
  def search(self, val):
    return self.search_helper(self.root, val)

  def insert(self, val):
    # The root node is empty
    if not self.root:
      self.root = Node(val)
    else:
      self.insert_helper(self.root, val)

  def insert_helper(self, node, val):
    # Case 1: Check if the inserted value is less than the node's data
    if val < node.data:
      # Case 1A: There is no left child
      if not node.left:
        node.left = Node(val)
      # Case 1B: There is left child
      else:
        self.insert_helper(node.left, val)
    # Case 2: Check if the inserted value is greater than or equal to node's data
    else:
      # Case 2A: There is no right child
      if not node.right:
        node.right = Node(val)
      # Case 2B: There is right child
      else:
        self.insert_helper(node.right, val)

  def delete(self, val):
    self.delete_helper(self.root, val)

  def delete_helper(self, node, val):
    # Base Case: No node 
    if not node:
      return

    # The following code will find the position of the deleted node
    if val < node.data:
      # Traverse to the left subtree
      node.left = self.delete_helper(node.left, val)
    elif val > node.data:
      # Traverse to the right subtree
      node.right = self.delete_helper(node.right, val)
    else:
      # The deleted node is found
      # If there is no left child
      if not node.left:
        temp = node.right
        node = None
        return temp
      # If there is no right child
      elif not node.right:
        temp = node.left
        node = None
        return temp
      else:
        # The case where it has two children
        min_val = self.min_helper(node.right)
        node.data = min_val
        node.right = self.delete_helper(node.right, min_val)
    return node
  
  def in_order(self):
    return self.in_order_helper(self.root)

  def in_order_helper(self, node):
    if not node:
      return ''
      
    return self.in_order_helper(node.left) + str(node.data) + ' ' + self.in_order_helper(node.right)

  def pre_order(self):
    return self.pre_order_helper(self.root)

  def pre_order_helper(self, node):
    if not node:
      return ''

    return str(node.data) + ' ' + self.pre_order_helper(node.left) + self.pre_order_helper(node.right)

  def post_order(self):
    return self.post_order_helper(self.root)

  def post_order_helper(self, node):
    if not node:
      return ''

    return self.post_order_helper(node.left) + self.post_order_helper(node.right) + str(node.data)  + ' '
  
  def pre_order_list(self):
    return self.pre_order_list_helper(self.root, [])

  def pre_order_list_helper(self, node, lst):
    if not node:
      return []
    lst.append(node.data)
    self.pre_order_list_helper(node.left, lst)
    self.pre_order_list_helper(node.right, lst)
    return lst

  def post_order_list(self):
    return self.post_order_list_helper(self.root, [])

  def post_order_list_helper(self, node, lst):
    if not node:
      return []

    self.post_order_list_helper(node.left, lst)
    self.post_order_list_helper(node.right, lst)
    lst.append(node.data)
    return lst
   # congrats

  def max(self):
   return self.max_helper(self.root)

  def min(self):
    return self.min_helper(self.root)

  def max_helper(self, node):
    while node.right:
      node = node.right
    return node.data

  def min_helper(self, node):
    while node.left:
      node = node.left
    return node.data

  # Depth First Traversal
  def bfs(self):
    return self.bfs_helper(self.root)

  def bfs_helper(self, node):
    if not node:
      return []
    output = []
    queue = []
    queue.append(node)


    while queue:
      size = len(queue)
      row = []
      while size != 0:
        temp = queue.pop()
        row.append(temp.data)
       
        if temp.right:
          queue.append(temp.right)
        
        if temp.left:
          queue.append(temp.left)



        size -= 1
      output.append(row)
    return output
      
      

# node60 = Node(60)
# node40 = Node(40)
# node80 = Node(80)
# node70 = Node(70)
# node20 = Node(20)

# node60.left = node40
# node60.right = node80
# node80.left = node70
# node40.left = node20

# bst.root = node60
bst = BST()
lst = [100, 57, 32, 189, 900, 200, 1, 50, 20, 35]

for num in lst:
  bst.insert(num)

print(bst.bfs())
bst.delete(200)
print(bst.in_order())
bst.delete(20)
print(bst.in_order())
bst.delete(100)
print(bst.in_order())
bst.delete(900)
print(bst.in_order())
# for i in range(5):
#   num = randint(0, 40)
#   lst.append(num)
#   bst.insert(num)
# print(lst)
# print(bst.dfs())


# print(bst.post_order())
# print(bst.post_order_list())
# print(bst.max())

# print(bst.min())
# print(bst.in_order())
# print(bst.pre_order())
# print(bst.pre_order_list())