# Wap to print the multiplication of matrix using oops and in next module display the addition and multiplication 

class Matrix:
    """display the matrix using list """

    def __init__(self):
        """Initilize attribute"""
        self.m1 = [[1, 2], [2, 3]]
        self.m2 = [[4, 3], [2, 1]]

    @staticmethod
    def multiplication_matrix(m1, m2 ):
        """display the multiplication of matrix"""
        mat1 = m1#[[1, 2], [2, 3]]
        mat2 = m2#[[4, 3], [2, 1]]
        multi = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat2)):
                value = 0
                for k in range(len(mat2)):
                    value += mat1[i][k]*mat2[k][j]
                row.append(value) 
            multi.append(row) 
        print(multi) 


obj = Matrix()
obj.multiplication_matrix(m1 = obj.m1, m2 = obj.m2)

# [2, 2]      [3, 3]      [[14]]
# [2, 1]      [4, 1]      []
# multi >> [7]
# >> 0 to 2 >> 0 1 
# >> value row = 0 > [] = 14 [14] > 0 [7]  
# >> 0 to 2 >> 0 1 >>  0 1
