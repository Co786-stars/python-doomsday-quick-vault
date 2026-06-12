# Modification : if any datatype changes it original state then we say modification is occur
# How to modify Data in set datatype

"""
x = {10, 20, 30}
x.add(40)  # add() function is use to add new item in set datatype
# x.add()  # if no argument is pass then error are occur
# x.add(10)  # attribute error occur if argument is pass when set is empty
print(x)  # {20, 10, 30, 40}

y = {"red", "blue", "Green"}
y.remove("Green")  # use to remove existing element of set datatype
y.remove("sky")  # Key error are occur because element are not exist
# del y
print(y)  # {'blue', 'red'}

z = {"Laptop", 20, 2+1j, 20.6}
z.add("Smartphone")
z.discard("Smartphone")  # use to discard existing element from  set datatype
z.discard(50)  # if the element is not exist in set datatype we try to access it then No error are occur
z.remove(50)  # if the element is not exist in set datatype we try to access it then key error are generate
print(z)  # {'laptop', 20, 2+1j, 20.6}

x = {20, 10}
y = {10, 20, 30}
z = {10, 20, 30, 40, 50, 60}
x.pop()  # pop() function is use to remove last item of list but not in set
y.pop()  # In set datatype it remove item or element from any place
z.pop()
print(x)  # {20}  {10}
print(y)  # {10, 20}, {10, 30}, {20, 30}, {30, 20}..etc
print(z)  # ....................etc

x = {10, 20, 30}  # set    >> first element remove {20, 30}
y = (10, 20, 30)  # tuple  >> error occur Attribute error
z = [10, 20, 30]  # list   >> last item remove [10, 20]
x.pop()
# y.pop()
z.pop()  # [10, 20]
z.pop(1)  # [10]
# x.pop(2) # {10, 20} # error because set does not depend upon index number
print(x, y, z)

x = {10, 20, 30, 40, 50}
y = {1, 1, 1, 1, 1, 1, 1}
x.add(50)  # no changes in output because set does not allow duplicate item .
print(x)
print(y)  # {1} because duplicate items are not allow in set datatype

p = {1, True}  # {1, 1} >> True value read as a 1 so that's why it is also duplicate
q = {0, False} # {0, 0} >> False value read as a 0 so that's why it is also duplicat
r = {True, 1, False, 0}  # >> {1, 1, 0, 0}
print(p)  # {1}
print(q)  # {0}
print(r)  # {True, False}

"""