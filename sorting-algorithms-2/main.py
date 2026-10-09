def sort(array):
  for i in range(len(array)):
    insert_element = array[i]
    insert_position = i
    for j in range(insert_position - 1, -1, -1):
      if insert_element < array[j]:
        array[j + 1] = array[j]
        insert_position -= 1
    array[insert_position] = insert_element


lst = [5, 4, 3, 2, 1]



sort(lst)


def list_reverse(list):
  for n in range(len(list) // 2):
    list[n], list[len(list) - n - 1] = list[len(list) - n - 1], list[n]

list_reverse(lst)

print(lst)

def binary_sorting(arr, val):
  low = 0
  high = len(arr)-1
  while low <= high:
    mid = (low + high)// 2
    if arr[mid] == val:
      return mid
    elif arr[mid] > val:
      high = mid-1
    elif arr[mid] < val:
      low = mid + 1
  return -1

print(binary_sorting([1,2,3,4,5], 2))


def shell_sort(array):
  length = len(array)
  gap = length // 2
  while gap > 0:
    for i in range(gap, length):
      j = i
      while j - gap >= 0 and array[j] < array[j - gap]:
        array[j], array[j-gap] = array[j-gap], array[j]
        j -= gap
    gap = gap // 2

list1 = [3, 6, 9, 3, 2, 5, 9, 1, 0]
shell_sort(list1)
print(list1)
        

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

list = [1, 2, 3, 4]

two_sum(list, 7) -> [2, 3]


'''

# def two_sum(arr, num):
#   for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#       if arr[i] + arr[j] == num:
#         return [i, j]

def two_sum(arr, num):
  seen_numbers = {}
  for index, val in enumerate(arr):
    if num - val in seen_numbers:
      return [seen_numbers[num - val], index]
    
    seen_numbers[val] = index

list1 = [1, 2, 3, 4, 5]

print(two_sum(list1, 8))