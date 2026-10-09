from stack import Stack
from queue import Queue
# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# # print(matrix[0][0])

# for row in matrix:
#   output = '|'
#   for column in row:
#     output += '{} '.format(column)
#   print(output[:len(output) - 1] + '|')

'''
Graph Implementation
'''

# Vertex class
class Vertex:
  def __init__(self, data):
    self.data = data
    self.visited = False


# Graph class
class Graph:
  def __init__(self, max_size):
    self.max_size = max_size
    self.vertexs = []
    self.graph = [[0 for i in range(max_size)] for i in range(max_size)]
    self.size = 0
    self.topologys = [0 for i in range(max_size)]
    self.stack = Stack()
    self.queue = Queue()

  def add_vertex(self, data):
    vertex = Vertex(data)
    self.vertexs.append(vertex)
    self.size += 1

  def add_edge(self, row, column):
    self.graph[row][column] = 1

  def topology_sort(self):
    while self.size > 0:
      no_successor_vertex = self.get_no_successor_vertex()

      if no_successor_vertex == -1:
        print('There are ring the graph')
        return

      self.topologys[self.size - 1] = self.vertexs[no_successor_vertex]
      self.remove_vertex(no_successor_vertex)

  def get_no_successor_vertex(self):
    exist_successor = False
    for row in range(self.size):
      exist_successor = False
      for column in range(self.size):
        if self.graph[row][column] == 1:
          exist_successor = True
          break

      if exist_successor == False:
        return row
    return - 1

  def remove_vertex(self, vertex):
    if vertex != self.size - 1:
      for i in range(vertex, self.size - 1):
        self.vertexs[i] = self.vertexs[i + 1]

      for row in range(vertex, self.size - 1):
        for column in range(self.size):
          self.graph[row][column] = self.matrix[row + 1][column]

      for column in range(vertex, self.size - 1):
        for row in range(self.size - 1):
          self.graph[row][column] = self.graph[row][column + 1]
    self.size -= 1
  
  def depth_first_search(self):
    first_vertex = self.vertexs[0]
    first_vertex.visited = True
    print(first_vertex.data, end='')
    self.stack.push(0)

    while not self.stack.is_empty():
      row = self.stack.peek()
      column = self.find_unvisted_vertex(row)

      if column == -1:
        self.stack.pop()
      else:
        self.vertexs[column].visited =True
        print('->', self.vertexs[column].data, end='')
        self.stack.push(column)
    self.clear()

  def breadth_first_search(self):
    # start searching from the first vertex
    first_vertex = self.vertexs[0]
    first_vertex.visited = True
    print(first_vertex.data, end='')
    self.queue.enqueue(0)

    column = 0

    while not self.queue.is_empty():
      head = self.queue.dequeue()

      column = self.find_unvisted_vertex(head)

      while column != -1:
        self.vertexs[column].visited = True
        print('->', self.vertexs[column].data, end='')
        self.queue.enqueue(column)
        column = self.find_unvisted_vertex(head)
    self.clear()

  
  def find_unvisted_vertex(self, row):
    for column in range(self.size):
      if self.graph[row][column] == 1 and self.vertexs[column].visited == False:
        return column
    return -1

  def clear(self):
    for v in self.vertexs:
      v.visited = False

  def get_matrix(self):
    return self.graph

  def get_vertexs(self):
    return self.vertexs

  def get_topologys(self):
    return self.topologys
      
    
if __name__ == '__main__':
  graph = Graph(5)
  # Add Vertex
  graph.add_vertex("A")
  graph.add_vertex("B")
  graph.add_vertex("C")
  graph.add_vertex("D")
  graph.add_vertex("E")
  # Add adjacency edge
  graph.add_edge(0, 1)
  graph.add_edge(0, 2)
  graph.add_edge(0, 3)
  graph.add_edge(1, 2)
  graph.add_edge(1, 3)
  graph.add_edge(2, 3)
  graph.add_edge(3, 4)

  graph.depth_first_search()
  print()
  graph.breadth_first_search()
  print("Directed graph topological ordering:")
  graph.topology_sort()
  length = len(graph.get_topologys())
  for i in range(0, length):
    print(graph.get_topologys()[i].data, " -> ", end="")
