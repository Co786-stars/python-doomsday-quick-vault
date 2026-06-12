"""
# How to access tuple item using for loop
x = (10, 20, 30, 40, 50)
print(x[4])

for i in range(len(x)): # length = 5 >> 0 1 2 3 4
    print(x[i])

for j in x: # j >> 10, 20, 30, 40, 50
    print(j)

# How to access tuple item using while loop

x = ("Laptop", "Smartphone", "Monitor", "Router", "Hub")

i = 0
while i < len(x): # 0 < 5 >> 0 1 2 3 4
    print(x[i]) # x[0], x[1], x[2], x[3], x[4]
    i += 1  # 0+1>> 1+1>> 2+1> 3+1> 4+1> 5>>> false


x = ((10, 20, 30, 40),
     (50, 60, 70, 80),
     (40, 30, 20, 10),
     (80, 70, 60,50))
# print(x)
for i in x: # row
    for j in i:
        print(j, end =" ")

x = (("Hacker", 151), ("Wizard", 101), ("Xyz", 000))
y  = tuple(x for x, name in x)
print(y)
z = tuple(x for x, x in x)
print(z)

x  = (1, 2, 3, 4, 5)
y  = (6, 7, 8, 9, 10)
print(x+y)

"""
