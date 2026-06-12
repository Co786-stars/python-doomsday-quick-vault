# print the right half star pyramid pattern 
def right_half_pyramid(num):
    """code to print the right half pyramid"""
    for i in range(1, num+1):
        print("* "*i)

value = 5
right_half_pyramid(value)
# output >> i = 1  2  3  4  5
# output >> *
# output >> * *
# output >> * * *
# output >> * * * *
# output >> * * * * * 


# Def function is use to print the right half numaric  pyramid 
def right_half_alpha(num1):
    " right half pattern alpha pyramid"
    for i in range(1, num1+1):
        for j in range(1, 2*i):
            print(j, end="")
        print()
num1 = 5
right_half_alpha(num1)

