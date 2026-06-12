# store a all item of x in x new
x = ["value1", "value2", "value3", "value3", "value4", "value5"]
xnew = []

for i in range(len(x)):
    xnew.append(i)
print(xnew)
xnew.clear()


for i in x:
    xnew.append(i)
print(xnew)
xnew.clear()


i=0
while i < len(x):
    xnew.append(x[i])  # store item of x in xnew
    i+=1
print(xnew)
xnew.clear()

# store a value and change in upper case using while loop

j = 0
while j < len(x):
     xnew.append(x[j].upper())
     j+=1
print(xnew)


# with condition inside the the loop

