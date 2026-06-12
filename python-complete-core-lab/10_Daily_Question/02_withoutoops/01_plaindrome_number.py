# Write a program to check whether a given number is a palindrome.
# How would you determine if an integer is a palindrome without converting it to a string?
# Given a number, reverse it and check if the reversed number is equal to the original. Explain your approach.
# How can you check if a number is a palindrome using modulo and division operations?
# Write an optimized solution to check palindrome numbers for very large inputs.
# Explain how you would handle negative numbers in a palindrome check.
# Check if a number is a palindrome using recursion.
# Given a range of numbers, print all palindrome numbers within that range.
# How would you check if a number is a palindrome in constant space?
# What edge cases should be considered when checking for palindrome numbers?


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
        for i in range(1, len(str(self.n))+1): #
            self.rem = self.usr%10             # logic: 123 => 3,  2, 1, exit
            self.lst.append(self.rem)          # _list:     => 3,  2, 1, exit
            self.usr = self.usr//10            # __usr:     => 12, 1, exit

        if self.lst == self.lst[::-1]:  # condition check: [1, 2, 3] == [3, 2, 1] => False
            return f"The given number {self.n} is Palindrome"
        else:
            return f"The number {self.n} is Not Palindrome" # executed

try:
     _user = int(input("Enter the number to check palindrome or not : "))
     _palindrome = Palindrome(n=_user) # creating an object from _Palindrome
     final_output = _palindrome.solution() # revoke the method from _palindrome
     print(final_output)

except:
    print("pls enter valid numer str not allow")

