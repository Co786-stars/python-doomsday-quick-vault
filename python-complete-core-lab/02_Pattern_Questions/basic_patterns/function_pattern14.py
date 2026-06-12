# HOLLOW FULL PYRAMID PATTER : --

#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *


def hollow_full_pyramid(num):
    """ This is Hollow full pyramid pattern"""
    x = 2*num-1
    for i in range(1, num+1):
        for j in range(1, x+1):
            print(" ", end="")

        for k in range(1, 2*i):
            if k == 1 or i == num or k == 2*i-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        x -= 2
        print()
hollow_full_pyramid(5)


# HOLLOW FULL PYRAMID NUMERIC PATTERN : -

#         1
#       1   3
#     1       5
#   1           7
# 1 2 3 4 5 6 7 8 9


def hollow_pattern(arg1):
    """ This is function body for numeric hollow pattern """
    x = arg1*2-1
    for i in range(1, arg1+1):
        
        for j in range(1, x):
            print("-", end="")
        x -= 2
        for k in range(1, 2*i):
            if k == 1 or i==arg1 or k == 2*i-1:
                print(f"{k}", end=" ")
            else:
                print(f" ", end=" ")
        print()


hollow_pattern(5)


# HOLLOW FULL NUMERIC PYRAMID PATTERN 
 
def hollow_pattern2(arg3):
    """alpha hollow gram pattern"""
    arg4 = 2*arg3-1
    for row in range(1, arg3+1):
        
        for col in range(1, arg4+1):
            print(f" ", end="")
        arg4 -= 2
        
        for astrisk in range(1, 2*row):
            if astrisk == 2*row-1 or astrisk == 1 or row == arg3:
                print(f"{chr(64 + astrisk)}", end=" ")
            else:
                print(" ", end=" ")
        print()

hollow_pattern2(5)

