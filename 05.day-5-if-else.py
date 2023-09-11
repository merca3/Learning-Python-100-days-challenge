print("Which character are you from 'Avengers?'")
print()
print("Answer these questions with Yes/No and let's find out.")
print()

hangingAround = input("Do you like 'hanging around'?: ")
if hangingAround == "No":
    print("Then you are not Spider-Man!")

gravellyVoice = input("Do you have a 'gravelly' voice?: ")
if gravellyVoice == "No":
    print("Aww, then you're not Korg")

feelingMarvelous = input("Do you often feel 'Marvelous'?: ")
if feelingMarvelous == "Yes":
    print("Aha! You're Captain Marvel! Hi!")
else:
    print("I guess you are not like anyone from 'Avengers.'")
