from random import randint

def compare(coins, i, j, k):
  if coins[i] > coins[k]:
    print('The counterfeit currency {} is heavier'.format(i + 1))
  else:
    print('The counterfeit currency {} is lighter'.format(j + 1))


def eight_coins(coins):
  left_sum = sum(coins[0:3])
  right_sum = sum(coins[3:6])

  if left_sum == right_sum:
    if coins[6] > coins[7]:
      compare(coins, 6, 7, 0)
    else:
      compare(coins, 7, 6, 0)
  elif left_sum > right_sum:
    left_sum2 = coins[0] + coins[3]
    right_sum2 = coins[1] + coins[4]

    if left_sum2 == right_sum2:
      compare(coins, 2, 5, 6)
    elif left_sum2 > right_sum2:
      compare(coins, 0, 4, 6)
    else:
      compare(coins, 1, 3, 6)
  else:
    left_sum2 = coins[0] + coins[3]
    right_sum2 = coins[1] + coins[4]

    if left_sum2 == right_sum2:
      compare(coins, 5, 2, 6)
    elif left_sum2 > right_sum2:
      compare(coins, 3, 1, 6)
    else:
      compare(coins, 4, 0, 6)

class Fruit:
  def __init__(self, name, size, price):
    self.name = name
    self.size = size
    self.price = price

  def get_name(self):
    return self.name

  def get_size(self):
    return self.size

  def get_price(self):
    return self.price

def solution():
  MAX_SIZE = 8
  MIN_SIZE = 1
  item = [0 for _ in range(MAX_SIZE + 1)]
  value = [0 for _ in range(MAX_SIZE + 1)]

  fruits = [
            Fruit("Plum ", 4, 4500),
            Fruit("Apple", 5, 5700),
            Fruit("Orange", 2, 2250),
            Fruit("Strawberry", 1, 1100),
            Fruit("Melon", 6, 6700)
          ]

  length = len(fruits)

  for i in range(length):
    size = fruits[i].get_size()
    for j in range(size, MAX_SIZE + 1):
      p = j - fruits[i].get_size()
      new_value = value[p] + fruits[i].get_price()

      if new_value > value[j]:
        value[j] = new_value
        item[j] = i
  print("Item  Price")
  i = MAX_SIZE
  while i >= MIN_SIZE:
    print(fruits[item[i]].get_name() +str(fruits[item[i]].get_price()))
    i = i - fruits[item[i]].get_size()
  print("Total " + str(value[MAX_SIZE]))

def survive():
  n = 11
  m = 3
  man = [0 for _ in range(n)]
  count = 1

  i = 0
  pos = -1
  alive = 0

  while count <= n:
    while True:
      pos = (pos + 1) % n

      if man[pos] == 0:
        i += 1
      if i == m:
        i = 0
        break
    man[pos] = count
    count += 1

  print("\nJoseph sequence：")
  for i in range(0,n):
    print(str(man[i]) + " , ", end="")

'''
Given 2 int values, if the parameter "negative" is True, then return True only if both ints are negative. Otherwise return True if one is negative and one is positive.

Example Output:
Function header: pos_neg(int1, int2, negative)
pos_neg(1, 1, False) → False
pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
'''
def pos_neg(int1, int2, negative):
  # if negative == True:
  #   if int1 < 0 and int2 < 0:
  #     return True
  #   else:
  #     return False
  # else:
  #   n = 0
  #   if int1 < 0:
  #     n += 1
  #   if int2 < 0:
  #     n += 1
  # if n == 1:
  #   return True
  # else:
  #   return False
  if negative:
    return True if int1 < 0 and int2 < 0 else False
  else:
    return True if ((int1 > 0 and int2 < 0) or (int1 < 0 and int2 > 0)) else False
  

if __name__ == '__main__':
  # coins = [10 for i in range(8)]
  # coins[randint(0, 7)] = int(input('Please enter the weight for the counterfeit currency:\n'))

  # eight_coins(coins)
  # print(coins)
  # solution()

  print(pos_neg(1, 1, False)) 
  print(pos_neg(-1, -1, False)) 
  print(pos_neg(1, -1, False)) 
  print(pos_neg(-1, 1, False)) 
  print(pos_neg(-4, -5, True)) 
