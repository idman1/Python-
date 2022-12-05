count = 0
largest_so_far = 0
while count < 5:
    num = int(input("Give me a number: "))
    if num > largest_so_far:
        largest_so_far = num
    count += 1
print("largest numbers so far", largest_so_far)
