print("Generation generator")
print()
print("Are you aware to which generation you belong? Let's find out!")
year = int(input("Please enter the year you were born: "))

if year >= 1925 and year <= 1946:
    print("You are one from Traditionalists!")
elif year >= 1947 and year <= 1964:
    print("You are one from Baby Boomers!")
elif year >= 1965 and year <= 1981:
    print("You belong to Generation X!")
elif year >= 1982 and year <= 1995:
    print("You belong to Millenials!")
elif year >= 1996 and year <= 2015:
    print("You belong to Generation Z!")
else:
    print("We don't know the name of generation for this year")


myPi = float(input("What is Pi to 3dp?"))
if myPi == 3.142:
    print("Exactly!")
else:
    print("Try again 😭")
