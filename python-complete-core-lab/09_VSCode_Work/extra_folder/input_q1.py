"""# 1)) wap to check the given number is even or odd .

num = int(input("Enter your number : "))
if num%2 == 0:
    print(f"Your given number {num} is even")
elif num%2 != 0:
    print(f"Your given number {num} is odd")
else:
    print("Pls enter valid number ")

# 2))  write a program that asks the user how many people are in thier dinner group if more 
#      then eight print a message saying they'll have a wait for a table . otherwise , report
#      that their table is ready 

p_group = int(input("how many people are in their dinner group : "))
if p_group > 8:
    print("They will wait for a table ")
else:
    print("The table is ready for dinner")

# 3)) write a program that asks the user what kind of rental car they would like 
#     print a message about that car such as "Let me see if I can find you a subaru"

rental_car = input("what kind of rental car woould you like : ")
print(f"Let me see {rental_car} it is the best car in all of above car")

# 4)) Ask the user for a number and then report weather the number is a multipal of 10 or not.
num = int(input("Enter the number : "))
if num%10 == 0:
    print(f"The number {num} is devisible by 10")
elif num%10 != 0:
    print(f"The number {num} is not devisble by 10")
else:
    print("Enter valid number pls ")


# 5)) write a program to find the unit degit of the number

number = int(input("Enter your vlauable number : "))
unit_degit = number%10
print(f"Unit degit of the number is {number} is {unit_degit}")
"""



