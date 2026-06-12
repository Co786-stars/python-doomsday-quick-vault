# There are the many way to pass the argument in function definition 
# 1)) Positional argument
# 2)) Keyword argument
# 4)) Default argument
# 5)) Arbitary argument
 
""" 
____Positional argument_________

Positional arguments are fundamental in passing values to function parameters these arguments are assigned 
to parameters based on their order within the function.

When positional arguments are provided in an unordered form, there is a risk of obtaining incorrect output. 
Therefore, it is essential to specify the correct order.
"""

#1)) exaple of positional argument 

def favorite_fruits(arg1, arg2):
        """function body to check the positional argumnent """
        print(f"your favorite fruit is : {arg1} ") 
        print(f"your favorite books is : {arg2} ") 

arg1 =  "Apple"
arg2 = "depth"
favorite_fruits(arg1 , arg2)   



#2)) example of  positional argument  

def new_value(num1, num2):            # these are the two parameter that pass the value 9 and 10 .
        """try to add the both value"""
        sum = num1+num2
        return sum

new_value(9, 10)  # positional argument are basic argument that passed orderly in parameter 


# 3)) example of positional argument book

def describe_pet(animal_type , pet_name): # function definition
       """about pet animal""" # docstring that define about function body
       print(f"I have a {animal_type}")
       print(f"My {animal_type.lower()}'s name is {pet_name.title()}")

# positional argument given in order so we get correct output in this case 
describe_pet("dog", "tomy") # call function 1st

# positional argument given in unorder so we get Incorrect output in this case 
describe_pet("chiku", "cow") # call function 2nd



