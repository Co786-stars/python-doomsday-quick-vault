# WAPP to check the Number is Prime or Not
# The Number that have a two factor 1 and itself called prime
# ex : 2 3 5 7 11 13 ...101 102 103..etc

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# Explanation : -
# _____________________________________________________________________________#

def isprimenumber(user_number):
    """check the number is prime or not"""
    if user_number <=1:
        x = True # because if value is false is not prime number
    else:
        x = False # because if value is true means prime 

    for i in range(2, user_number):
        if user_number%i == 0:
            x = True
            break
    if x :
        print(f"{gnum} is a prime Not number")
    else:
        print(f"{gnum} is a prime number ")

gnum = int(input("Enter the prime Number : "))    
isprimenumber(gnum)

# _____________________________________________________________________________#

class Number:
    def __init__(self):
        """initilize the attribute"""
        self.var1 = int(input("Enter the number : "))  # take the number from use and asign in var1
        

    def isprimenumber(self):
        "check the number is prime or not"
        if self.var1 == 1:
            self.prime = True  # True  is assign because 1 have only one factor so it not prime 
        else: 
            self.prime = False  # false is assign because number that have a exactly two factor given in false statment 

        self.num1 = self.var1
        # check the factctor of the numbers number (number that is not prime )
        for i in range(2, self.num1):
            if self.var1%i == 0:  # given number is check is it is exactly devisible or not 
                self.prime = True # if the number is devisible the this is not prime means more the on factor 
                break

        if self.prime:     # first condition is true in the calse of 1 otherwise when number have more then two factor 
            print(f"{self.var1} is Not prime number")
        else:
            print(f"{self.var1} is a prime Number")

isprime = Number()
isprime.isprimenumber()

# _____________________________________________________________________________#

print(int(9**0.5))
