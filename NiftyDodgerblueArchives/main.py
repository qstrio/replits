#example = input("Please enter your name: ")
#print("This is what you inputted: " + example)
animals = ["cat","dog","fish", "mouse", "bunny"]
print (animals[0])
print(animals[1:5])
print("length of hello is", len("hello"))
print(len(animals))

woods = ['pine', 'cedar','birch']
print(len(woods))
woods[2] = 'maple'
woods.append('oak')
woods.append('birch')
del woods[0]
print(woods)
woods.remove('oak')
print(woods)

primary_colors = ['red', 'blue','yellow']
secondary_colors = ['orange', 'green', 'purple']
colors = primary_colors + secondary_colors
print(colors)
animals3 = animals*3
print(animals3)

if 'red' in primary_colors:
  print('red is a primary color')
  else
  print('red is not a primary color')
if 'cedar 'in animals:
  print('cedar is an animal')elif cedar not in animals:se
  print('cedar is not an animal')
else:t('cedar is cool')e')