def number_length(nums):
	count = 0 
	for num in str(nums):
		count +=1
	return count
		
def fizz_buzz(num):
	if int(num%3) == 0 and int(num%5) == 0:
		return "FizzBuzz"
	elif int(num%3) == 0:
		return "Fizz"
	elif int(num%5) == 0:
		return "Buzz"
	else:
		return str(num)
	