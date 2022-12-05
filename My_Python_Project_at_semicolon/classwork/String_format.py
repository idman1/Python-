name = "idris"
age = 18
s = "{0:^20} is {1:>20.2f} years old,and {0} loves {2}".format(name,age,"java")
s = a = f"{name:^20} is {1:>20.2f} years old,and {0} loves {2}""java"
print(s)
print(a)

hello = "hello world"
for index, letter in enumerate(hello, start=1):
    print(f"{index} ----->{letter}")

for i in range(2, 21, 2):
    s="*"*i
    print(f"{s:20} {s:^20} {s:>20}")

s = "hello wolrd"
to_be_found = "l"
for i in range(len(s)):

    if s[i] == to_be_found:
        print(f"{s[i]} was found at index {i}")
        break
    else:
        print(f"sorry i could not find {to_be_found}")

for index, letter in enumerate(s):

    if letter == to_be_found:
        print(f"{letter} found at index {index}")
