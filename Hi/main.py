'''
def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed <= 65:
      return 0
    elif speed <=85:
      return 1
    else:
      return 2
  if is_birthday == False:
    if speed <= 60:
      return 0
    elif speed <=80:
      return 1
    else:
      return 2

even = False
if even:
  print('it is even!')
'''

tuplea = ('1','2')
tupleb = ('3','4')
print(tuplea + tupleb)