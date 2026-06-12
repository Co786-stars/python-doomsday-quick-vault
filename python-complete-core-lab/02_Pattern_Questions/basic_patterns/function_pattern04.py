
x = int(input("Enter your number : "))
def pattern_full_pyramid(value):
    value2 = value+4
    for i in range(1, value+1):

        for j in range(1, value2+1):
            print(" ", end="")

        for k in range(1, i*2):
            print("*", end=" ")
        print()
        value2 -= 2
g_value = x
pattern_full_pyramid(g_value)




def full_pyramid_pattern(user):
    """full pyramid pattern using function"""
    condition = user*2-1
    for row in range(1, user+1):
        
        for space in range(1, condition+1):
            print("-", end="")
        
        for col in range(1, 2*row):
            print(f'{col}', end=" ")
        
        print()
        condition -= 2
        
full_pyramid_pattern(user=5)

""" full_pyramid_pattern without using function very simple"""

x = 9
for i in range(1, 6):
    for j in range(1, x+1):
        print(" ", end="")
    
    for k in range(1, 2*i):
        print(f'{chr(64+k)}', end=" ")
    print()
    x -= 2


