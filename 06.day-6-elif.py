print("Welcome to login page!")
username = input("Please enter your Username: ")
password = input("Please enter your Password: ")
print()

if username == "john.doe" and password == "password123":
    print("Welcome, Joe!")
elif username == "kate.moss" and password == "kate123":
    print("Hi, Kate!")
elif username == "johny.depp" and password == "pirate001":
    print("Nice to see you back, Johny!")
else:
    print("Username or password are incorrect!")
