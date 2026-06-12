class Concept:

    def __init__(self, p1='', p2=''):
        self.row = p1
        self.col = p2

    def mat1(self, row, col):
        """body use to display the matrix 1st"""
        matrix1st = []
        i = 1
        while i < row+1:    # outer loop for row
            singled = []
            j = 1
            while j < col+1:   # inner loop for column
                singled.append(int(input(f"Enter value : a[{i}][{j}] : ")))
                j += 1
            matrix1st.append(singled)  # append single dimension
            i += 1
        for mat in matrix1st:    # loop print as a display
            print(mat)
        return matrix1st


    def mat2(self, value1, value2):
        """body use to display the matrix 2nd"""
        matrix2nd = []
        for i in range(1, value1+1):  # outer loop for row
            oned = []
            for j in range(1, value2+1):  # inner loop for column
                oned.append(int(input(f"Enter value : a2[{i}][{j}] : ")))   # append user value to list
            matrix2nd.append(oned)
        for mat2 in matrix2nd:  # append list to user list
             print(mat2)
        return matrix2nd


    def add(self, arg1, arg2):
        addition = []
        i = 1
        while i < len(arg1)+1:  # outer loop for row
            add_num = []
            j = 1
            while j < len(arg2)+1:  # inner loop for column
                add_num.append(arg1[i-1][j-1] + arg2[i-1][j-1])  # addition of element
                j += 1
            addition.append(add_num)
            i += 1
        k = 1
        print("Addition of matrix : -")
        while k < len(addition)+1:  # loop use for display addition as matrix
            print(addition[k-1])
            k += 1


    @classmethod
    def multiply(cls, row, col):
        """body use to display multiplication """
        if len(row) != len(col):
            return print("multiplication is not possible")
        else:
            multi = []
            for i in range(len(row)):   # outer loop as a row
                single = []
                for j in range(len(col)): # inner loop as a col
                    m = 0
                    for k in range(len(col)):  # loop for multiplication
                        m += row[i][k]*col[k][j]
                    single.append(m)
                multi.append(single)
            print("Multiplication of Matrix : - ")
            for _ in multi:
                print(_)
            return multi


    @staticmethod
    def hollow_hourglass_pattern():
        """use to display hollow hour glass pattern"""
        user = int(input("Enter the row number : "))
        if user%2 == 0:
            user += 1   # increment in user to make odd
        spc1 = spc2 = user
        for i in range(1, user+1):

            if i <= user/2:
                for j in range(1, 2*i):
                    print("-", end='')

                for k in range(1, spc2+1):
                    print("*", end=" ")
                spc2 -= 2
            else:
                for j in range(1, spc1+1):
                    print("-", end="")

                for k in range(1, (user+1)-spc1+1):
                    print("*", end=" ")
                spc1 -= 2
            print()

matrix = Concept()
mat1 = matrix.mat1(row = 2, col = 2)
mat2 = matrix.mat2(value1 = 2, value2 = 2)
matrix.add(arg1 = mat1, arg2 = mat2)
matrix.multiply(mat1, mat2)
matrix.hollow_hourglass_pattern()

