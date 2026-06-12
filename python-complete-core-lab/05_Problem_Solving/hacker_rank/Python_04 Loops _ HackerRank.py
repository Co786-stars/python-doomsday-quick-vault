def _square(p1):
    _ = 0
    while _ <= n-1:
        """try to display the positive Square"""
        var = _*_
        print(var)
        _ += 1

try:
    n = int(input("Enter the number : "))
    _square(p1=n)
except ValueError:
    print("Pls enter the correct/valid number")


'''
if __name__ == '__main__':
    n = int(input())

class Integer:
    """class body is try to display square of the each number"""

    def __init__(self, n):
        self.user_value = n

    def actions(self):
        """method try to display the positive square"""
        if self.user_value >= 0:
            for i in range(self.user_value):
                "set the range from 0 to n in loop"
                self.square = i * i
                print(f"{self.square}")
        else:
            """else method to flex the error value"""
            print(f"{self.user_value} is Invalid try again")


try:
    final_output = Integer(n)
    # the value enter via user is passed as default argument from n
    final_output.actions()  # invoked then method from Integer class
except ValueError:
    if n < 0:
        print("Pls enter the positive integer")
    else:
        print("Pls enter the positive numeric integer")
'''



# Task/Question:-
# The provided code stub reads an integer,n,from STDIN. For all non-negative integers , i < n print i^2.
# Example : n = 3
# The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the square of each number on
# a separate line.
# Input Format :-
# 0
# 1
# 2
# 4
# The first and only line contains the integer,n.

# Extra : - other method
# if __name__ == '__main__':
#     n = int(input())
#     i = 0
#     while i < n:
#         print(f"{i*i}")
#         i += 1

