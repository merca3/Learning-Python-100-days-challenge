print("Hi there!")
name = input("What is your name? ")
day = input("What day of the week is it? ")
hobby = input("What do you like to do on a weekend? ")
print()

if name == "Kate" or name == "kate":
    print("Hi", name, "!")
    if day == "monday":
        niceWeekend = input("Did you have a nice weekend? ")
        if niceWeekend == "yes":
            print("Glad to hear that!")
        else:
            print("I'm sure next one will be amazing!")
    elif day == "friday":
        print("Weekend is almost here!")
        print("Do you have some time reserved for", hobby, "?")
elif name == "Andrea" or name == "andrea":
    print("Ciao", name, "!")
    if day == "tuesday":
        print("It's", day, "today, do you rememer about your doctors appointment?")
    elif day == "thursday":
        print("It's gym day!")
    else:
        print("No plans for you today!")
else:
    print("Something went wrong or there are no messages for you!")
