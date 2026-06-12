"""
1) symmetric_difference()
    It is type of function that use to provide different item from both set (given set) set1 and set2

x = {10, 20, 30}
y = {40, 30, 50}
z = {10, 20, 40}
v1 = x.difference(y)
v2 = x.symmetric_difference(y)
v3 = x^y
# v3 = x.symmetric_difference(y,z) # error are generate because we do not use multipal argument
print(v1)   # {10, 20}
print(v2)   # {10, 20, 40, 50}
print(v3)

2) symmetric_difference_function update()
   It is a type of function that use to modify original state of set with different item
   but when we use symmetric_difference() then new set is return . it is denoted with ^=
x = {10, 20, 30}
y = {30, 40, 50}
# x.symmetric_difference(y)  # when we use this function then new set is return
x.symmetric_difference_update(y)  # in case this function we modify original set
print(x)  # {10, 20, 30} >> # {10, 20}

3)) difference_update()
x = {10, 20, 30, 40}
y = {40, 50, 10, 70}
x.difference_update(y)  # use to modify original set and we only use single argument. it is denoted with -=
print(x)  # {20, 30}, {30, 20}

4)) Intersection_update()
x = {10, 20, 30, 50,  40}
y = {10, 20, 50, 60}      # intersection_update() use single argument . it is denoted with &=
x.intersection_update(y)  # use to modify original using similar data in both set (set1 and set2)
print(x)   # {50, 10, 20}, {20, 10}

5)) copy()
x = {"hello", "wizard", "hacker", "@"}
y = x.copy()  # copy function is use to copy() datatypes
print(x)
print(y)

6)) isdisjoint()
x = {10, 20, 30}
y = {30, 40, 50}
p = {10, 20}
q = {30, 40}
z = x.isdisjoint(y)  # isdisjoint() is use to return boolean value True or False if when set is intersection
#                      then False is return otherwise True value is return . it takes single argument
r = p.isdisjoint(q)
print(z)  # False
print(r)  # True

7)) issubset()
x = {10, 20, 30}
y = {40, 10, 50}
p = {10, 20, 30, 40, "wizard"}
q = {50, 60, 10, 20, 30, 70, 40, "wizard"}
z = x.issubset(y)  # subset is use to check all item of original set available in other set or not
r = p.issubset(q)  # it denoted with <=
print(z)  # False
print(r)  # True

8)) issuperset()
x = {10, 20, 30, 40}
y = {10, 20, 30}
z = x.issuperset(y) # it only take one argument and it issuperset() is denoted with >=
print(z)  # True

"""




