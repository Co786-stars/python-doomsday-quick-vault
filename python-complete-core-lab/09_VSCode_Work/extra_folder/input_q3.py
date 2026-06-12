"""a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]

m = 4
n = 5
a = [[0 for x in range(n)] for x in range(m)]

a.append([5, 10, 15, 20, 25])

a[0].extend([12, 14, 16, 18])

a[2].reverse()


# Get the dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty 2D list"""

rows  = 2
cols = 2
matrix = []


for i in range(rows):
    row = [] 
    for j in range(cols):
        value = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(value) 
    matrix.append(row)  
print(matrix)

for row in matrix:
    print(row) 


"""


# Get the dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create a 2D list using list comprehensions
matrix = [[int(input(f"Enter element at position ({i}, {j}): ")) for j in range(cols)] for i in range(rows)]

# Display the multi-dimensional list
print("Multi-dimensional list:")
for row in matrix:
    print(row)
"""





    # Get the dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create a 2D list using list comprehensions
matrix = [[int(input(f"Enter element at position ({i}, {j}): ")) for j in range(cols)] for i in range(rows)]

# Display the multi-dimensional list
print("Multi-dimensional list:")
for row in matrix:
    print(row)

