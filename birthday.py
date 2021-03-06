"""
birthday.py
Author: Peter Bynum
Credit: None
Assignment: Birthday Quiz

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonthnum = datetime.today().month
todaydate = datetime.today().day
todaymonth = month_name[todaymonthnum]

name = input("Hello, what is your name? ")
month = input(("Hi {0}, what was the name of the month you were born in? ").format(name))
year = input(("And what year were you born in, {0}? ").format(name))
day = input("And the day? ")

if month == "October" and day == "31":
    print("You were born on Halloween!")
elif month == todaymonth and day == str(todaydate):
    print("Happy birthday!")
else:
    if month == "December" or month == "January" or month == "February":
        season = "winter"
        if int(year) >= 2000 and int(year) <= 2016:
            age = "two thousands"
        elif int(year) >= 1990 and int(year) < 2000:
            age = "nineties"
        elif int(year) >= 1980 and int(year) <1990:
            age = "eighties"
        else:
            age = "Stone Age"
    elif month == "March" or month == "April" or month == "May":
        season = "spring"
        if int(year) >= 2000 and int(year) <= 2016:
            age = "two thousands"
        elif int(year) >= 1990 and int(year) < 2000:
            age = "nineties"
        elif int(year) >= 1980 and int(year) <1990:
            age = "eighties"
        else:
            age = "Stone Age"
    elif month == "June" or month == "July" or month == "August":
        season = "summer"
        if int(year) >= 2000 and int(year) <= 2016:
            age = "two thousands"
        elif int(year) >= 1990 and int(year) < 2000:
            age = "nineties"
        elif int(year) >= 1980 and int(year) <1990:
            age = "eighties"
        else:
            age = "Stone Age"
    else:
        season = "fall"
        if int(year) >= 2000 and int(year) <= 2016:
            age = "two thousands"
        elif int(year) >= 1990 and int(year) < 2000:
            age = "nineties"
        elif int(year) >= 1980 and int(year) <1990:
            age = "eighties"
        else:
            age = "Stone Age"
    print(("{0}, you are a {1} baby of the {2}.").format(name, season, age))





