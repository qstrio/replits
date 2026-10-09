# def add(num):
#   print(num)
#   add(num + 2)

# add(1)

# def countdown(n):
#   print(n)
#   if n == 0:
#     return
#   else:
#     countdown(n - 1)

# countdown(5)

# def factorial(n):
#   if n == 1:
#     return 1
#   else:
#     return n * factorial(n - 1)
    
# print(factorial(5))

l = [1, 2, 3, 0, 4]

# def get_sum(l):
#   if len(l) == 1:
#     return l[0]
#   else:
#     return l[0] + get_sum(l[1:])
  
# # l[3:]
# print(get_sum(l))

# def is_increasing(lst):
#   if len(lst) == 1:
#     return True
#   elif lst[0] >= lst[1]:
#     return False
#   else:
#     return is_increasing(lst[1:])

# print(is_increasing(l))

# def filter_gt_n(lst, n):
#  if len(lst) == 0:
#    return []
#  if lst[0] > n:
#     return [lst[0]] + filter_gt_n(lst[1:], n)
#  else:
#    return filter_gt_n(lst[1:], n)
  
# print(filter_gt_n(l, 1))
# return the numbers greater than n
# doesn't work with return, but does work with print?

def intersection(list1, list2):
  #return numbers that appear in both lists, no duplicates in finished product
  return intersection_helper(list1, list2, [])

def intersection_helper(list1, list2, output):
  if not list1:
    return output
  if list1[0] in list2 and list1[0] not in output:
    output.append(list1[0])
  return intersection_helper(list1[1:], list2, output)

list1 = [1, 2, 3, 4]
list2 = [1, 1, 2, 19]
print(intersection(list1, list2))
    