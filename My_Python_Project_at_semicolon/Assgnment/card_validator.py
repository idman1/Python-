card_number = input("enter card number: ")


def even_double_digits(credit_card_number):
    total_sum_of_even_digits = 0
    for i in range(len(credit_card_number) - 2, -1, -2):
        sum_even = int(credit_card_number[i]) * 2
        if sum_even > 9:
            new_sum = sum_even % 10 + sum_even // 10
            total_sum_of_even_digits += new_sum
        else:
            total_sum_of_even_digits += sum_even
    return total_sum_of_even_digits


def odd_digits(credit_card_number):
    total_odd = 0
    for i in range(len(credit_card_number) - 1, -1, -2):
        total_odd += int(credit_card_number[i])
    return total_odd


result_of_digits = odd_digits(card_number) + even_double_digits(card_number)
if result_of_digits % 10 == 0:
    print("Card is valid")
else:
    print("Card is invalid")


def length_validity(credit_card_number):
    if len(credit_card_number) < 13 or len(credit_card_number) > 16:
        return "invalid"
    else:
        return "valid"


print("****Card length: " + length_validity(card_number))
print("****Credit Card Number: " + card_number)
print(f"****Credit Card Digit Length {+len(card_number)}")