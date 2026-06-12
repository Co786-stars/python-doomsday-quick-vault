"""
Type of variable and instance method in oops 

Type of variable in oops : -
>> In functional programming we see local variable Global variables .
   Now In OOPs there are two type of variable instance variable and class variables 

1)) Instance variable : -
    
    variable made for particular instance
    saperate compy is create for every object 
    modification of one object never effect to other object 
    value of variable differ from object to object 

2)) Class variable : --

"""
class cloth:
    """class body provide info about many cloth"""
    def __init__(self,n, t, p):
        """function body is use to indicate the type and price"""
        self._cloth_type = t # attribute
        self._cloth_price = p # attribute
        self._cloth_name = n  #attribute

    def marriage_cloth(self):
        self.cloth_type = "mydress"  # self.cloth_type is a instance variable (attribute)
        self.cloth_name = "noname"   # self.cloth_name is instance variable (attribute)

object1 = cloth("t_shirt", "half", 200)
object2 = cloth("shirt", "full", 300)
object3 = cloth("Hat", "Ovel", 250)
print(object1.__dict__)
object1.color = "red"    # use to add the attribute from outside the class (example of instance variable )
print(object1.__dict__) 
print(object3.__dict__)
del object3   # It use to delete object
del object1._cloth_type # use to delete attribute of object1 class  
# print(object3.__dict__) >> the output is showing not define object because object3 is delete from cloth class
print(object1.__dict__)
object1.marriage_cloth()
print(object1.__dict__)

"""
Explanation : for memory-

Step 1.> if interpeter read line 7 then create the namespcace fro class cloth in memory namespace  
step 2.> after read line 2 interperter read line 15 object1 and allocate 
         memory space for object1 and _init__ initilized attribute self n ,t p automatically  
step 3.> in memoryspace object1 is created and it contain three variable(atttribute) t_shirt, cloth_price
         cloth_name whith own specfic value

step 4.> if we delete one object then there is no affect on other object means (modification of one object
        does not impact on other object)

      
 _____________________________
|  _______________________    |
| | cloth_type  = t_shirt |   |
| | cloth_price = half    |   |
| | cloth_name  = 200     |   |
| |_______________________|   | 
|          object1            |
|                             | 
|  ________________________   |
| | cloth_type  = shirt    |  |
| | cloth_price = full     |  |
| | cloth_type  = 300      |  |
| |________________________|  |
|           object2           |
|  ________________________   |
| | cloth_type  =  Hat     |  |
| | cloth_price =  ovel    |  |
| | cloth_type  =  250     |  |
| |________________________|  |
|           object3           |
|_____________________________|

"""