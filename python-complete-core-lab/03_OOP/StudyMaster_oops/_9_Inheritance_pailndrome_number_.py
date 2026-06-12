"""
> In this module we are going to Solve the Palindrome Question fom different ways : -

  Question 2 : -
  Palindrome Number
  Design an object-oriented program in python to display/check palindrome Number:
  -> Write a program to determine whether a given positive integer is a palindrome or not without
      using any string or list only use logic and algorithm .
"""

# Basic example Inheritance using Palindrome
class X:
    def __init__(self):
        self.user = int(input("Enter the number : "))


class Y(X):
    def fun1(self):
        # super().__init__() # try store new value in user
        pln = int(''.join(reversed(str(self.user))))
        if pln == self.user:
            return f"Yes Palindrome"
        return f"Not Palindrome"


try:
    x = Y()  # auto initialize the constructor of parents class
    val = x.fun1()  # because constructor is not in child class
    print(val)
except:
    print("Enter correct input")

"""
Step-by-step flow line 19 :-
→ Take the integer → 123
    str(123) → "123"
→ Reverse the string → "123"
    reversed("123") → "3", "2", "1"
→ Join the reversed characters → "321"
    ''.join(["3","2","1"]) → "321"
→ Convert back to integer → 321
    int("321") → 321
Final check:
- If reversed value == original value → Palindrome
- Otherwise → Not Palindrome
"""



# Simple example of inheritance using Palindrome
class Module3:
    """class try to display plain_drome"""

    def __init__(self, user):
        self.usr_num = user

    def plain_drome(self):
        s = str(self.usr_num)
        if s == s[::-1]:  # Python Code Using Slicing
            return f"{self.usr_num} is a Palindrome number"
        else:
            return f"{self.usr_num} is not Palindrome number"


