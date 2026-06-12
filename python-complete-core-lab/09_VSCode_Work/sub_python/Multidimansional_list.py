"""
1)) how to create multidimensional list or access multidimensional list
var = [[10, 20, 30], [40, 50, 60], ["red", "blue", "green"], [], [70, 80, 90]]
print(var[0])
print(var[1])
print(var[4])
print(var[2])
# print(var[3]) ?
print(var)

print(var[2][1])
print(var[2][2])
print(var[0][1])
x = ["monitor", "tv", "phone"]
var.append(x)
print(var)
var.reverse()
print(var)

# VVI important  ( HOW TO STORE ITEM OR ELEMENT FROM USER IN MULTIDIMENSIONAL LIST )

# var1 = [[10, 20],
#         [30, 40]]
x = int(input("Enter row number : "))#row
y = int(input("Enter col number : "))#col
emp1 = []    # emp1 >> [[20, 40], [50, 60]]
for i in range(x): # i = 0  1
        emp2 = []   # emp2 = [20 , 40] >> [50, 60]
        for j in range(y): # j = 0  1  >> j = 0  1
                z = int(input(f"Enter your value : mat[{i}][{j}] : ")) # z = 20 , 40 , 50 , 60
                emp2.append(z)
        emp1.append(emp2)
for emp2 in emp1:
        print(emp2)   # emp2 >>  [20,  40]
                      #>>        [50,  60]
# print(emp1)


"""
