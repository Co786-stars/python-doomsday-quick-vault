#  left half pyramid without function

print(" The given pattern is left half pyramid : -")
x = 5
y = x*2-2
for i in range(1, x+1):
    for j in range(1, y+1):
        print(end="-")
    y = y-2
    for k in range(i):
        print("*", end=" ")
    print()


# numeric left half pyramid with function
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

print("Enter the value for numeric left  half pyramid : -")
user_input = int(input("Enter the number of pyramid : "))
def left_half_pyramid(arg1):
    """Left half pyramid using function focus on space counting """
    sp = arg1*2-2
    for i in  range(1, arg1+1):

        for j in range(1, sp+1):
            print(end= " ")
        sp -= 2

        for k in range(1, i+1):
            print(f"{k}", end=" ")
        print()

left_half_pyramid(user_input) # function call


# Alphabetical numeric Left half pyramid with function
#         A
#       A B
#     A B C
#   A B C D
# A B C D E

print("Enter the value for alpha left  half pyramid : -")
g_value = int(input("Enter the row number : "))
def alpha_half_pyramid(x , y):
    """Alphabetical left half pyramid"""
    space = x*2-2
    for i in range(x):

        for j in range(space):
            print(end=" ")
        space -= 2

        for k in range(i+1):
            alpha = chr(y+k)
            print(f"{alpha}", end=" ")
        print()
alpha_half_pyramid(x = g_value, y=65)




