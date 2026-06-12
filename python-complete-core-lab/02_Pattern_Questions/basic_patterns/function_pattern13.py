#HOLLOW SQUARE PATTERN
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# Numeric Hollow Square pattern
def square_pattern(value1):
    # for row of the square
    for i in range(1, value1+1):
        # column of the square
        for j in range(1, value1+1):
            # to full-fill condition of square
            if i == value1 or i == 1 or j == 1 or j == value1:
                print(f"{j}", end=" ")
            # to give space between the square
            else:
                print("-", end=" ")
        print()
x = int(input("Inter your number : "))
if x < 10:
    square_pattern(value1=x)
else:
    print("pls enter number smaller then ten")
# value1 = 5
# i = 1 to 5 >>    1 2 3 4 5 false
# j = 1 to 5 >>    1 2 3 4 5 false :  1 to 5 >> 1 2 3 4 5 false  : 1 to 5 >> 1 2 3 4 5 false
#     1 to 5 >>    1 2 3 4 5 false :  1 to 5 >> 1 2 3 4 5 fase

#  1 1 1 1 1
#  2 - - - 2
#  3 - - - 3
#  4 - - - 4
#  5 5 5 5 5



# Star Hollow square pattern
def hollow_square_pattern(user):
    """ this is star hollow square pattern """
    for i in range(user):
        for j in range(user):
            if j == 0 or i == 0 or i == (user-1) or j == (user-1):
                print("*", end=" ")
            else:
                print("-", end=" ")
        print()

y  = int(input("Enter the row number for hollow square pattern : "))
hollow_square_pattern(user=y)
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *




# Star hallow square using while loop with help of function

x = int(input("Enter Row number for matrix hollow pattern : "))
i = 1
while i < x+1:
    j = 1
    while j < x+1:
        if j == 1 or j == x or i == x or i == 1:
            print(f"{chr(64+j)}", end=" ")
        else:
            print(" ", end=" ")
        j += 1
    print()
    i += 1


# A B C D E
# A - - - E
# A - - - E
# A - - - E
# A B C D E

