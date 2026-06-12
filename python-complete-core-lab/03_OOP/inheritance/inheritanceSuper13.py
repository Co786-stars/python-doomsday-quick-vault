# -----------------------------------------------------------------------------------------------------------------

class Device:

    def __init__(self, name, type):
        
        self.dname = name
        self.dtype = type
    
    def tec():

        return "This is technical device"
    
class Type(Device):
     def __init__(self):
         super().__init__("Laptop", "Rizon")  # when __init__ is excute then name and type is also initilize so we give two value 
# at this point attributes dname and dtype is created from parents . Now we want to pass the value of parameter name and type 
# is "laptop" nad Rizon

obj = Type()
print(obj.dname)
print(obj.dtype)


# -------------------------------------------------------------------------------------------------------------------

# ------------------------------# SUPER NEED TO MORE PRACTIC #-------------------------------# ---------------------