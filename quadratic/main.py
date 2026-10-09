# Time Complexity O(n) Space Complexity O(1)

def get_middle(arr):
  mid = len(arr // 2)

  output = 0
  
  for i in range(mid):
    output = arr[i]

  return output

# Time Complextiy is O(n) SPace Complextiy O(1)

def reverse(arr):
  output = []

  end = len(arr) - 1

  while end >= 0:
    output.append(arr[end])
    end -= 1

  return output

# Time Complexity is O(n^2) Space Complexity is O(n)

def weird(arr):
  output = []
  weird_number = 0
  
  for num in arr:
    output.append(num)
    for num2 in arr:
      output.append(num2)

  return output