def do_twice(f,x):
  f(x)
  f(x)
  
def print_twice(n):
  print(n)
  print(n)
 
def do_four(func,a):
  do_twice(func,a)
  do_twice(func,a)

do_four(print_twice,'hi')
  
  




  
  