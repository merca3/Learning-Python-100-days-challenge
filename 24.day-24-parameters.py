import random

print("Infinity Dice 🎲")
print()
sidesInput = int(input("How many sides?: "))


def rollDice(sides):
    number = random.randint(1, sides)
    print("You rolled", number)
    print()


while True:
    rollDice(sidesInput)
    rollAgain = input("Roll again? ")
    if rollAgain == "no":
        break
