"""Dimoand pattern Question very important """

# ---------*
# -------* * *
# -----* * * * *
# ---* * * * * * *
# -* * * * * * * * *
# ---* * * * * * *
# -----* * * * *
# -------* * *
# ---------* 

def dimoand_pyramid_pattern(user):
    """Dimoand pyramid pattern"""
    x = user
    y = x
    for row in range(1, user+1): # outer loop 
        if row < user/2:    
            for space in range(1, x+1): # inner loop for column
                print("-", end="")
        else:
            for space in range(1, 2*row-user+1): # Inner loop for column
                print("-", end="") 
        
        if row < user/2:
            for column in range(1, 2*row):
                print("*", end=" ")
        else:
            for column in range(1, y+1):
                print("*", end=" ")
            y = y-2
        x = x-2
        print()
num = int(input("User input : "))
if num%2 == 1:
    dimoand_pyramid_pattern(num)
else:
    num +=1
    dimoand_pyramid_pattern(num)



# --------- 1
# ------- 1 2 3
# ----- 1 2 3 4 5
# --- 1 2 3 4 5 6 7
# - 1 2 3 4 5 6 7 8 9
# --- 1 2 3 4 5 6 7
# ----- 1 2 3 4 5
# ------- 1 2 3
# --------- 1

def numeric_diamond_pattern(user_value):
    """numeric diamond pattern"""
    us = user_value  # upper_space row from 1st to 5th
    for i in range(1, user_value+1):  # 1 2 3 4 5 6  7 8 9 >> outerloop

        if i < 6:   # condition that check upper space 1st to 5th
            for j in range(1, us+1):  # inner loop for space
                print("-", end="")

        else:       # condition that use to check the space 6th to 9th
            for j in range(1, 2*i-user_value+1):   # inner loop for space
                print("-", end="")

        if i < 6:   # condition that check upper numbers 1st to 5th
            for k in range(1, 2*i):   # internal loop use for numbers
                print(f"{k}", end=" ")

        else:    # condition that check upper number 1st to 5th
            for k in range(1, user_value+us):  # internal loop use for numbers second logic
                print(f"{k}", end=" ")

        print()
        us -= 2
input_value = 9
numeric_diamond_pattern(input_value)


# ---------A
# -------A B C
# -----A B C D E
# ---A B C D E F G
# -A B C D E F G H I
# ---A B C D E F G
# -----A B C D E
# -------A B C
# ---------A
def alpha_diamond_pattern(user_value, alpha_num):
    """Alphabet diamond pattern"""
    spc = user_value
    for x in range(1, user_value+1):  #  x >> 1 2 3 4 5 6 7 8 9
        if x < 5:
            for y in range(1, spc+1):
                print("-", end="")
        else:
            for y in range(1, 2*x-user_value+1):
                print("-", end="")

        if x < 6:
            for z in range(1, 2*x):
                print(f"{chr(alpha_num+z)}", end=" ")
        else:
            for z in range(1, user_value+spc):  # -1 -3 -5 -7
                print(f"{chr(alpha_num+z)}", end=" ")
        spc -= 2  # 9 7 5 3 2 1 -1
        print()

alpha_diamond_pattern(9, 64)

