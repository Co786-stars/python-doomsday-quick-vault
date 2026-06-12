# Method Resolution Order______________ Method Resolution Order______________________Method Resolution Order__________________________ 
# Method Resolution Order__________ Method Resolution Order_____________________Method Resolution Order______________________________
# Method Resolution Order__________ Method Resolution Order______________Method Resolution Order_____________________________________

"""
Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially 
with multiple inheritance, knowing how Python decides which method to execute is vita

It uses the C3 linearization algorithm to determine the method resolution order of a class.

The C3 linearization is a way to obtain an order of classes for the purpose of method resolution which 
is deterministic, monotonic, and preserves local precedence order

"""

class Color:

    def red(self):
        return 'red is my favroite color'
    
    def green(self):
        return "green is my favorite color"

class Flower:

    def red(self):
        return "my favorite flower is red rose"

    def green(self):
        return "my favorite flower is while tulip"


class Flower_clors(Color, Flower): # method resolution order
    pass

obj = Flower_clors()
x = obj.red()
y = obj.green()
print([x], [y])


# another method 
class Device:

    def technical(self):
        print("Technical devices")
    
    def central():
        pass
    
class Network():

    def central(self):
        print("wan network")

class Connector(Device, Network):  # class orderring 

    def rj45(self):
        print("connector rj45")
    
    def central(self):
        pass

obj2 = Connector()
print(Connector.__mro__)   # Classname.attributename (__micro__) . (use to display how many class passes throug child class {Connector})
print(Connector.mro())
