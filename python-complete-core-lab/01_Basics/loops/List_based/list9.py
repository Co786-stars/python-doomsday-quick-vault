# List Compheransion

var1 = [["Aditya", 22], ["Wizard", 30], ["Abhishek", 25], ["Ankit", 14]]  
var2 = set((name, age) for name, age in var1)  # use to access multi dimansional list comprehension
var3 = set(age for age, var3 in var1)   # use to access the first item of list using list comphrension
var4 = set(var4 for var1, var4 in var1) # use to access second item of the list 
print(var1) 
print(var2)
print(var3)
print(var4)

# explanation : --
"""
var2 = set((name, age) for name, age in var1) :----------

This list comprehension iterates over each sublist in var1.
For each sublist, it extracts the first element (the name) and the second element (the age).
The resulting tuples (name, age) are collected into a set (var2).
So, var2 contains pairs of names and ages: {('Ankit', 14), ('Aditya', 22), ('Wizard', 30), ('Abhishek', 25)}.

var3 = set(age for age, var3 in var1)  :---------------

This list comprehension iterates over each sublist in var1.
For each sublist, it extracts the second element (the age).
The resulting ages are collected into a set (var3).
So, var3 contains the ages only: {25, 14, 22, 30}.

var4 = set(var4 for var1, var4 in var1) : --------------

This list comprehension iterates over each sublist in var1.
For each sublist, it extracts the second element (the age) again.
The resulting ages are collected into a set (var4).
So, var4 also contains the ages only: {25, 14, 22, 30} (same as var3).

"""

