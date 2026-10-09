# fruit_colors = {"apples":"red","bananas":"yellow","grapes":"purple","oranges":"orange"}
# for fruit, colour in fruit_colors.items():
#   print(fruit, colour)

# del fruit_colors["grapes"]

# if "grape" in fruit_colors:
#   print("grape is in fruit_colors")
# else:
#   print("grape is not in fruit_colors")

# fruit_colors2 = fruit_colors.copy()
# fruit_colors2["apples"] = "green"
# print(fruit_colors)
# print(fruit_colors2)
'''
phrase = "the quick brown fox jumps over the lazy dog"

counter = {}
for i in phrase:
  if i in counter:
    counter[i] += 1
  else:
    counter[i] = 1

for letter, count in counter.items():
  print("there are",count,letter+"'s in the phrase")



birthdays = {"my cat":"08/24/2018","barack obama":"08/04/1961","nickola tesla":"07/10/1856"}

print("Hi person, welcome to the birthday dictionary!!!!!")
print("\nWe know the birthdays of:")
for pers in birthdays:
  print(pers)
birthday_input = input("\nwho's birthday do you want to know?? ")

if birthday_input in birthdays:
  print(birthday_input + "'s birthday is:",birthdays[birthday_input])
else:
  print("sorry, we don't have that person")
    
    
      
    

Get all values from the dictionary and add them to a list but don’t add duplicates


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
[47, 52, 44, 53, 54]

Hint: speed.values() gives you all the values in a dictionary
''' 
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
[47, 52, 44, 53, 54]
values = []
for v in speed.values():
  if v not in values:
    values.append(v)
  else:
    continue
print(values)
  