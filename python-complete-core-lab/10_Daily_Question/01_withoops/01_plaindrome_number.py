# Q1. Write a program to check whether a given number is a palindrome using OOPS concept.
# Explain your approach.
class Number:
    """class body is try to display the palindrome number"""
    def __init__(self, n):
        """constructor create the attribute"""
        self.n = n

class Palindrome(Number):
    """child try to display the num is palindrome or not"""
    def solution(self):
        """method is display the palindrome number"""
        self.usr, self.lst = self.n, []
        for i in range(1, len(str(self.n))+1):
            self.rem = self.usr%10
            self.lst.append(self.rem)
            self.usr = self.usr//10

        if self.lst == self.lst[::-1]:
            return f"The given number {self.n} is Palindrome"
        else:
            return f"The number {self.n} is Not Palindrome" # executed

try:
     _user = int(input("Enter the number to check palindrome or not : "))
     _palindrome = Palindrome(n=_user) # creating an object from _Palindrome
     final_output = _palindrome.solution() # revoke the method from _palindrome
     print(final_output)
except ValueError:
    print("pls enter valid numer str not allow")

# -> (AI Review: 6.5/10)
# -> Need to improve code
# Works correctly ✔
# Logic is valid ✔
# But uses extra space, unnecessary attributes, and string conversion ❌
# Not optimized ❌
# Docstrings need improvement ❌
# ---------------------------------------------------------------------------------------------------------------

# Q2. Reverse a number using mathematical operations and check if the reversed number
#     is equal to the original. Explain the approach.

class Palindrome2(Number):
    """child try to display the palindrome number without using slice/indexing method"""
    self.var1 = _
    def solution(self):
