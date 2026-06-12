"""
Use to import multiple class in __main__ module : -

syntax : - import module only 
import class_name
import class_name

Syntax : - import class only

from module_name import classname
from module_name import classname1, classname2...etc

"""

# import class1_import: It use to import module basic 
# from class1_import import Device 
# from class1_import import Tec
from class1_import import Device, Tec, Toys

obj = Device()
x = obj.motorspeed()
print(x)

obj2 = Tec()
x = obj2.odometer_speed()
print(x)

obj3 = Toys()
x = obj3.toy_speed()
print(x)