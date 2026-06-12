x  = {"aditya", "raj", "saurab", "singh"}
for i in x:
    print(i)
    
if "raj" in x:
    print("yes it is in this list")
else:
    print("it is not in list")

if "saurab" not in x:
    print("not in x ")
else:
    print("Yes it is in x ")

print(x)

x.add("rajput")
print(x) 

y = { 1, 2, 3, 4, 5}

# x. extend(y) # never work because extend is not valid for set datatype

x.update(y) # uopdate() is valuiuid for work 
print(x)


l = [1,2,3,4,5,6,7,8]
l = {1,2,3,4,5,6,7,8}

l.remove(5) # remove() function is valid for both list and set 
print(l)

l.pop()
print(l)
l.pop()
print(l)

h  = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(h)

h.discard(50) # use to remove the list 
print(h)

h.clear()
print(h)

del h 
# print(h) # error is find because set is not exist in the variable x 


x  = { 1,2,3,4,5,6,7,8,9}
for i in x:
    print(i)

