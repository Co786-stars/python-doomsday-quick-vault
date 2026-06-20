# How would you determine if an integer is a palindrome without converting it to a string?
# Given a number, reverse it and check if the reversed number is equal to the original. Explain your approach.
# How can you check if a number is a palindrome using modulo and division operations?
# Write an optimized solution to check palindrome numbers for very large inputs.
# Explain how you would handle negative numbers in a palindrome check.
# Check if a number is a palindrome using recursion.
# Given a range of numbers, print all palindrome numbers within that range.
# How would you check if a number is a palindrome in constant space?
# What edge cases should be considered when checking for palindrome numbers?

# _1 Write a program to check whether a given number is a palindrome.

def palindrome(n):
    """displayed the palindrome number"""
    duplicate = str(n)
    rev = int(duplicate[::-1])

    if n == rev:
        """checked the number palindrome or not"""
        return f"{n} is palindrome number"
    else:
        return f"{n} is not palindrome number"

try:
    n = int(input("Enter the number to check palindrome : "))
    p = palindrome(n)
    print(p)

except ValueError:
    print("pls enter integer value ")

