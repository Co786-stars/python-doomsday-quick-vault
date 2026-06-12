# Importing an entire module 

"""
import class2_import
y  = class1_import.Toys("Car", 2000)
y.x(y.toy_name, y.toy_price)

obj = class2_import.Toys(str(input("Enter Toy name : - ")), int(input("Enter Toy Price : - ")))
print(obj.x(obj.toy_name, obj.toy_price))
"""

# Importing using alias
from class2_import  import Tec as T
y = T()
y.odometer_speed()

#  importing module 

"""import class2_import as module21"""




