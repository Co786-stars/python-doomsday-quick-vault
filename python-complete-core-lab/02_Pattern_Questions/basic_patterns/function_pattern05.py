# Simple method Inverted half right pyramid pattern using function

print("Enter the value for Inverted  right half pyramid : -")
value = int(input("Enter the row number : "))
def pattern(x):

    for i in range(1, x+1):
        print("* "*(x-i+1))

pattern(value)

# Inverted half right pyramid pattern using function

print("Enter the value for Inverted left half pyramid : - ")
value = int(input("Enter the row number : "))
def inverted_right_half(row):
    for i in range(1, row+1):
        print("-" * 4, end=" ")
        j = row
        while j >= i:
            print("*", end=" ")
            j -= 1
        print()
inverted_right_half(value)

# Inverted Right half Pyramid pattern using function
print("Pls enter your range of the Inverted right half :- ")
user = int(input("Enter the Row number for pattern : "))
def Inverted_right_half(value1):

    i = 1
    j = 1
    while i < value1+1:
        print(" ", end="")
        while j < i+1:
            print(f"x "*(value1-i+1))
            j += 1
        i += 1
Inverted_right_half(value1=user)


# Numeric right half inverted pattern pyramid using function
ur_input = int(input("Enter the row number for pattern : "))
def numeric_right_half_inverted_pattern_pyramid(x):
    count = x
    for i in range(1, x+1):
        for j in range(1, count+1):
            print(f"{j}", end=" ")
        print()
        count -= 1
numeric_right_half_inverted_pattern_pyramid(ur_input)
# count = 5 4 3 2 1
# i = 1 2 3 4 5
# j = 1 2 3 4 5 >> 1 2 3 4 >> 1 2 3 >> 1 2 >> 1

# output >> 1 2 3 4 5
#           1 2 3 4
#           1 2 3
#           1 2
#           1

# alphabetical Inverted right half pyramid pattern using function

x = int(input("Enter the row number for inverted pyramid patten : "))
def inverted_half_pyramid(arg1, dvalue = 64):
    value = arg1  # arg1 = 5 value = 5 , 4, 3, 2, 1
    for i in range(1, arg1+1):  # i >> 1 to 6 >> 1 2 3 4 5

        for j in range(True+1):  # j >> 1 to 2 : 0 1 >> 0 1 >> 0 1 >> 0 1 >> 0 1
            print("  ", end="")

        for k in range(1, value+1):  # k >> 1 to 6 >> 1  2  3  4  5 ||| 1 to 5 : >>  1 2 3 4 ||| 1 to 4 : >>  1 2 3
            char = chr(dvalue+k)     # k >> 1 to 3 : >> 1 2 ||| 1 to 2 : >> 1
            print(char, end=" ")
        value -= 1
        print()

inverted_half_pyramid(x)
# output =  --A B C D E
#           --A B C D
#           --A B C
#           --A B
#           --A