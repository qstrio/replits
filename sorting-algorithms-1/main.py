# list1 = [2, 1]
# print(list1)

# list1[0], list1[1] = list1[1], list1[0]

def bubble_sorting(array):
  for i in range(len(array)-1):
    for j in range(len(array) - i - 1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]

list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# bubble_sorting(list2)

# print(list2)

def minimum(array):
  min_index = 0
  for i in range(1, len(array)):
    if array[min_index] > array[i]:
      min_index = i

  return array[min_index]

print(minimum(list2))

def select_sorting(array):
  for i in range(len(array)-1):
    min_index = i
    for j in range(i, len(array)-1):
      if array[j] > array[j+1]:
        min_index = j+1
    array[i], array[min_index] = array[min_index], array[i]


select_sorting(list2)
print(list2)