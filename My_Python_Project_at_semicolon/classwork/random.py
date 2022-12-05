import random

number_to_be_guessed = random.randint(1, 100)
number_to_be_guesses = 0


while number_to_be_guesses <= 2:
    num = int(input("please guess a number: "))
    if num == number_to_be_guessed:
        print("you got it right")
        break
    else:
        print("wrong guess")
    if number_to_be_guesses == 2:
        print("Try again later, its unfortunate you cloud not guess right", number_to_be_guessed)

    number_to_be_guesses += 1
