# Right half pattern
# *
# * *
# * * *
# * * * *
# * * * * *
print("Pls Enter the value for right half pattern : -")
user_input = int(input("Enter your number of Row : "))

for i in range(1, user_input+1):
    print("* "*i)

# Numeric Right half pyramid
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("Pls Enter the value for numeric right half pyramid : -")
user_num_input = int(input("Enter the number of Row : "))

def num_half_pyramid(value):
    """Numeric right half pyramid"""
    for j in range(1, user_num_input+1):
        for k in range(1, j+1):
            print(f"{k} ", end="")
        print()
num_half_pyramid(user_num_input)



# Alpha Numeric half Pyramid
# A
# A B
# A B C
# A B C D
# A B C D E

print("Enter your value for alpha right half pyramid : -")
user_value_input = int(input("Enter the  Row number : "))

def alpha_half_pyramid(arg1, arg2):
    """Alphabet right half pyramid"""
    for i in range(1, user_value_input+1):
        for j in range(1, i+1):
            char1 = chr(arg2+j)
            print(f"{char1} ", end="")
        print()

alpha_value = 64
alpha_half_pyramid(user_value_input, alpha_value)