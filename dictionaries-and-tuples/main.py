'''
t1 = ("hi","hello")
print(t1)

print(t1[1])

#t1[1] = "hey"
my_list = [1,2,3]
my_list[1] = 6
print(my_list)

t2 = ("red","orange","yellow","green","blue","purple","brown","pink")
print(t2[2:5])

d1 = {'one':1,'two':2,'three':3}
d2 = {"run":"running","walk":"walking","swim":"swimming"}
d3 = {"?":"question mark","()":"round brackets","+":"plus symbol"}
print(d1)
print(len(d2))

print(d3["+"])
d3["$"] = "dollar sign"
print(d3)

d1.update({'four':4,'five':5,'six':6})
print(d1)

del d2["run"]
print(d2)

removed1 = d3.pop("?","not found")
print(removed1)
removed2 = d3.pop('/',"not found")
print(removed2)

d1['one'] = "uno"
print(d1)

fruit = {}

def add_one(index):
  if index in fruit:
    fruit[index]+=1
  else:
    fruit[index] = 1

add_one('Apple')
add_one('Banana')
add_one('apple')
print(len(fruit))
'''

a = {(1,2):1,(2,3):2}
print(a[1,2])