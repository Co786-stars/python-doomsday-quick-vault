"""
> In this module we are going to Solve teh matrix Question : -
  Question 1 : -
  Matrix Multiplication
  Design an object-oriented program in python to perform matrix multiplication:
  -> Use a base class `Matrix` with member functions for reading a matrix from the user and for displaying a matrix.
  -> Use a derived class `MatrixMultiply` that inherits from `Matrix` and implements a method to multiply two matrices, checking for compatible dimensions (number of columns of the first matrix must equal the number of rows of the second matrix).
  -> In the `main` function, allow the user to input two matrices, use the derived class to compute the product, and display the resulting product matrix. If the dimensions are incompatible, display an appropriate error message.
"""
# from A_to_z.third import addition


class Matrix:
    """class try to display the matrix """
    def __init__(self, row, col):
        """initialize the attribute"""
        self.r = row
        self.c = col  # call the matrix first
        self.mat1st = DisplayMatrix.matrix1st(user_row = self.r, user_col = self.c)

        #user input value of second matrix
        self.mat2row = int(input("Enter the row of 2nd matrix "))
        self.mat2col = int(input("Enter the col of 2nd matrix "))  # call the matrix second
        self.mat2nd = DisplayMatrix.matrix2nd(given_row=self.mat2row, given_col=self.mat2col)



class DisplayMatrix:
    @classmethod
    def matrix1st(cls, user_row, user_col):

        i, cls.mat1 = 1, []
        while i < user_row+1:
            cls.lst = []

            j = 1
            while j < user_col+1:
                cls.user_value = int(input(f"Enter the value of mat1st{i}{j} of matrix1st : "))
                cls.lst.append(cls.user_value)
                j += 1
            cls.mat1.append(cls.lst)
            i += 1
        print("\n")
        return  cls.mat1

    @classmethod
    def matrix2nd(cls, given_row, given_col):
        cls.mat2 = []
        for i in range(1, given_row+1):
            cls.lst = []
            for j in range(1, given_col+1):
                cls.user_value =  int(input(f"Enter the value of mat2nd{i}{j} of matrix2nd : "))
                cls.lst.append(cls.user_value)
            cls.mat2.append(cls.lst)
        return cls.mat2


class MultiplicationAddition(Matrix):
    """try to display the both matrix and multiplication or addition extra also"""

    def display_matrix(self):

        print("\n")
        print("This is the matrix 1st : -")
        # try to display the matrix 1st in proper format
        for i in self.mat1st:
            print(i)

        print("\n")
        print("This the the matrix 2nd : - ")
        #try to display the matrix 2nd in proper format
        for i in self.mat2nd:
            print(i)


    def addition_matrix(self):
        """try to add the matrix1 and matrix2"""
        self.mat_addition = []
        for i in range(len(self.mat1st)):
            self.lst = []
            for j in range(len(self.mat2nd[0])):
                self.mat_add = self.mat1st[i][j] + self.mat2nd[i][j]
                self.lst.append(self.mat_add)
            self.mat_addition.append(self.lst)

        print("\n")  # Now try to break the lines
        # try display the matrix addition in proper formatt
        print("The addition of the matrix is : - ")
        for _ in self.mat_addition:
            print(_)  #return to the matrx




    def multi_matrix(self):
        """try to multiply the matrix1 and matrix2"""
        self.mat_multipy = []

        # high leval of thinking (better way to think)
        """for i in range(len(self.mat1st)):
            row = []
            for j in range(len(self.mat2nd[0])):
                sum_product = 0
                for k in range(len(self.mat2nd)):
                    sum_product += self.mat1st[i][k] * self.mat2nd[k][j]
                row.append(sum_product)
            self.mat_multipy.append(row) ...............copilot  suggestion to use this way that is in comment section"""

        # my leval fo thinking
        for  i in range(len(self.mat1st)):   # it's prefect but not proper prefect according to copilot
            self.multi, self.lst = 0, []
            for j in range(len(self.mat2nd[0])):
                x = 1
                for k in range(1, len(self.mat2nd)):
                    self.multi = self.mat1st[i][k]*self.mat2nd[i][j] + self.mat1st[i][x]*self.mat2nd[x][j]
                    self.lst.append(self.multi)
            self.mat_multipy.append(self.lst)

        print("\n")  # Now try to break the lines
        # try display the matrix multiplication in proper format
        print("The multiplication of the matrix is : - ")
        for _ in self.mat_multipy:
            print(_)




# i = 0 -> 1  -> false exit
# j = 0 -> 1 -> false exit =  0
# k = 0 ->
# ( mat1st00*mat2nd00 + mat1st01*mat2nd10 )      mat1st00*mat2nd01 + mat1st01*mat2nd11
# ( mat1st10*mat2nd00 + mat1st11*mat2nd10 )      mat1st10*mat2nd01 + mat1st11*mat2nd11
# Rough  [a11 a12]   [b11 b12]  = [ (a11*b11 + a12*b21)   (a11*b12 + a12*b22) ]
#        [a21 a22]   [b21 b22]  = [ (a21*b11 + a22*b21)   (a21*b12 + a22*b22) ]



try:
    row = int(input("Enter the row of 1st matrix : "))
    col = int(input("Enter the col of 2nd matrix : "))

    # try to Display the both matrix
    obj = MultiplicationAddition(row, col)
    obj.display_matrix()

    # displaying the addition of the matrix
    obj.addition_matrix()

    # displaying the multiplication of the matrix
    obj.multi_matrix()

except ValueError:
    print("Pls enter the valid number  ....")







"""
# basic dryrun  ROUGH to REMBER PREVIOUS PROGRAM 
2
2
obj = pass the value from row and col
r =  2
c = 2
user_row = 2
user_col = 2

#loop
i = 1:3 --> 1 2 3 exit
mat1 = [[10, 20], [30, 40]]
 lst = [10, 20] ->  [30, 40]

j > 1, 1:3 --> 1 2 3 exit ,  j > 1 , 1:3 --> 1 2 3 exit
uv = mat11 = 10,  mat22 = 20, mat21 = 30,   
         mat22 = 40

at the end self.mat1st store the matrix 
= [[10, 20], [30, 40]]

_________________________
2
2
mat2 = [[40, 30 ], [ 20, 10]
i  = 1:3 -> 1, 2
lst  = [40, 30] -> [20, 10]
j = 1:3 -> 1 2 3exit  , j = 1:3 -> 1 2 3
uv = mat2nd11 = 40, mat2nd12 = 30
        mat2nd21 = 20 , mat2nd22 = 10
now the final value is store in self.mat2nd
 = [[40, 30], [20, 10]]


This is the matrix   1st :  -
i = [10, 20] -> [30, 40]
[10, 20]
[30, 40]


This is the matrix   2nd -
i = [40, 30] -> [20, 30]
[40, 30]
[20, 10]
"""

