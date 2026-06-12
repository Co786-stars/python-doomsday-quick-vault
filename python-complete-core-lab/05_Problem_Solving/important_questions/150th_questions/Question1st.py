
# WAPP to print "Hello Python" ? 

# ____________________________________________________________________________________________#

print("Hello Python") # task oriented programming
# Explanation : - 
# In the given statment print is display the copy text "Hello Python" . 
# because print is pridefine function that use to display copy value in output screen
# output : -
# Hello Python


# ____________________________________________________________________________________________#

def fun(value):
    print(value)
fun("Hello Python")
# In the given program we create the function "fun()" using def keyword .
# "fun()" contain value parameter that pass argument "Hello Python" when it was call
# Now print is use to dispay the argument that pass from value parameter "Hello Python" 

# ____________________________________________________________________________________________#

class DisplayText:  # Object oriented programming 
    """Class body is use to print the copy text"""
    def __init__(self):
        """constructor is initilize attribute"""
        self.var1 = str(input("Enter text : "))
    
    def displaytext(self):
        """display text at output screen"""
        print(self.var1)

txt = DisplayText()
txt.displaytext()
"""
Explain : -

In  the given program we create the class "DisplayText" that contain two function
first is "__init__() " constructor(special function , auto callable, magical function) 
and second is "displaytext()"

After that we create object "txt" from "DisplayText" then the memory  refrence
(location, address) of "DisplayText" assign in object(variable) "txt".

Then after we use prantheses in class "DisplayText()" to pass the memory location
of "txt" as a argument from self parameter and auto initilize special function .

After initilization the attribute (variable) "var1" is created in given memory location 
that passed from self thats why we use "memory_location.variable_name"  "self.var1"

Now var1 store user_value using "input()" then we call the second function 
"txt.displaytext()" and pass memory same location from self parameter where 
user_value was store.

Hence we acess the value from memory and display the user_value using "print()"
because print is use to display print or copy value on output scren.

output : -
Enter the text : "Hello Python"
Hello Python
"""
# ____________________________________________________________________________________________#
