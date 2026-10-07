# 1. Write a program to check whether a given number is a palindrome.
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


# For_TimePass
x = 50
if x >= 50:
    print(f"Hello wizard {x} is greater the 50")
else:
    print("condition is not matched")

