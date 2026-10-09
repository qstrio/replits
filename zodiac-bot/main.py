import time

# Zodiac bot
# Author: sarah
# Date: 12th March 2024

# Tell the user what zodiac animal they are based on their birth  year

print("Hello, I'm ZodiacBot. I'll tell you what your zodiac animal is!")
time.sleep(1.5)

# Ask the user what their birth year is 
birth_year = input("What year were you born?")
time.sleep(2.0)
print("Calculating...")
time.sleep(0.5)
print("Calculating...")
time.sleep(0.5)
print("Calculating...")
# Rats - 1948, 60, 72, 84, 96, 2008, 20, 32

if birth_year in ["1948", "1960", "1972", "1984", "1996", "2008", "2020", "2032"]:
  print("I have calculated that you are a rat!")
elif birth_year in ["1949", "1961", "1973", "1985", "1997", "2009", "2021", "2033"]:
  print("You are strong like an ox!")
elif birth_year in ["1950", "1962", "1974", "1986", "1998", "2010", "2022", "2034"]:
  print("You are a courageous tiger!")
else:
  print(f"Sorry, I don't know what {birth_year} means.")

time.sleep(1.5)
print("Thank you for using ZodiacBot!")