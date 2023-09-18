print("Grade calculator")
print()
name = input("Please enter the name of the test: ")
max = int(input("Please enter maximum amount of points possible: "))
points = int(input("Please enter amount of received points: "))

grade = round(points / max * 100, 2)

print()

if points > max:
    print("You can get more points than maximum, please correct your input")
elif grade >= 90:
    print("Your score was A+ or", grade, "%")
elif grade >= 80:
    print("Your score was A or", grade, "%")
elif grade >= 70:
    print("Your score was B or", grade, "%")
elif grade >= 60:
    print("Your score was C or", grade, "%")
elif grade >= 50:
    print("Your score was D or", grade, "%")
else:
    print("Your score was U or below 50%")
    print("Precise score:", grade, "%")