class Module1(Module3):
    """print the Palindrome number"""

    def __init__(self):
        super().__init__(user=12125)  # Dryrun on number that was given by user 11

    def digit_wise(self):
        import math  # by using log we count the digit of user input
        num = int(math.log10(self.usr_num)) + 1  # log10 tells us how many times to multiply the base (10) to reach x
        for i in range(num // 2):  # num=2, itr=(0:num//2, 0:2//2) =  0:1, i = 0 exit
            left = (self.usr_num // 10 ** (num - i - 1)) % 10  # left = (11//10**(2-0-1)%10 -> (11//10)%10 -> 1%10 :: 1
            right = (self.usr_num // 10 ** i) % 10  # right = (11//10**0)%10 -> (11//1)%10 --> 11%10 :: 1
            if left != right:  # Python Code Using integer mathematical model
                return f"{self.usr_num} is not Palindrome number"
        return f"{self.usr_num} is looks a Palindrome number"

# Dryrun on number 12121
# num = int(4.08)+1 -->  4+1 --> 5
# i = 0: num//2     -->  0:2 --> 0 1 3(exit)
# left  = (12121//10 ** (5-0-1))%10 ---> (12121//10 **4)%10  --> (12121//10000)%10 ---> 1%10  --> 1
#         (12121//10 ** (5-1-1))%10 ---  (12121//10 **3)%10  --> (12121//1000)%10  ---> 12%10 --> 2

# right = (12121//10 ** 0)%10       ---> (12121//1)%10       -->  12121%10                    --> 1
#         (12121//10 ** 1)%10       ---> (12121//10)%10      -->  1212%10                     --> 2

# return = 12121 is looks a Palindrome number.  1st == last



# creating instance from Module3
try:  #
    x = int(input("Enter the number : "))
    obj = Module3(user=x)
    print(obj.plain_drome())
except ValueError:
    print("Pls enter valid Character it's invalid")


# creating instance from Module1 or accessing
try:  # super class  attribute from derived class.
    # if constructor is not define parents in child class then
    x = Module1()  # parents constructor is automatically execute if instance is created.
    # print(x.digit_wise())
except ValueError:
    print("pls enter valid character ")



"""
# Explanation Module1 class : -
Its VVI to known how it's work (Module1):-
step1: Python read entire code but not yet execute before instantiation

step2: After execution of Model3 python execute try and inside that we
       create the instance from derived class(Module3).

step3: Now '__init__()' is auto initialize. after that 'super().__init__()'
       (
       Suppose we don't give the constructor.
       '__init__()' to child class what will be happen? ans -> interpreter
       try to find the '__init__()' to parents class and auto initialized
       ) 
       initialize the parents class '__init__()' and pass the value '11' 
       as argument from 'user'  to user parameter that assign in attribute 
       'usr_num'.

step4: 'user_num' value is accessible in derived class(child class) because it
       inherit property from Parents(Method3) now it's comes to calling function
       (super().__init__()) and return it's to calling method where 'obj' is created

step5: after that we invoke the 'digit_wise' method then python directly encounter 
       'digit_wise()' and in inside import the Library 'math' to using function log10(arg)
       to count how many times base 10 is multiplied to reached given number(self.usr_num). 

       Explanation log10(x)
       log10(1000) = log10(10^3) 
       This means: we need to raise the base (10) to the power of approximately 3 to produce the value 1000.
       That’s exactly what log10 does:
       # log₁₀(x) is the exponent to which the base 10 must be raised to produce the number x.

       -> log10 tells us how many times to multiply the base (10) to reach x
          So, here log10(11) So how many time multiply base (10) to reach 11 ?
          ans: single time 
              (how? because 10 needs to multiply only one time means 10^1 to reach 11)

          example : -
          log10(5)       ->  base need ?
          log10(10)      ->  base 10 need to multiply 1 time to reach x : 10^1 
          log10(1000000) ->  base 10 need to multiply 6 time to reach x : 10^6
          log10(1234567) ->  base 10 need to multiply 6 times to reach x : 10^6.somthing

          But Now in this statement we need to count digit of number that given by user. 
          suppose user enter number 1213421 how we can try to count -> 
          log10(1213421) means base 10 multiply at list approx 6 times 10^6 reach the 1213421.
          the exact value is in decimal 6.somthing to reach 1213421 . 
          Now to count the total digit of 1213421 we need to convert in integer and add 1
          so log10(x)+1 : 6.somthing+1 => int(log10(x))+1 --> 6+1 -> 7
          Now u see the total degit is 7 in given number : 1213421   

step6:   The self.usr_num attribute value is accessible because derived class access the super classes
         attributes now log(self.usr_num) means log10(11) that gives count digit of number in decimal
         we use int to get only integer so we get 1 why?(because base 10 needs only one time multiplication
         to reach approx at 11 : 10^1 = 10 but it a approx exactly in decimal) now we conver in int or add 1 to 
         get number of digit in user value

step7:   so num is store 2 after the define here via dry run:  
         for i in range(num //2): # num=2, itr=(0:num//2, 0:2//2) =  0:1, i = 0 exit
             left  = (self.usr_num // 10**(num-i-1))%10  # left = (11//10**(2-0-1)%10 -> (11//10)%10 -> 1%10 :: 1
             right = (self.usr_num // 10**i)%10 # right = (11//10**0)%10 -> (11//1)%10 --> 11%10 :: 1

step8:   according to condition if right and left digit are same then return the  this 'Is 11 Palindrome Yes : Tue'
         to calling method x.digit_wise()

step9:   print is display the returned value from module1 class.
         NOW when except is execute : In both cases of instance user send string or char value
                                      then except is execute at the place of attribute error that looks more 
                                      better in screen then error (red dotted spot)         
"""




# Creating palindrome with other logic using inheritance
class PalinDrome:
    def __init__(self, user_value):
        self.user_value = user_value
        self.original_val = self.user_value

class Display(PalinDrome):
    def __call__(self):
        self.reverse = 0
        for i in range(0, len(str(self.user_value))):   #       for digit in str(self.user_value):
            self.each_digit = self.user_value%10        #              self.reverse = self.reverse * 10 + int(digit)
            self.reverse = self.reverse*10 +self.each_digit
            self.user_value //= 10

        if self.reverse == self.original_val:
            return f"{self.original_val} is palindrome Number"
        else:
            return f"{self.original_val} is no palindrome Number"
try:
    x = int(input("Enter the number to check the palindrome number : "))
    obj = Display(x)
    final_output = obj() # try to trigger the call function
    print(final_output)

except ValueError:
    print("Pls enter the valid value")


'''
💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫

# Understandable Question try to understand : - 
# Palindrome number 
def is_palindrome_math():
    num = int(input("Enter the number : "))
    original = num
    reverse = 0

    while num > 0:                        # n  = 121 > 0 -> True,  12 > 0 -> True,  1 > 0 -> True,  0 > 0 -> False(exit)
        digit = num % 10                  # d  = 121   ->  1  -> 2 -> 1
        reverse = reverse * 10 + digit    # r  = 1     -> 12  -> 121
        num //= 10                        # n  = 121    ->  12 -> 1 -> 0.1

    if original == reverse:
        print(f"{original} is a palindrome number")
    else:
        print(f"{original} is not a palindrome number")

💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫💫
class MyClass:
    def __init__(self, user):
        self.user_num = str(user)
    def palindrome(self):
        left = 0
        right = len(self.user_num) - 1
        while left < right:
            if self.user_num[left] != self.user_num[right]:
                print(f"{self.user_num} Not palindrome")
                return
            left += 1
            right -= 1
        print("Palindrome")

obj = MyClass(user=121)
obj.palindrome()

'''
