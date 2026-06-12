"""
#----- Built_in Class function --------Built_in Class function -------Built_in Class function -----Built_in Class function --------#

syntax : -

getattr(object_name, attribute)
delattr(object_name, attribute)
hasattr(object_name, attribute)
setattr(object_name, 'attribute', 'new_name')

"""

class Product:

    def __init__(self, name, price):
        
        self.p_name = name    #attribute
        self.p_price = price  #attribute
    
    def display(self):
       
       return  f"The product name is {self.p_name} and price is {self.p_price}"


x = str(input("Enter your product name  : "))
y = int(input("Enter your product price : "))
p1st = Product(name=x, price=y) # creating object (p1st)

print(getattr(p1st, 'p_name'))  # type of built-In-class function use to Retrieves the value of attribute 
print(p1st.__dict__) 
delattr(p1st, 'p_price')   # use to delete an attribute 
print(p1st.__dict__)
print(hasattr(p1st, 'p_price'))  # use to check attribute is exist in object or not if not exist it return False 
print(hasattr(p1st, 'p_name'))   # use to check the attribute exits in object or not if exist it return True
setattr(p1st, 'p_name', 'mobile')   # use to change the value of an attribute 
print(p1st.__dict__)

# print("\n")
# print(p1st.__dict__)   # use to access the attributes value
# var = p1st.p_name      #  use to access the value of attribute (variable)
# print(var)
# var1 = p1st.display()  # use to access the function/method
# print(var1)


""""
explanation : -

-> getattr(object_name, 'attribute_name')  >> How interperter read it the line 

step 1.> Calls the getattr() function.
step 2.> Checks if the attribute p_name exists in the p1st object.
step 3.> If p_name exists, it returns the value of p_name

or 

when the interpreter reaches the getattr(p1st, 'p_name') line, it:
Goes to the memory location where the p1st object is stored.
Checks if the attribute p_name exists in the p1st object.
If p_name exists, it retrieves and returns its value.



-> delattr(object_name, attribute) 

step 1.> Calls the delattr() function.
step 2.> Checks if the attribute p_price exists in the p1st object.
step 3.> If p_price exists, it delete the attribute


-> hasattr(object_name, 'attribute')  >> it return bool value 

step 1.> Calls the hasttar() function.
step 2.> Checks if the attribute p_price exists in the p1st object then return True otherwise False .
step 3.> p_price is no exists so it return False.


setattr(object_name, 'attribute_name', 'new_value') >> srtattr() always take three argument 

step 1.> Calls the setattr() function.
step 2.> Checks if the attribute p_price exists in the p1st object then change the attribute value .
step 3.> current value of p_name attribute is change .


"""

# ----------extra topic (built in class function) =----------------
# print(isinstance(p1st, MyClass))
# print(issubclass(MyClass, ParentClass))
# print(dir(p1st))
# print(vars(p1st))
# print(callable(p1st.some_method))
# print(type(p1st))


