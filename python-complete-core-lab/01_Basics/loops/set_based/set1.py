x = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for y in x:
    print(y)

y = {"India", "Arab", "Europe"}
y.add("Nicobar")
# y.append("Delhi") append is not support in set type data type
print( y)

set1 = {10, 11, 12, 13, 14, 15}
set2 = {16, 17, 18, 19, 20}
set1.update(set2)
print(set1)

set1.clear()
print(set1)

for x in set2:
    set1.add(x)
print(set1)
print({})   # empty set
print(set()) # empty set



#list part previous
x = [1,2,3]
y =[4, 5, 6]
# x.append(y)
# x = x+y
#x.extend(y)
"""for i in y:
    x.append(i)
print(x)
"""
