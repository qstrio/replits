'''
Dijkstra algorithm
'''

def dijkstra(lst):
  b = 0
  w = 0
  r = len(lst) - 1

  while w <= r:
    if lst[w] == 'W':
      w += 1
    elif lst[w] == 'B':
      lst[w], lst[b] = lst[b], lst[w]
      b += 1
      w += 1
    elif lst[w] == 'R':
      lst[w], lst[r] = lst[r], lst[w]
      r -= 1

def solution(matrix, row, col, end_row, end_col):
  global success
  matrix[row][col] = 1
  if row == end_row and col == end_col:
    success = 1
  if success != 1 and matrix[row][col + 1] == 0:
    solution(matrix, row, col + 1, end_row, end_col)
  if success != 1 and matrix[row + 1][col] == 0:
    solution(matrix, row + 1, col, end_row, end_col) 
  if success != 1 and matrix[row][col - 1] == 0:
    solution(matrix, row, col - 1, end_row, end_col)
  if success != 1 and matrix[row - 1][col] == 0:
    solution(matrix, row - 1, col, end_row, end_col) 
  if success != 1:
    matrix[row][col] = 0
  return success

def maze_printer(matrix):
  print('Maze: ')
  for row in range(7):
    output = ''
    for col in range(7):
      if maze[row][col] == 2:
        output += '█ '
      elif maze[row][col] == 1:
        output += '- '
      else:
        output += '* '
    print(output)
              

if __name__ == '__main__':
  # flags = ['R', 'B', 'W', 'B', 'R', 'W']
  # dijkstra(flags)
  # assert  flags == ['B', 'B', 'W', 'W', 'R', 'R']
  # print(flags)
  maze = [
    [ 2, 2, 2, 2, 2, 2, 2 ],
    [ 2, 0, 0, 0, 0, 0, 2 ],
    [ 2, 2, 2, 0, 2, 0, 2 ],
    [ 2, 0, 2, 0, 0, 2, 2 ],
    [ 2, 2, 0, 2, 0, 2, 2 ],
    [ 2, 0, 0, 0, 0, 0, 2 ],
    [ 2, 2, 2, 2, 2, 2, 2 ]
  ]
  
  maze_printer(maze)
  
  start_row = 1
  start_col = 1
  end_row = 5
  end_col = 5
  success = 0
  print(solution(maze, start_row, start_col, end_row, end_col))

  maze_printer(maze)