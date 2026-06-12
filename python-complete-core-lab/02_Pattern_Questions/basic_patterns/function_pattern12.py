# HOURGLASS PATTERN
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

def Hollow_pattern(user):
    """Hollow_pattern"""
    spc = 2*user-1
    asp = user
    for row in range(1, user+1): # outer loop use to count the row  1 2 3 4 5 6 7 8 9

        if row < user/2:  # condition control upper pyramid
            for space in range(1, 2*row):  # inner loop use to count 1st to 5th space
                print("-", end="")
        else:     # condition control lower pyramid
            for space in range(1, spc+1):  # inner loop use to count 6th to 9th space
                print("-", end="")
        if row < user/2:
            for col in range(1, asp+1):
                print("*", end=" ")
        else:
            for col in range(1, -1*(asp-2)+1):  # 4  6 8 9 internal loop for  
                print("*", end=" ")
        asp -= 2  # 9 7 5 3 1 :: -1 -3 -5 -7
        spc -= 2  # space :: if 17  15  13  11  9  :: else 7 5 3 1
        print()

Hollow_pattern(17)


""" Numeric hallow pattern """ 

# -1 2 3 4 5 6 7 8 9
# ---1 2 3 4 5 6 7
# -----1 2 3 4 5
# -------1 2 3
# ---------1
# -------1 2 3
# -----1 2 3 4 5
# ---1 2 3 4 5 6 7
# -1 2 3 4 5 6 7 8 9


def Hallow_pattern(value):
    x = y = value
    for i in range(1, value+1):

        if i < value/2:
            for j in range(1, 2*i):
                print("", end=" ")

            for k in range(1, y+1):
                print(f"{k}", end=" ")
            y -= 2
        else:
            for j in range(1, x+1):
                print("", end=" ")

            for k in range(1, 2*i-value+1): 
                print(f"{k}", end=" ")

            x -= 2
        print()

user = int(input("Enter the row number : "))
if user%2==1:
    Hallow_pattern(user)
else:
    user += 1
    Hallow_pattern(user)




# alphabet Hollow pattern without using function

# -A B C D E F G H I
# ---A B C D E F G
# -----A B C D E
# -------A B C
# ---------A
# -------A B C
# -----A B C D E
# ---A B C D E F G
# -A B C D E F G H I

user = int(input("Enter row number : "))
lsp = user
for i in range(1, user+1):

    if i < 5:
        for j in range(1, 2*i):
            print("-", end="")

    else:
        for j in range(1, lsp+1):
            print("-", end="")
        lsp -= 2

    if i < 6:
        for k in range(1, (user-2*i)+3): # -1 -3 -5 -7 -9
            print(f"{chr(64 + k)}", end=" ")
    else:
        for k in range(1, 2*i-user+1):
            print(f"{chr(64+k)}", end=" ")
    print()


