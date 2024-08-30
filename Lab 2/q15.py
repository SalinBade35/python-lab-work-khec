#an extra day is added to the calendar almost every four years as february 29, and the dau is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# in the Gregorian calendar, three conditions are used to identify leap years:
# 1. year can be evenly divided by 4, is a leap year, unless.
# 2. year can be evenly divided by 100, it is not a leap year, unless:
# 3. year is also evenly divisible by 400. then it is a leap year.


year = int(input("entre year : "))

print((year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)))
