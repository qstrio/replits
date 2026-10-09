from array import array
age = array("i",[1, 45, 23, 912, 8])
print(age)

def sort(array):
  for i in range(len(array) -1):
    min_index = i
    for j in range(i, len(array) - 1):
      if array[min_index] > array[j + 1]:
        min_index = j + 1
    array[min_index], array[i] = array[i], array[min_index]


sort(age)
print(age)


age.append(5)
print(age)
age.insert(2, 56)
age.remove(56)
age[0] = 2
age.pop()
print(age)

