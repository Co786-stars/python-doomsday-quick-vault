"""
1) Unpacked tuple

# packed tuple means creating a tuple and assigning it to variable .
color = ("red", "green", "blue") # multiple item are packed in single tuple # packed tuple
var1, var2, var3 = color # tuple are unpacked because individual variable contain
                         # individual item of tuple
print(var1, var2, var3)

device = ("Laptop", "Monitor", "Smartphone")
(var1, *var2 )= device
print(var1)  # Laptop
print(var2) # ['Monitor', 'Smartphone']

number = (10, 20, 30, 40, 50, 60, 70)
x, y, *z = number
x, y, *z = number
*x, y, z = number
print(x, y, z)
"""

