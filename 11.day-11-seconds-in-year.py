############################ My solution ############################

print("How many seconds are in a year?")
print()
year = int(input("Please enter enter year starting from 0: "))
isLeap = input("Is it leap year? Y/N: ")
print()

if isLeap == "Y" or isLeap == "y":
    days = 366
else:
    days = 365

seconds = days * 24 * 60 * 60

print("In year", year, "there are", seconds, "seconds")


########################## Replit solution ###########################

days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute


if days_this_year == 366:
    print("Number of seconds in a leap year are", leapyear_result)
else:
    print("Number of seconds in a year are", result)
