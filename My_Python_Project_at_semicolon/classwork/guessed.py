import random

number_to_be_guess = random.randint(1, 3)
number_to_be_guessed = 0

while number_to_be_guessed <= 6:
    num = int(input("enter your guessing number: "))
    if num == number_to_be_guess:
        print("congratulation you have guess the right number")
    else:
        print("unfortunate you have enter wrong number")
    number_to_be_guessed += 1
