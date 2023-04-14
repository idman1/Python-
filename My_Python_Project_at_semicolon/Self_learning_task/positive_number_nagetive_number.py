positive = 0
negative = 0
total = 0
user_input = int(input("Enter a number and use and Enter 0 to Exit "))
while user_input != 0:
    user_input = int(input(""))
    if user_input > 0:
        positive += 1
    elif user_input < 0:
        negative += 1
    if user_input == user_input:
        total = total + user_input

sum_up = positive + negative
avearge = sum_up / total
print("number of positive number enter is: ", positive)
print("number of negative number enter is", negative)
print(f"The total is : ", sum_up)
print("the average is: ", avearge)
