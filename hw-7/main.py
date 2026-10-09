def count_evens(nums):
  count = 0
  for num in nums:
    if num%2 == 0:
      count += 1
  return count

  
for i in range(10):
  for j in range(10):
    print(i*j)