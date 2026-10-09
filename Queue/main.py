class Node:
  def __init__(self, data, next = None):
    self.data = data
    self.next = next


class Queue:
  def __init__(self, head = None, tail = None, size = 0):
    self.head = head
    self.tail = tail
    self.size = size

  def enqueue(self, data):
    new_node = Node(data)
    if self.is_empty():
      self.tail = self.head = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      return
    delete_node = self.head
    self.head= self.head.next
    self.size -= 1
    return delete_node.data

  def is_empty(self):
    return True if self.size == 0 else False

  def get_size(self):
    return self.size

  def peek(self):
    return self.head.data if self.is_empty() else None

  def __repr__(self):
    output = ''
    cur = self.head

    while cur:
      output += '{} -> '.format(cur.data)
      cur = cur.next

    return output
    

class Queue_with_List:
  def __init__(self):
    self.queue = []
    self.size = 0

  def enqueue(self, data):
    self.queue.append(data)
    self.size += 1

  def dequeue(self):
    if self.is_empty():
      return
    self.size -= 1
    return self.queue.pop(0)

  def is_empty(self):
    return True if self.size == 0 else False

  def get_size(self):
    return self.size

  def peek(self):
    return self.queue[0] if self.is_empty() else None

  def get_queue(self):
    return self.queue


queue = Queue_with_List()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.get_queue())

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print('Dequeue Data', queue.dequeue())
# print('Dequeue Data', queue.dequeue())
# print('Dequeue Data', queue.dequeue())
# print('Dequeue Data', queue.dequeue())
# print(queue.is_empty())
# print(queue.get_size())
# print(queue)

# lst = [i for i in range(10)]
# print(lst)

    
    
  