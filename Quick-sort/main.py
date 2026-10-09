# Partition Function that will return the pivot number
# l is the left index and r is the right index
def partition(l, r, nums):
  # Pivot number
  pivot = nums[r]
  # returned pivot index
  par = l

  # Iterate from l index to r IndexError
  for i in range(l, r):
    # Check if the current number is less than or equal to the pivot number
    # If true, the program will swap the ValueError
    if nums[i] <= pivot:
      # Sawp the number
      nums[i], nums[par] = nums[par], nums[i]
      # Increment the pointer for parition 
      par += 1

  # Swap the last element with the pointer pivot index number
  nums[r], nums[par] = nums[par], nums[r]

  return par

# Quicksort helper function
def quicksort_helper(l, r, nums):
  # Base Case: When there is only 1 number in the list
  if len(nums) == 1:
    return nums
  # if the l index is less than the r index, the program will do the quicksort
  if l < r:
    pivot_index = partition(l, r, nums)
    quicksort_helper(l, pivot_index - 1, nums)
    quicksort_helper(pivot_index + 1, r, nums)

  return nums
  
def quicksort(nums):
  return quicksort_helper(0, len(nums) - 1, nums)

lst = [5, 3, 2, 10, 9, 100, 20]


# Quicksort v2
def quicksort2(nums):
  if not nums:
    return []

  left = []
  right = []
  pivot = nums[-1]

  for i in range(0, len(nums) - 1):
    if nums[i] <= pivot:
      left.append(nums[i])
    else:
      right.append(nums[i])

  return quicksort2(left) + [pivot] + quicksort2(right)

lst2 = quicksort2(lst)
print(lst2)


'''
Palindrome
()[]{}
()[]{} -> True
([{}]) -> True
([]){} -> True

'''

def c(s):
  stack = []
  table = {
    ']': '[',
    '}': '{',
    ')': '('
  }

  for l in s:
    if l not in table:
      stack.append(l)
    else:
      begining = stack.pop() if stack else '#'
      if begining != table[l]:
        return False
  return True if not stack else False
print(c('([]){}}'))
