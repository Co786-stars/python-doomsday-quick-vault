tup = ("aditya", "Rohan", "Sohan", "Mohan", "Zilla")
tup = list(tup)
tup[4] = "hello"
tup = tuple(tup)
print(tup)

ap = list(tup)
ap.append("rajesh")
tup = tuple(ap)
print(tup)

x = (1, 2, 3, 4, 5)
y = (10 ,20)
z = [30, 40 , 50 ]
k = [1,2,3,4,5,6,7,8,9]
print(x+y)
print(k+z)

for x in z:
    print(x)

print(x)

del x
# print(x) delete the value of x






