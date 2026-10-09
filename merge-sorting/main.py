def merge(arr, l, m, r):
  # initialize the size for list1 and list2
  n1 = m - l + 1
  n2 = r - m

  # create a temp list for list1 and list2
  list1 = [0] * n1
  list2 = [0] * n2

  # copy date from the original array to list1 and list2
  for i in range(0, n1):
    list1[i] = arr[l + i]

  for j in range(0, n2):
    list2[j] = arr[m + 1 + j]

  # initialize the pointers
  i = 0
  j = 0
  k = l

  while i < n1 and j < n2:
    if list1[i] <= list2[j]:
      arr[k] = list1[i]
      i += 1
    else:
      arr[k] = list2[j]
      j += 1
    k += 1

  while i < n1:
    arr[k] = list1[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = list2[j]
    j += 1
    k += 1

def merge_sort_helper(arr, l, r):
  if l < r:
    m = (l + (r - 1)) // 2

    merge_sort_helper(arr, l, m)
    merge_sort_helper(arr, m + 1, r)
    merge(arr, l, m, r)

def merge_sort(arr):
  merge_sort_helper(arr, 0, len(arr) -1)

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)