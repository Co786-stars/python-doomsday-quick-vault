ul = [1,2,3,4,5,6,7,8,9,10]
nul = []
for x in ul :
    if len(ul) == 10:
        nul.append(x)
    else:
        ul.clear()
print(nul)

x= ["red", "green", "blue", "brown", "black", "yellow", "white", "purple", "grey"]
y = []
for i in range(len(x)):
    if "r" in x[i]:
        y.append(x[i])
print(y)
y.clear()


i = 0
while i < len(x):
    if "r" in x[i]:
        y.append(x[i].upper())
    i += 1
print(y)
y.clear()

# change the value of x in upper case . and value of y in title case
# condition by shorthand loop .

i = 0
while i < len(x):
    x[i] = x[i].upper()
    if i < len(x):
        y.append(x[i].upper())
    i += 1
print(x)
print(y)


x = [x.lower() for x in x]
print(x)


x = [x for x in x if "w" in x]
print(x)

x = [x for x in range(10) if x < 5]
print(x)

# RE........................PEAT............RE.......PET

new_li = ["wizard" for i in range(10)]
print(new_li)

new_li = [i if i == "b" else "Gabber" for i in new_li]
print(new_li)

# concept......................concept............concept
print("\n")
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
newlist = [x for x in list]
print(newlist)
# print(len(list[10])) doubt

z = [j if j < 5 else "....." for j in range(11)]
print(z)

x = ["Aditya", "Raushan", "Shavani", "Kokila", "Raja", "Rani"]

print(sorted(x))
print(x)
x.sort()
print(x)
x.reverse()
print(x)

y  = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
y.reverse()
print(y)
y.sort(reverse = True)
print(y)

# Function.........Function.........Function............Function.........Function

color = ["Red", "Green", "Yellow", "Blue", "Orange"]
new = color.copy()
print(new)

# list = list((1,2,3,4,5,6))   >>>>>>>  concatination of list
# x = list(x)                  >>>>>>>  copy methoad of list


# joining of list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ["Aditya", "Raj", "saurab", "singh", "Rajput"]
x = list1 + list2
# print(list1+list2)
print(x)

for k in list2:
    list1.append(k)
print(list1)

h =[0, 0, 0, 0, 0]
i =[1, 1, 1, 1, 1]
h.extend(i)
print(h)
