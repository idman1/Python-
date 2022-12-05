hello = "hello there!!!"
#print(hello.find("llo"))
#print(hello.rfind("o", 3))
#print(hello.index("a"))
#found = 0
#while True:
#    found = hello.find("e",found)
 #   if found == -1:
   #     break
   # print(found)

   # found+=

#print(hello.find(found))
print(hello.upper())
print(hello.swapcase())
print(hello.count("e"))
print(hello.title())
print(hello.format())
print(hello.capitalize())
print(hello.lower())
print(hello.rfind("y"))
print(hello.center(20, "*"))

for i in range(1, 21, 2):
    stert = "!" * i
    #print(stert.rjust(20))
    print(stert.center(20))

bin_ = "101101010101*****101010!!!!101010#&#"
print(bin_.replace("1", "x").replace("0", "1").replace("x", "0"))
print(bin_.translate(str.maketrans("01", "10", "8#!*&")))


