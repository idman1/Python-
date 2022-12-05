first_largest_number = float("-inf")
second_largest_number = float("-inf")
number_of_prompt = 0

while number_of_prompt < 3:
    num = float(input("enter a number: "))
    if num > first_largest_number:
        second_largest_number = num
        first_largest_number = second_largest_number
    elif num < second_largest_number:
        first_largest_number = num
    number_of_prompt += 1
print(first_largest_number, "first_largest_number", second_largest_number, "second_largest_number")
