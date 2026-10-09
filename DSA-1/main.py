from array import array

donuts = array('b',[1, 2, 3, 4, 50])

print(donuts)

# donuts.append(6)
# print(donuts)
# donuts.pop()
# print(donuts)
# donuts.insert(2, 7)
# print(donuts)

# print(donuts[3])

# donuts.pop()

# for num in donuts:
#   print(num)


# def find_element_2(arr):
#   for num in arr:
#     if num == arr:
#       return '2 is found!'


def print10():
  var = 0
  while var <= 10:
    print(var)
    var += 1

def get_element(arr, index):
  return arr[index]

print(get_element(donuts, 2))

def delete_last_element(arr):
  arr.pop()

def get_last_element_equal_to_one(arr):
  for i in range(len(arr)):
    if i == len(arr) - 1 and arr[i] == 1:
      return 'the last element is 1'



