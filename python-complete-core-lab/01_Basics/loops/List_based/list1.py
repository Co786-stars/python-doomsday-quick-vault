x = ["aditya", "Raj", "Saurab", "Singh", "Rajput" ]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [True ,False]
x.append("Rajput")

print(list[4])
print(list[1:3])
print(list[-3])
print(list[:3])
print(list[4:])
print(list)
list.reverse()
print(list)
print(list)

print(x)
print(len(x))
print(len(x[2]))
print(len(x[4]))
print(len(x[1]))
print(y)
print(y[0])
print(y[1])
print(type(y))
print(type(x))
print(type(list))
print(type([1,2,3,4,5,6,7,8,9]))

# Negetive indexing
l1 = ["Aditya", "Raj", "Saurab", "ji", "How", "are", "you"]
print(l1[-5:-2])
print(l1[-3])
print(l1[-3:])
print(l1[-4:])
print(l1[4:])
print(l1[-5:])
print(l1[-5:-3])
print(l1[2:4])


if "Aditya" in l1 :
    print("Yes")
else:
    print("No")


l1.append(2+2j)
if 2+2j in l1:
    print("Yes", 2+2j, "in l1 list")
else:
    print("No")


x_l = [1,2,3,4,5]

print(x_l)
x_l[0] = 10
x_l[1] = 20
x_l[2] = 30
x_l[3] = 40
x_l[4] = 50
print(x_l)

# Re-change again list item [10, 20, 30, 40, 50]

x_l[2:4] = ["Black", "Rock"]
x_l[0:2] = ["Jio", "Reliance"]
x_l[4] = "company"
print(x_l)

x_l[1:3] = ["hello"]
print(x_l)

x_l.insert(1, "Relance")
print(x_l)

x_l.insert(0,"Google")
print(x_l)

x_l.append("Microsoft")
print(x_l)

x_l.remove("Microsoft")
print(x_l)

x_l.remove(x_l[1])
print(x_l)

x_l.remove(x_l[-3])
print(x_l)

x_l.pop()
print(x_l)

x_l.pop()
print(x_l)

x_l.pop(0)
print(x_l)

x_l.pop()
print(x_l)

x_l.append("Aditya")
x_l.append(100)
x_l.insert(2,2+2j)
# x_l[2] = "Rajwashari"
x_l.insert(4,"Rajeshwari")
print(x_l)

del x_l[0]
print(x_l)

del x_l[1]
print(x_l)

del x_l
# print(x_l) x_l list was delete that is not found

l = [10, 20 , 30, 40, 50, 60, 70, 80, 90]
l.remove(10)
l.remove(l[3])
print(l)
l.clear()
print(l)

z = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in z :
    print(x)
print(x) # last value of x is 9

print("\n")
for i in range(len(z)):
    print(z[i])

# for j in range(10):
#     for k in range(5):
#         print(j, end=" ")
#         print(k, end=" ")
#

x = [x for x in  z if z != 3]
print(x)

L_2 = ["Green", "Bue", "Black", "Red", "Brown", "yellow"]
i = 0
while i < 6:
    print(L_2[i])
    i +=1


# newlist = []
# i=0
# while i < len(L_2):
#     newlist[i] = L_2[i]
#     i +=1
# print(newlist)

L_2 = [x.upper() for x in L_2]
print(L_2)

for i in range(len(L_2)) :
    L_2[i] = L_2[i].lower()
print(L_2)

L_2 = [x.title() for x in L_2]
print(L_2)

for j in range(len(L_2)):
    L_2[j] = L_2[j].swapcase()
print(L_2)
