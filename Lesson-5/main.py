# Write a function, that takes a percent (int) as an argument. The function should print out the letter grade for the corresponding percent
# A = 86-100
# B = 73-85
# C = 60-72
# D = 50 -71
# Fail = anything less than 50
# in the case that you get bad input, just print a message

def grading(n):
  if n>=86 and n<=100:
    return 'A'
  elif n>=73 and n<=85:
    print('B')
  elif n>=60 and n<=72:
    print('C')
  elif n>=50 and n<=71:
    print('D')
  elif n>=0 and n<=50:
    print('fail')
  else:
    print('unexpected input')


grading(0)
grade = input('Please enter your number grade: ')
print('Your letter grade is ' + grading(int(grade)))

result = input("Please enter your favorite color: ")
print("You said " + result + "!!")


