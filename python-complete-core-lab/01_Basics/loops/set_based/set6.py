# """add or remove"""
# var1 = {10, 20, 30, 40}
# var1.add(50) # use to add new items and contain exactly one argument 
# var1.remove(50) # use to remove exist item but if item not exist KeyError occur.
# var1.discard(100) # use to remove exist item but if item not exist no error are occur
# var1.pop() # use to remove last item of set and no argument contain 
# del var1
# # print(var1) 


# """join or exit"""
# x = {"hub", "router", "laptop", "mobile", 1}
# y = {"smartphone", "transreciver", "mobile", True}
# ex = {"Aditya", "raj"}
# z = x.union(y) # use to add all items from both set and contain one or more then one argument  
# print(x|ex)    # there are two way to join two set using union function or vertical pipe symbol
# print(x|ex|y)  
# print(x.union(y, ex)) # use to multipal set

# p = {100, 200, 300}
# q = (300, 400, 500)
# r = [600, 700, 800]
# print(p.union(q)) # use to join all the set item and tuple items as a set
# print(p.union(q, q, r)) # use to join all the set, list and tuple item as a set 


# p = x.update(y) # use to update item of y in x 
# print(x) 
# print(p, y) # None is happen because in p variable no data is exist nothing exist



# """find duplicate item of set"""
# x = {10, 20, 30, 40, 50}
# y = {50, 60, 70, 80, 40, 50}
# z = {100, 200, 300, 40, 50}
# print(x.intersection(y))   # use to provide duplicate item from sets as a set and containone or more then one argument
# print(x.intersection(y, z)) # there are two method to keep only the duplicates set item using intersection function and ampersend symbol 
# print(x&y)
# print(x & y & z)

# "find difference item of set "
# #   difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# x = {10, 20, 30}
# y = {40, 10, 60}
# z = {70, 20, 90}
# print(x.difference(y)) # use to provide item of first set that does not present in other set 
# print(y.difference(z)) # there are two method to keep different item as a set using difference function and subtract symboll 
# print(x.difference(y, z))
# print(x-y)
# print(x-y-z)


# x = {10, 9, 8,7, 5}
# y = {1, 2, 8, 4, 5}
# z = {5, 7, 9, 6, 10}
# print(x-y-z)
# print(x-y)
# print(x.difference(y))
# print(x.difference(y, z))

# """ Symmetric difference set """
# x = {"Aditya", "Hello", "wizard", "smartphone"}
# y = {"Laptop", "Mobile", "smartphone"}
# z = {10, 20, "Aditya"}
# x = {10, 20, 30}
# y = {40, 20, 10}
# z = {20, 10, 40}
# print(x.symmetric_difference(y)) # use to provide element that does not present in both set denoted by (^) and take exactly one argument 
# print(y^z^x)  


# """clear function in set """
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set1.clear() # use to clear the all element of set and no parameter are used 
# print(set1)

# """copy function in set"""
# set2 = {10, 20, 30, 40, 50}
# print(set2.copy())

# """difference_update in set"""
# x = {10, 20, 30}
# y = {40, 30, 50}
# z = {10, 60, 70}

# z = x.difference_update(y) # use to return method that not present in both set 
# print(z, x)

# """Intersection update"""

# x = {10, 20, 30, 40}
# y = {1, 2, 3, 4, 30, 50}
# x.intersection_update(y) # use to removes the items that is not present in both sets
# print(x)


# """symmetric_difference_update set """
# x = {10, 20, 30, 40}
# y = {90, 10, 60, 20}
# z = x.symmetric_difference_update(y) # use to return the item that not present in both set 
# x.symmetric_difference_update(y)
# print(z, x)


# """isdisjoint use for set"""
# x = {1, 2, 3, 4}
# y = {5, 4, 3, 2}
# k = {10, 20, 30}
# z = x.isdisjoint(y) # use to check two set are intersection or not 
# p = x.isdisjoint(k) # if set item are similar to other set then retuen False otherwise True
# print(z)
# print(p) 


# """issubset in set"""
# x  = {1, 2, 3, 4}
# y = {1, 2, 3, 4, 5 }
# z = x.issubset(y)
# print(z)

# """issuperset in set"""
# x = {1, 2, 3, 4, 5}
# y = {4, 3, 2, 1}
# z = y.issubset(x)
# p = y.issuperset(x)
# print(z, p)


x = {10, 20, 30, 40}
y = {}
z = {10, 20, 0, 30}
num = all(number > 0 for number in x)
print(all(x), end=" ") # if all element are true then Return True value
print(all(y), end=" ") # if elements are empty then return true
print(all(z), end = " ") # if element any one element are false then return False value 
print(num)


x = {10, 20, 30, 40}
y = {}
z = {10, 20, 0, 30}
num = all(number > 0 for number in x)
print(any(x), end=" ") # if all element are true then Return True value
print(any(y), end=" ") # if elements are empty then return false
print(any(z), end=" ") # if element any one element are true then return true value 
print(num)



x = {10, 20, 30, 40}
for i, j in enumerate(x, start=1): # use to add counter 
    print(i ,j)


def mynum(val):
    return val//5 == 0

num = [10, 20, 30, 40]
twice = filter(mynum, num)
print(tuple(x), set(x))


x = frozenset([1, 2, 3, 4, 5])
y = {1, 2, 3}
# x.add(y) error are geneteate because we can change set but we cant change forzenset
print(x) 


def function(value):
    return value**2

x = {10, 20, 30}
y = map(function, x)
print(y) # <map object at 0x0000015E4BB86BF0>
print(list(y)) # [100, 400, 900]

x = {10, 20, 30}
print(max(x))
print(min(x))

x = [1, 2, 3, 4]
y = [10, 10, 10, 10]
x = map(lambda i, j: i*j, x, y)
print(set(x))

var = lambda x : x*2
print(var(10))


x = {2, 3,4, 5, 6, 1}
y = sorted(x, reverse=True)
print(y)


x = [("Aditya", 10), ("Wizard", 30), ("Haridwar", 20), ("nampant", 40)]
s = sorted(x, key= lambda x: x[1])
print(s)
