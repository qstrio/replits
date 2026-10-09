def detect_word(str):
	word = ""
	for letter in str:
		if letter.islower():
			word += letter
	return word	

print(detect_word("UcUNFYGaFYFYGtNUH"))
print(detect_word("bEEFGBuFBRrHgUHlNFYaYr"))

# no idea for the second one, i looked up resources and they all used lambda (what is lambda)