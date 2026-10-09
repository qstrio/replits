# big ideas:
# functions are named, reusable blocks of code

def say_hello():
  print("Hello")

def say_hello_to(name):
  print(f"Hello {name}!")

def clean_input():
  return input().lower().strip(",.?!")

def add_two(num):
  print(num+2)

# create a function called say_hello_to
# -print(hello{name})

say_hello()
say_hello()
say_hello_to("james")
say_hello_to("as")
say_hello_to("fasdageg")
print("Typically, what's the color of the sky?")
user_answer = input().lower().strip("!?/.,")
if user_answer  == "blue":
  print("You are right!")
else:
  print("sorry, you are wrong.")

print("what's 10x10?")
user_answer = clean_input()
if user_answer in[100, "one hundred", "one-hundred"]:
  print("yay")
else:
  print("nay")

add_two(6)