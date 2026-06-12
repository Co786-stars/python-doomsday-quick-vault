'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Generate coordinates excluding those where i+j+k == n
    coordinates = [[i, j, k]
                   for i in range(x + 1)
                   for j in range(y + 1)
                   for k in range(z + 1) if i + j + k != n]
    print(coordinates)
'''

# syntax
# [expression for item in iterable if condition]

# Task/Question
# Let's learn about list comprehensions! You are given three integers  x, y and z  representing the dimensions
# of a cuboid along with an integer n . Print a list of all possible coordinates given by  (i, j, k) on a 3D grid
# Where the sum of i+j+k is not equal to n. Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather
# than multiple loops, as a learning exercise.
# x = 1
# y = 2
# z = 3
# n = 3

# All permutations of [i, j, k] are:
# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1, 0, 2], [1,1,0], [1,1,1], [1,1,2]]

# Print an array of the elements that do not sum to n = 3.
# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0],[1,1,2]]

# Input Format
# Four integers  x, y z and n , each on a separate line.

# Constraints
# Print the list in lexicographic increasing order.
# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output___________________________________________
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# ________________________________________________________


# Sample Input 0
# 2
# 2
# 2
# 2
# Sample Output________________________________________________________________
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0],
# [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1],
# [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
# ________________________________________________________________________________

class Cuboid:
    """class body is display 3D grid combinations"""
    def __init__(self, x, y, z, n):
        """constructor is initialized with a cuboid object/attributes"""
        self.x, self.y, self.z, self.n = x, y, z, n

    def actions(self):
        """Logic is defined inside the method body"""
        self.cuboid = []
        i = 0
        while i <= self.x:  #outer loop
            self.f = i
            j = 0
            while j <= self.y: #inner loop
                self.s = j
                k = 0
                while k <= self.z: #inner loop
                    self.t = k
                    if self.f + self.s + self.t != self.n: #condition
                        self.cuboid.append([self.f, self.s, self.t])
                    k += 1
                j += 1
            i += 1
        return self.cuboid

class Display(Cuboid):
    """subclass is display the cuboid 3d dimension"""
    def __init__(self, a, b, c, sum_):
        """constructor is initialized with a Display object/attribute"""
        # super().__init__(x=a, y=b, z=c, n=sum_)
        self.C3D = Cuboid(a, b, c, sum_)
        self.final_output = self.C3D.actions() # calling the method from parents class
        # return self.final_output # error are display because __init__ doesn't return list

    def show(self):
        """method is return the value of combanation/3d_Diminsion"""
        return self.final_output

try:
    a = int(input("Enter the value 1st : "))
    b = int(input("Enter the value 2nd : "))
    c = int(input("Enter the value 3rd : "))
    sum_ = int(input("Enter the value nth : "))
    obj = Display(a, b, c, sum_)
    output = obj.show()
    print(output) # final output are displayed

except ValueError:
    print("Value is invalid so pls enter valid number")


# Comprehension way (short and clean)
# Manual way (using loops) : -
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

# # # List comprehension
# # coordinates = [[i, j, k]
# #                for i in range(x + 1)
# #                for j in range(y + 1)
# #                for k in range(z + 1)
# #                if i + j + k != n]
#
# # print(coordinates)
#
#
# # coordinates = []
# # for i in range(x+1):
# #     for j in range(y+1):
# #         for k in range(z+1):
# #             if i + j + k != n:
# #                 coordinates.append([i, j, k])
