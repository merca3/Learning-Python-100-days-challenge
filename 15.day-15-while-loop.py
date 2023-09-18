exit = ""
while exit != "yes":
    animal = input("What animal do you want?: ")
    if animal == "cow":
        print("A cow goes moo.")
    elif animal == "a lesser spotted lemur":
        print("Ummm...the Lesser Spotter Lemur goes awooga.")
    elif animal == "dog":
        print("A dog goes woof.")
    elif animal == "cat":
        print("A cat goes meow.")
    elif animal == "pig":
        print("A pig goes oink.")
    else:
        print("We don't know how", animal, "goes...")
    exit = input("Exit?: ")
