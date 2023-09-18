print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")

counter = 0

while True:
    answer = input("Never going to ______ you up.")
    counter += 1
    if answer == "give":
        break
    else:
        print("Nope, try again.")
        print()
print()
print("Well done! It only took you", counter, "attempt(-s).")
