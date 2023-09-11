print("What kind of music do you like?")
genre = input("Choose one from those: trance / pop / rock ")
print()

if genre == "trance":
    print("Best music ever, right?")
    favArtist = input("Do you have favorite producer? ")
    if favArtist == "Armin van Buuren":
        print("Armin is the king of trance! Good choice!")
    else:
        print("Good one, but Armin is better!")
elif genre == "pop":
    print("Pop is pretty common choice :)")
elif genre == "rock":
    print("Rock is always a classic!")
else:
    print("Nice to see that there are other favorite music genres!")
