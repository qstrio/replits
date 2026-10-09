'''x = 8
while x > 0:
  x-=0.5
  print(x)

num_fibs = 10
a = 0
b = 1
fib_sum = 0
count = 1
while count <= num_fibs:
  print(fib_sum)
  a = b
  b = fib_sum
  fib_sum = a+b
  count+=1

my_string = "ijiejbigjsefniadjg"

indexing = len(my_string) -1
print(my_string[indexing])

my_fruit = "banana"
num_a = 0
for letter in my_fruit:
  if letter == 'a':
    num_a += 1

print (num_a)

def first_half(string):
  length = len(string)
  half = int(length/2)
  return string[0:half]

print(first_half("grapefruit"))
print(first_half("123456"))
print(first_half("grape fruit"))
'''

def game(quest, ans):
  score = 0
  result = input(quest + "?:")
  if result == ans:
      print(result + " is correct!")
      score += 1
  else:
      print("The answer was: " + ans)
  
  print("Score +", score)

game("When was Adrienne Rich born","1929")
game("How many sons did she have","3")
game("What style of poem did she like to write","free verse")


    
    
  