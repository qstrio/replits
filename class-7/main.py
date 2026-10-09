'''for num in range(0,5):
  print(num)

for num in range(5):
  print(num)


pizza = ['pepperoni','cheese','vegetarian']

for item in pizza:
  print(item)
  

# print the odd numbers from 1 - 15
for num in range(1,16, 2):
  print(num)

for num in range(20,41,2):
  print(num)

  # print all numbers between 1 and 20 that are divisible by either 2 or 3


for num in range(1,21):
  if num%2 == 0 or num%3 == 0:
    print(num)

for num in range(15, 0, -1):
  print(num)


for letter in 'Python':
  if letter == 'h':
    break
  print(letter, end='')

for letter in 'Python':
  if letter == 'h':
    continue
  print(letter, end='')


for letter in "Python":
  print(letter)
else: # when inner for loop is done
  print("done printing")


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

for each_list in matrix:
  for num in each_list:
    print(num)


1. Create a matrix which is a 2d-array
2. Write a for loop to print out each element in all of the lists but do it using range

list1 = [[9,8,7],[6,5,4]]

for num in range(2):
  for item in range(3):
    print(list1[num][item])

print(list1[0][0])

 *
 ***
 *****
 *******

 
stars = [[*],[***],[*****],[*******]]
'''

for star in range(1,21,2):
  print("*" * star)