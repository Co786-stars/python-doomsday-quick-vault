class Device:
    """class is use to provide the information about Device"""

    def motorcar(self):
        """___________"""
        motor = ["honda", "tvs", "hero", "apache"]
        i = 0
        while i < len(motor):
            current_motor = motor[i]
           
            if current_motor in motor:
                x = f"{current_motor} company moterbike are abliable"
           
            else:
                return f"{current_motor} company are not avaliable"
            i += 1


    def  motorspeed(self):
        """__________"""
        odometer_speed = int(input("Enter odometer speed of moter : "))
    
        if odometer_speed < 251:
            return f"The speed {odometer_speed} of odometer is prefect for motor car"
        
        else:
            return f"It is to high, {odometer_speed} odometer for any prefect motorcar "
    

    def __init__(self, name = "Two wheller", company="Honda"):
        """__________"""
    

class Tec(Device):
    """class body contain techinical methods"""

    # def __init__(self):
    #     super().__init__() 
    #     self.battry = "Good"

    def odometer_speed(self): # similar method name are difine in parents class so child class overide the same method of parents class  
        """this method is is display override process in oops"""
        return "The odometer are not found in technical device it is in machinacl device"

class Toys:

    def __init__(self, name, price):
        
        self.toy_name = name 
        self.toy_price = price 
        
    def x(self, name, price): 
        return f"Toy name is {self.toy_name} and price of Toy is {self.toy_price}" 


# obj = Tec() 
# x = obj.odometer_speed() 
# print(x) 


# obj = Device() 
# x = obj.motorspeed() 
# print(x) 

# obj = Toys(str(input("Enter Toy name : -")), int(input("Enter Toy Price : -")))
# print(obj.x(obj.toy_name, obj.toy_price))

# ---------------------->>>>>>>>>>>>>>> GO TO NEXT MODULE FOR WATCHING HOW IMPORT WORK ? <<<<<<<<<<<------------------#

