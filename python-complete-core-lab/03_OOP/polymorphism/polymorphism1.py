"""
Polymorphism : -

Polymorphism means "many forms" the ability of different objects to respond to the same method or function in different ways.
Polymorphism is fundamental concept in OOPs that allow object to process differently based on their datatype or class .

In python Polymorphism is  enhance code flexbility, reusability , readability and  making it more intuitive and powerful 
basically polymorphism categorized in four parts : - 

1> Functional polymorphism
2> Operator polymorphism
3> Class Polymorphism
4> Polymorphism With inheritance
"""

"""
function polymorphism : -

The ability of a function to operate on different types of data to take multiple forms.
Function Polymorphism means a single function name can represent different functionality based on the context. 

"""

# >> example : - 1st : -

class Cat:
    def make_sound(self):
        return "Meow"
    
class Dog:
    def make_sound(self):
        return "Woof"
class Cow:
    def make_sound(self):
        return "Moo"

def animals_sound(animal): # we call the function from class Cat, Dog .
    print(animal.make_sound()) # positional parameter animals pass the value(argument) from function call

for i in range(3):
    def animal_sound(animal):
        print(animal.make_sound())

cat = Cat()
dog = Dog()
cow = Cow()

animals_sound(cat) # function call
animals_sound(cow) # function call
animals_sound(dog) # function call
# expain : - functioon is same but represent different context or result.


# example second : - 2nd :- 
print(len("Hello"))  #--------------------------------------------| In this example function is same but perform action
print(len([1, 2, 3, 4]))  #-------------------------------------- | on different object (string, number, value) or datatype
print(len({"key1": "value1", "key2": "value2"}), "\n") #----------| we also use more function like add(), len(), max(), min() etc.



# example 3rd : - 
# single function same role on different datatype thats why this is functional Polymorphism . 
def add(a, b):
    return a + b

# Works with integers
print(add(5, 3))  # Outputs: 8

# Works with strings
print(add("Hello", "world"))  # Outputs: Hello world
