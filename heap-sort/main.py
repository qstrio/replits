from random import randint
from time import time

def heapify(lst, n, i):
  # Find the largest among root and the children
  largest = i
  # Initialize the left index and the right index
  l = 2 * i + 1
  r = 2 * i + 2

  # Finding values from the left or right children if it is greater than parent
  if l < n and lst[l] > lst[i]:
    largest = l

  if r < n and lst[r] > lst[largest]:
    largest = r

  # Check the values between largest and i, if different, heapify would be required to maintain the rule
  if largest != i:
    # Swap the values
    lst[largest], lst[i] = lst[i], lst[largest]
    heapify(lst, n, largest)
    

def heapsort(lst):
  n = len(lst)

  # Build the max heap
  # The following code will heapify the list for the first time
  for i in range(n // 2, -1, -1):
    heapify(lst, n, i)

  # Time to swap numbers
  for i in range(n - 1, 0 , -1):
    # Swap the first element with the last element
    lst[0], lst[i] = lst[i], lst[0]

    # Heapify again to make sure the heap satisfy the rule
    heapify(lst, i, 0)


lst = [randint(0, 1000) for num in range(200)]
print('List Before Heapsort')
#print(lst)
start = time()
heapsort(lst)
end = time()
print('List After Heapsort')
#print(lst)
print('The time it takes to sort the list is', end - start)