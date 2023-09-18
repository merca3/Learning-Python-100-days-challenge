from getpass import getpass as input

print("E P I C    \U0001FAA8 | \U0001F4C4 | ✂️    B A T T L E!")
print()
print("Select your move (R, P or S)")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
print()

if player1 == player2:
    print("It's a tie!")
elif player1 == "R":
    if player2 == "P":
        print("Player's 1 Rock is smothered by Player's 2 Paper!")
    elif player2 == "S":
        print("Player's 1 Rock won Player's 2 Scissors!")
elif player1 == "P":
    if player2 == "R":
        print("Player's 2 Rock is smothered by Player's 1 Paper!")
    elif player2 == "S":
        print("Player's 1 Paper was cut by Player's 2 Scissors!")
elif player1 == "S":
    if player2 == "R":
        print("Player's 1 Scissors got broken by Player's 2 Rock!")
    elif player2 == "P":
        print("Player's 2 Paper was cut by Player's 1 Scissors!")
else:
    print("Something went wrong, try again!")
