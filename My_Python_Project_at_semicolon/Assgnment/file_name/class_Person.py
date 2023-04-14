from Person import Person

# if __name__ == '__main__':
name = input("Enter name: ")
age = int(input("Enter your age: "))

idris = Person(name, age)

print("your name is: ", idris.get_name(), "your age is: ", idris.get_age())
