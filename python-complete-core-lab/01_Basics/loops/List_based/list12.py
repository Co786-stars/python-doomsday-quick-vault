# wap to take the input from user and print matrix as using loop .

row = 2  
col = 2
emp1 = []  # __? 

for i in range(row):   # i = 0  
    emp2 = []          # emp2 = [100, 200]
    for j in range(col): # J  = 0  1 
        x = input("Enter your number : ")
        emp2.append(x)
    emp1.append(emp2)
print(emp1)

