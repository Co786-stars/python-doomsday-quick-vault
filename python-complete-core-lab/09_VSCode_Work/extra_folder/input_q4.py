# var = [1]
# print(var)

# num[0][2] = 20 
# print(num) 

# num[0][0] = num[2][2]
# x = num.pop(1)
# print(num)
# print(x)
# num[1].extend(x)
# print(num)

# num.reverse()
# print(num)

num = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 40, 30]]
sat = []
for i in range(len(num)):
    print("\n")
    for j in range(len(num[i])):
        var = num[i][j]
        sat.append(var)
print(sat)

for i in num:
    for j in i:
        print(j)


z  = [["red", "green", "blue"], ["yellow", "sky", "brown"], ["grey", "light", "white"]]
for x in z:
    for y in x:
        print(y)

# problem (( 1 ))

"""
row = int(input("Enter your Row number : "))
col = int(input("Enter your col number : "))
mat = []
for x in range(row):
    emp = []
    for y in range(col):
        value = int(input(f"Enter your value ({x}, {y}):"))
        value.append(emp)
        mat.append(emp)

    
for emp in mat:
    print(row)"""


