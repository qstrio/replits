def hello_name(name):
  return 'Hello ' + name + "!"
  
def extra_end(stri):
  end = len(stri) -2
  end2 = len(stri)
  return stri[end:end2]*3

def left2(st):
  end = len(st)
  return st[2:end] + st[0:2]

def double_char(string):
  for char in range(len(string)):
    return string[char]*2

def count_hi(str):
  count = 0
  for char in range(len(str)-1):
    if str[char:char+2] == 'hi':
      count += 1
  return count


  
  

  

  


  
  
  
  
