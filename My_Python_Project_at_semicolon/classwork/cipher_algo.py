import string
user_input = input("Enter the word to encode: ")

key = int(input("what key would you like to use: "))

lower_letter = string.ascii_lowercase
upper_letter = string.ascii_uppercase
decoded_upper_letter = lower_letter[key:] + lower_letter[:key]
decoded_lower_letter = upper_letter[key:] + upper_letter[:key]

letters = lower_letter + upper_letter + string.whitespace
decoder_letters = decoded_lower_letter + decoded_upper_letter + string.whitespace
encoded = user_input.translate(str.maketrans(letters, decoder_letters))
decoded = encoded.translate(str.maketrans(decoder_letters, letters))
decoded_letter = decoded_lower_letter + decoded_upper_letter+string.whitespace

print(encoded)
print(decoded)


#print(user_input.translate(str.maketrans(lower_letter+" ", decoded_lower_letter+" ")))


