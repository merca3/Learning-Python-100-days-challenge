print("Guess the number between 1 and 1,000,000!")

number = 55
counter = 0

while True:
    counter += 1
    print()
    guess = int(input("Enter your guess: "))
    if guess < 0:
        print("Please enter positive numbers only next time...")
        exit()
    elif guess == number:
        print("You guessed it right - congratulations!")
        print("It took you only", counter, "tries to guess the number!")
        break
    elif guess > number:
        print("Your number is too high")
    else:
        print("Your number is too low")
