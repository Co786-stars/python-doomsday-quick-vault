"""
#1)) How to use union()
# Type of functions use with set datatype
x = {10, 20, 30}
y = {40, 50, 60}
z = {"Hello", "wizard"}
var1 = (70, 80, 90)
var2 = [90, 100, 101]
p = x.union(y)  # union function is use to return new datatype in from of set
q = x|z  # use to set items
r = x.union(y, z)
s = x|y|z # union() function is denoted with vertical pipe in python
# t = x|var1|var2  # with shor method we never use multipal argument
t = x.union(var1, var2) # but with the help of union function we multipal argument
print(p)  # {10, 20, 30, 40, 50, 60}
print(q)  # {'Hello', 'wizard', 10, 20, 30}
print(r)  # {'Hello', 'wizard', 10, 20, 30, 40, 50, 60}
print(s)  # {50, 'wizard', 20, 40, 'Hello', 10, 60, 30}
print(t)  # {70, 80, 90, 100, 101, 10, 20, 30}


2)) How to use update()
x = {"router", "Hub"}
y = {"switch", "bridge"}
z = [10, 20, 30]
p = (50, 60, 70, 10, 10, 10, 10)
# x.update(y)
# x.update(z)  # {'router', 10, 20, 'switch', 'bridge', 'Hub', 30}
# x.update(p)  # {'router', 10, 20, 'switch', 'bridge', 'Hub', 30, 50, 60, 70}
x.update(y, z, p)  # we also pass multipal argument from update function
print(x)  # update() function is use to update items of set in other set datatype
# output : {70, 10, 60, 'router', 'bridge', 50, 20, 'switch', 'Hub', 30}

3)) how to use intersection()
x = {10, 20, 30, 40}
y = {50, 60, 10, 20, 40}
p = {50, 60, 10, 40}
z = x.intersection(y)  # intersection() function is use to return similar data in the from of set  # {40, 10, 20}
o = x.intersection(y, p)
q = x&y   # intersection is denoted with ampersand (&) symbol in python   >> {40, 10, 20}
r = x&y&p  # {40, 10}
print(z)   # {10, 20, 40}
print(o)   # {10, 20, 40} change when value is p at place of z >> {10, 40}, {40, 10}
print(p)
print(r)

4)) how to use difference()
x = {10, 20, 30, 40}
y = {30, 20, 50, 70}
var1 = {100, 101, 10, 40}
z = x.difference(y)  # difference function is use to return different value from set
p = x-y  # difference() is denoted with subtract symbol
r = x-y-z # first of all x-y >>  {40, 10}-z >> {40, 10}-{100, 101, 10, 40}
print(z)  # {10, 40}, {40, 10}
print(p)  # {40, 10}
print(r)  # set(), {}

"""


