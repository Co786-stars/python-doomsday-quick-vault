""" 
Question 1) 
wap to create  two matrix mat1 and mat2  ?  # extra very important concept in 15 >> 16 file to clear vision of acess method attributes 
                                              and how pass argument ?  
explanation : - VVI 
In this class we create a two function matrix1 and matrix2 that coded as a function programming   there is only one difference 
in functional programming we call the function directly but in oops we use first object name and then we use muncation name
"""

class mymatrix:
    """perform the addition and multiplication of matrix"""
    
    # >> Not necassary for __init__
    # def __init__(self, row, col):
    #     """initialize the attribute of """
    #     self.matrow = row
    #     self.matcol = col


    def matrix1(matrow, matcol):  
        """ display matrix1st to user """ 
        matrix = []
        for i in range(matrow):
            mat1d = []
            for j in range(matcol):
                mat1d.append(int(input(f"Enter value : a{i+1}{j+1} : ")))
            matrix.append(mat1d)    
        # Display multidimansional as a matrix  
        for _ in matrix:
            print(_)
        return matrix


    def matrix2(value1, value2):
        """display matrix2nd to user"""
        matrix = []
        for i in range(1, value1+1):
            mat1d = []
            for j in range(1, value2+1): 
                mat1d.append(int(input("Enter value : ")))
            matrix.append(mat1d)
        for _ in matrix:
            print(_)
        return matrix        

mat = mymatrix
mat.matrix1(2, 2)  # first we give objectname and then function(arg1, arg2) name in opps programmin but in functional
mat.matrix2(2, 2)  # we only give function name for calling 