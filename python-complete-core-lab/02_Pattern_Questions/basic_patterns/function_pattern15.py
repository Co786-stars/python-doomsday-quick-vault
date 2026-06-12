def hollow_inverted_pattern(value):
    """hollow inverted full pyramid pattern"""
    x = 2*value-1
    for row in range(1, value+1):

        for space in range(1, 2*row):
            print(" ", end="")
        
        for col in range(1, x+1):
            if row == 1 or col == 1 or col==x:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        x -= 2
        print()

# user = int(input("Enter your row number : "))
hollow_inverted_pattern(5)

# x = 9 >> 7 >> 5 >> 3 >> 1
# row = 1 to 6 >> 1 2 3 4 5 false
# spa = 1 to 2 >> [ 1 ] >> 1 to 4 >> [ 1 2 3 ] >> 1 to 6 >> [ 1 2 3 4 5 ] 
#       1 to 8 >> [ 1 2 3 4 5 6 7 ]  >> 1 to 9 >> [ 1 2 3 4 5 6 7 8 9 ]
# col = 1 to 9 >> 1 2 3 4 5 6 7 8 9 >> 1 to 8 >> 1 2 3 4 5 6 7
#       1 to 6 >> 1 2 3 4 5 >> 1 to 4 >> 1 2 3 >> 1 to 2 >> 1 

# out = -*-*-*-*-*-*-*-*-*-
#       ---*-*-*-*-*-*-*-
#       -----*-*-*-*-*-
#       -------*-*-*-
#       ---------*-

print("\n")

def hollow_inverted_numeric_pattern(value1):
    y = 2*value1-1
    for i in range(1, value1+1):

        for j in range(1, 2*i):
            print("-", end="")
        
        for k in range(1, y+1):
            if i == 1 or k == 1 or k == y:
                print(f"{k}", end=" ")
            else:
                print(f" ", end=" ")
        y -= 2
        print()


hollow_inverted_numeric_pattern(5)


print("\n")

def alpha_hollow_numeric_pattern(user, num):
    """Alphabet hollow inverted pyramid pattern"""
    hollow = 2*user-1
    for row in range(1, user+1): #  1 2 3 4 5
        
        for space in range(1, 2*row): # 1 >> 1 2 3 >> 1 2 3 4 5 >> 1 2 3 4 5 6 7 >> 1 2 3 4 5 6 7 8 9
            print("-", end="")
        
        for col in range(1, hollow+1): # 1 2 3 4 5 6 7 8 9 >>  1 2 3 4 5 6 7 >> 1 2 3 4 5 >> 1 2 3 >> 1
            if col == 1 or row == 1 or col == hollow:
                print(f"{chr(num+col)}", end=" ")
            else:
                print(" ", end=" ")
        hollow -= 2 # >> 7 >> 5 >> 3 >> 1 >> -1
        print()

alpha_hollow_numeric_pattern(5, 64)

# -A-B-C-D-E-F-G-H-I-
# ---A-B-C-D-E-F-G- 
# -----A-B-C-D-E-
# -------A-B-C-
# ---------A-