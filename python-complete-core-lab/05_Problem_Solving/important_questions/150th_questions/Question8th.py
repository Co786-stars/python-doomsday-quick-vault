
# Write a python program to display clender
# __________________________________________________________________________#

import calendar
year = int(input("Enter year : "))
month = int(input("Enter month : "))
cleander = calendar.month(year, month)
print(cleander)

# __________________________________________________________________________#

def calendermolude():
    """function body display the clander functions"""
    y1, y2 = 2000, 2025
    y, m = 2000, 7
    year_range = calendar.leapdays(y1, y2) # Return the total number of leap year b/w y1 to y2
    print("Total number of leap year from 2000 to 2025 is :",year_range)
calendermolude()

# __________________________________________________________________________#

class ClanderMonth:
    def __init__(self, year, month):
        self.c = calendar.month(year, month)
        return print(self.c)
ym = ClanderMonth(2025, 1)

# __________________________________________________________________________#

