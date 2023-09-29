correct_username = "david"
correct_password = "baldies4life"


def login():
    while True:
        username = input("What is your username?: ")
        password = input("What is your password?: ")
        print()

        if username == correct_username and password == correct_password:
            print("Welcome to Replit!")
            break
        else:
            print("Whoops! I don't recognize that username or password. Try again!")
            print()
            continue


print("Replit Login Systen")
print()
login()
