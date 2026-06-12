"""
> In this module we are going to Solve teh matrix Question : -
  Question 1: -
  Matrix Addition
  Design an object-oriented program in python to perform matrix addition.
  -> Use a base class Matrix to handle the input of matrix elements from the user and to display any matrix.
  -> Use a derived class MatrixAddition that inherits from Matrix and contains a function to add two
     matrices and store the result.
  -> In the main function, allow the user to enter the dimensions and elements for two matrices, perform the
     addition using the derived class, and display the resultant matrix.
"""



class Matrix:
    """user first matrix"""
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def f_matrix(self):
        i, mat1st = 1, []
        while i < self.row+1:
            j, lst1st = 1, []
            while j < self.col+1:
                user_mat1st = int(input(f"Enter value of matrix a{i}{j} : "))
                lst1st.append(user_mat1st)
                j += 1
            mat1st.append(lst1st)
            i += 1
        return mat1st

    def s_matrix(self):
        mat2nd = []
        for i in range(1, self.row+1):
            lst2nd = []
            for j in range(1, self.col+1):
                user_mat2nd = int(input(f"Enter value of matrix b{i}{j} : "))
                lst2nd.append(user_mat2nd)
                j += 1
            mat2nd.append(lst2nd)
            i += 1
        return f"{mat2nd}"


class Addition(Matrix):
    """class body perform the addition fo matrix"""
    def __call__(self):

        user_row = int(input("Enter the row number of matrix : "))
        user_col = int(input("Enter the col number of matrix : "))

        print("\nEnter the element of 1st matrix :- ")
        obj = Matrix(row=user_row, col=user_col)
        matrix_1st = obj.f_matrix() # first matrix

        print("\nEnter the element of 2nd matrix :- ")
        matrix_2nd = obj.f_matrix() # second matrix

        #Display 1st matrix
        print("\nfirst matrix : -")
        for i in matrix_1st:
            print(i)

        #Display 2nd matrix
        print("\nsecond matrix : -")
        for j in matrix_2nd:
            print(j)


        try:
            # checking number of col and row are math or no
            if user_row== self.col:
                # addition of mat1 and mat2
                self.sum = []
                for i in range(len(matrix_1st)):  # [[10, 20] [30, 40]] >> [10, 20]
                    self.lst = []
                    for j in range(len(matrix_1st[0])):  # [[40, 50] [60, 70]] >> [40, 50] # wrong way matrix_1st
                        self.addition_value = matrix_1st[i][j] + matrix_2nd[i][j]
                        self.lst.append(self.addition_value)
                    self.sum.append(self.lst)
                return self.sum
        except ValueError:
            print()

def display():

    #creating object from Addition class
    x = Addition(2, 2)
    store_sum = x()

    #Display the Addition
    print(f"\nThe addition of both matrix is : - ")
    for i in store_sum:
        print(i)

display()  # function call


#Understanding : -
# can we add this : - [[3, 4],[7, 2],[5, 9]]+[[3, 1, 5],[6, 9, 7]]
# No, because addition requires both matrices to have the same dimensions
# means same number of rows and same number of columns (columns mismatch)
# in this case aij is 3x2 and bij is 2x3

