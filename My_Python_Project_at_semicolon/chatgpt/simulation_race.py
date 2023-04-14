import random


class Animal:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self):
        pass

    def has_won(self):
        return self.position >= 70


class Tortoise(Animal):
    def __init__(self):
        super().__init__("Tortoise")
        self.rand = random.Random()

    def move(self):
        random_num = self.rand.randint(1, 10)
        if 1 <= random_num <= 5:
            self.position += 3
        elif 6 <= random_num <= 7:
            self.position -= 6
        else:
            self.position += 1


class Hare(Animal):
    def __init__(self):
        super().__init__("Hare")
        self.rand = random.Random()

    def move(self):
        random_num = self.rand.randint(1, 10)
        if 1 <= random_num <= 2:
            self.position += 9
        elif random_num == 3:
            self.position -= 12
        elif 4 <= random_num <= 5:
            self.position += 1
        elif 8 <= random_num <= 9:
            self.position -= 2


def main():
    # create animal objects
    tortoise = Tortoise()
    hare = Hare()

    # display starting message
    print("BANG !!!!! AND THEY'RE OFF !!!!!\n")

    while True:
        # move animals
        tortoise.move()
        hare.move()

        # check for out of bounds positions
        if tortoise.position < 1:
            tortoise.position = 1
        if hare.position < 1:
            hare.position = 1

        # display race progress
        for i in range(1, 71):
            if i == tortoise.position and i == hare.position:
                print("OUCH!!!", end="")
            elif i == tortoise.position:
                print("T", end="")
            elif i == hare.position:
                print("H", end="")
            else:
                print(" ", end="")
        print()

        # check for winner
        if tortoise.has_won() and hare.has_won():
            print("IT'S A TIE.")
            break
        elif tortoise.has_won():
            print("TORTOISE WINS!!! YAY!!!")
            break
        elif hare.has_won():
            print("HARE WINS. YUCH.")
            break


if __name__ == "__main__":
    main()
