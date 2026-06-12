"""
Local Variables:
Local variables are declared within a function.
They have a limited scope and are destroyed when control exits the function.

Global Variables:
Global variables are declared outsides of any function.
They exist throughout the entire execution of the program.

# Write a program to store number in array or display the number that is divisible by 5.
def number(user_value=5):
    x, lst = 1,[]  # local variable
    while x:
        user_input = input(f"Enter the number : {x} : ")
        try:
            if int(user_input)%user_value == 0:
               lst.append(int(user_input))
        except ValueError:
            if user_input == "quit":
                break
        x += 1
    return f"selected number is divisible by 5 : {lst} "
divisible_num = number()
print(divisible_num)

"""

#arbitrary argument :
# > Positional arbitrary arguments (*args)
def make_pizza(*client_pizza): # store whole item as a tuple form
    print("Your pizza order given with the following : -")
    print(client_pizza)
    for pizza in client_pizza:
        print(f" {pizza}")
make_pizza("onionPizza", "little pizza", "large", "extra cheese")

def student_details(name, *student):
    print(f"my name is {name} \n details :  {student}")
student_details("Mohan", "Patna", "Bihar", 844126)

# keyword Positional arbitrary argument (*kwarg)



