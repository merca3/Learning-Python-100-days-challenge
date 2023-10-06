import random

print("⚔️ Character Stats Generator ⚔️")
print()


def rollDice(sides):
    result = random.randint(1, sides)
    return result


def getHealth():
    num1 = rollDice(6)
    num2 = rollDice(8)
    return num1 * num2


answer = ""
while answer != "no":
    character = input("Name your warrior: ")
    print("Health of", character, "is: ", getHealth(), "hp")
    answer = input("Do you want to create another character? ")
    print()
