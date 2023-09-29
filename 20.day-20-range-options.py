print("Let a computer count for you!")
print()
startAt = int(input("Please enter a number from which you want to start: "))
endBefore = int(input("Please enter a number before which you want to end: "))
increment = int(input("Please enter increment between values: "))
print()

for i in range(startAt, endBefore, increment):
    print(i)
