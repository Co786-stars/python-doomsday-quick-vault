# Easy way to print full pyramid pattern with without space practice

# ------*
# -----***
# ----*****
# ---*******
# --*********

x = 5
c = 1
for i in range(1, x+1):
    print("-"*(x-i+2), end="")
    # print("*"*(2*c-1))
    print("*"*(2*i - 1))
    c += 1



# Full pyramid without with without space using function practice

num1 = int(input("Enter your row number : "))
def Full_pattern_printing(user):
    """full pyramid pattern"""
    s = num1
    X = 1
    for i in range(1, num1+1):

        for j in range(1, s+1):
            print("-", end="")

        # for k in range(1, i*2):
        for k in range(1, X+1):
            print("*", end="")
        X += 2
        s -= 1
        print()
number = num1
Full_pattern_printing(number)




num = int(input("Enter the row number for inverted pyramid : "))
def inverted_pattern(G_num1):
    s = (2*G_num1-1)
    for i in range(1, G_num1+1):

        for j in range(1, i+1):
            print("-", end="")

        for k in range(1, s+1):
            print("*", end="")
        s -= 2
        print()
inverted_pattern(G_num1 = num)

# Inverted Half pyramid pattern using function
num2 = int(input("Enter the row number for inverted pyramid : ")) # 5
def inverted_alpha_pyramid(u_value):
    c = (2*u_value-1)  # c =  9 7 5 3 1
    for i in range(1, u_value+1): # i = 1 to 6 >> 1 2 3 4

        for j in range(1, i+1): #  j =  1 to 2 >> 1, j = 1 to 3 >> 1 2, j = 1 to 5 >> 1  2  3 4, j = 1 to 6 >> 1 2 3 4 5
            print("-", end="")

        for k in range(1, c+1): # k = 1 to 10 >> 1 2 3 4 5 6 7 8 9, k = 1 to 8 >> 1 2 3 4 5 6 7, 1 to 6 >> 1 2 3 4 5
            alpha = chr(64+k)   # k = 1 to 4 >>  1 2 3, 1 to 2 >>  1
            print(f"{alpha}", end="")
        c -= 2
        print()
inverted_alpha_pyramid(u_value=num2)

# output : -ABCDEFGHI
#          --ABCDEFH
#          ---ABCDE
#          ----ABC
#          -----A


# Inverted numeric full pyramid without using function
x = int(input("Enter the row number for numeric pattern printing : "))
count = 2*x-1
for i in range(1, x+1):

    for j in range(1, i+1):
        print("-", end="")

    for k in range(1, count+1):
        print(f"{k}", end="")
    count -= 2
    print()
