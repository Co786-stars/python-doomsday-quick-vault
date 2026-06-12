
# WAPP to check Leap year ?

# _________________________________________________________________________________#

y = int(input("Enter year : "))
# divided by 100 means century year (ending with 00)
# centuary year is divided by 400 is leap year
if (y%400 == 0 and y%100 == 0):
    print("{0} is a leap year".format(y))

# Not divided by 100 means not century year 
# year divided by 4 is a leap year (not century year)
elif (y%4 == 0 and y%100 != 0):
    print("{0} is a leap year".format(y))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is Not a leap year".format(y))

# _________________________________________________________________________________#

def myfun():
    """Function body to check if a year is a leap year or not"""
    year = int(input("Enter year: "))

    if (year % 400 == 0):  # Century year is divisible by 400
        print(f"{year} is a leap year")

    elif (year % 4 == 0 and year % 100 != 0):  # Not divisible by 100 means not a century year
        print(f"{year} is a leap year")       # Divisible by 4 means leap year

    else:
        print(f"{year} is Not a leap year")

myfun()

# _________________________________________________________________________________#

class Year:
    """class body check the leap year or not"""
    def __init__(self):
        """initilize the Year attribute"""
        # A year is a leap year if it is devided by 4 
        # but not divisible 100 unless divisible by 400
        self.Year = int(input("Enter Year : "))
    
    def isleapyear(self):
        """function to dsplay leap year"""
        if (self.Year%4 == 0 and self.Year%100 != 0) or self.Year%400 == 0:
            print(f"The Year {self.Year} is Leap year")
        else:
            print(f"The Year {self.Year} is Not leap year")

obj1 = Year()
obj1.isleapyear()
# _________________________________________________________________________________#
