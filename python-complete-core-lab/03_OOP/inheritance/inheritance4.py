# Wap to perform the addition of matrix  by user using class . >>>>>> Important concept in 15 ,16 files // Bilkul simple hai bus self 
# ka use keya hua hai wo v iskeleye kuyki 

class Mymatrix:


    def __init__(self, row, col):   # passing value 2 and 2 
        self.matrix_row = row 
        self.matrix_col = col



    def matrix1st(self, value1, value2):  # value passing from matrix1st() there is but  difference before calling first give obj 
        print("My first matrix elements : - ") 
        i = 0
        mat1 = []
        while i < value1:
            row = []
            j = 0 
            while j < value2:
                user = int(input(f"Enter value mat1[{i}][{j}]: "))
                row.append(user) 
                j += 1
            mat1.append(row)
            i += 1
        return mat1
    
    
    # function use to display the second matrix 
    def matrix2nd(self, uservalue1, uservalue2): # argument passing parameter
        print("My second matrix element : -")
        mat2 = [] 
        for i in range(1, uservalue1+1):
            row = []
            for j in range(1, uservalue2+1):
                row.append(int(input(f"Enter value : mat2[{i}][{j}] : ")))
            mat2.append(row)
        return mat2
    

    def sum_of_matrix(self, mat1, mat2):
        print("The addition of mat1 and mat2 is : -")        
        i = 0
        sum = []
        while i < len(mat1):
            row = []
            j = 0
            while j < len(mat2):
                row.append(int(f"{mat1[i][j] + mat2[i][j]}"))
                j += 1
            sum.append(row)
            i += 1
        return sum 

        
matrix = Mymatrix(2, 2) # if we dont pass any argument then error are generate 
mat1st = matrix.matrix1st(2, 2)  # pass positional argument (memory refrence, 2, 2)
mat2nd = matrix.matrix2nd(2, 2)  # pass positional argument (memory address,  2, 2)
sum = matrix.sum_of_matrix(mat1st, mat2nd)

print("first matrix  : -")
for _ in mat1st:
    print(_)

print("second matrix : -")
for _ in mat2nd:
    print(_) 

print("sum of matrix : -")
for _ in sum:
    print(_) 