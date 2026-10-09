import time

# def hanoi(n, a, b, c):
#   if n == 1:
#     print('Move {} {} to {}\n'.format(n, a, c))
#   else:
#     hanoi(n - 1, a, c, b)
#     print('Move {} from {} to {}\n'.format(n, a, c))
#     hanoi(n - 1, b, a, c)

# hanoi(6, 'A', 'B', 'C')

def fibonacci(n):
  if n <= 2:
    return 1
  if n > 2:
    return fibonacci(n - 1) + fibonacci(n - 2)

start = time.time()
print(fibonacci(8))
end = time.time()
print('The time for recursive function is {}'.format(end - start))


def f2(n):
  if n <= 2:
    return 1
  else:
    n1, n2 = 1, 1
    while n > 2:
      output = n1 + n2
      n1 = n2
      n2 = output
      n -= 1
    return output

start = time.time()
print(f2(8))
end = time.time()
print('The time for loop function is {}'.format(end - start))