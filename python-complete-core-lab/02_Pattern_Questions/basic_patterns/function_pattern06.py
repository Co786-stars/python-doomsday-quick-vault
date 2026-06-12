# Inverted left half pyramid pattern
def left_half_pyramid(x):
    s = 1
    a = x
    for i in range(1, x+1):

        for j in range(1, s+1):   # first of all print the space of pattern
            print("-", end="")

        for j in range(1, a+1):   # and then print the asterisk of pattern
            print("*", end=" ")
        a -= 1
        s += 2
        print()
left_half_pyramid(5)

"""# i = 1:6 >> 1 2 3 4 5
# j = 1:2 | 1:4 | 1:6 | 1:8 | 1: 10>> 1 >> 1 2 3 >> 1 2 3 4 5 >> 1 2 3 4 5 6 7
# s = 1 3 5 7 9 11
# output >> -* * * * *
#        >> ---* * * *
#        >> -----* * *
#        >> -------* *
#        >> ---------*
"""
# Inverted alphabetical left half pyramid pattern without function

print("Enter the number for printing Inverted left half pyramid pattern : -")
num1 = int(input("Enter the Row number of the pattern : "))
i = 1
k = 1
while i < num1+1:
    j = 1

    while j < k+1:
        print("-", end="")
        j += 1

    l = 1
    while l < (num1-i+1)+1:
        c_num = chr(64+l)
        print(f"{c_num}", end=" ")
        l += 1

    print()
    i += 1
    k += 2


# Inverted numeric left half pyramid pattern without function
def inverted_left_half_pyramid_pattern(g_value):
    """Inverted left half pyramid pattern"""
    s = g_value
    for i in range(1, g_value+1):

        for j in range(1, s+1):
            print(" ", end="")

        for k in range(1, (g_value-i+1)+1):
            print(k, end=" ")
        s += 2
        print()
print("Enter the value for nverted left half pyramid pattern : -")
user = int(input("Enter the row number for pattern : "))
inverted_left_half_pyramid_pattern(user)

