def sum13(nums):
  count = 0
  skip = False
  for num in nums:
    if num == 13:
      skip = True
    elif skip == True:
      skip = False
      continue
    else: 
      count += num
  return count
    
    
print (sum13([2,3,13,4]))


    
