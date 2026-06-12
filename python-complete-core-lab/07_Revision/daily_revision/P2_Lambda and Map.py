# Definition:-
# map() takes a function and one or more iterables, applies the function to each element,
# and produces a map object (iterator). Converting it to list/tuple shows the results.

# Syntax:-
# map(function, iterable1, iterable2, ...)

m = ['1', '2', '3', '4']
t = map(int, m)   # map() applies int() to each element of m
print(list(t), list(m))
'''
Step 1: When Python reads line (t = map(int, m)),
        it does not immediately convert the strings.
        It only creates a map object (an iterator) that knows
        how to apply int() to each element of m later.

Step 2: When Python reaches line (print(list(t), list(m))),
        it now starts consuming the map object.

Step 3: At this moment, Python goes back to line (t = map(int,m)) 
        internally and applies int() to the first element of m:
        '1' → 1. Then it continues for each element:
        '2' → 2, '3' → 3, '4' → 4.

Step 4: After converting all elements, list(t) becomes [1, 2, 3, 4].

Step 5: The original list m is unchanged, so list(m) still shows ['1', '2', '3', '4'].

Note : - 
line 9th only sets up the map object, and line 10th is where the actual conversion 
happens, one element at a time, before printing.
'''


def func(num):
    return len(num)   # func() takes a string and returns its length

var = ('word', 'wait', 'wizard')   # tuple of strings
t = map(func, var)   # map() sets up an iterator to apply func() to each element of var
print(list(t))       # consuming the map object to see results
'''
Step 1: → Python defines func(num), which returns the length of a string.
Step 2: → var is a tuple ('word', 'wait', 'wizard').
Step 3: → t = map(func, var). No function calls yet, only a map object created.
Step 4: → print(list(t)) starts consuming the map object.
          Internally Python calls func() one by one:
            func('word')   → len('word')   → 4 → list becomes [4]
            func('wait')   → len('wait')   → 4 → list becomes [4, 4]
            func('wizard') → len('wizard') → 6 → list becomes [4, 4, 6]
Step 5: → Finally, list(t) = [4, 4, 6] is printed.
'''




# Definition :-
# - A lambda function is an anonymous (no name) function defined with the keyword `lambda`.
# - It can take any number of arguments but must have only one expression.
# - The result of that single expression is automatically returned.
# - Lambda → only one expression (can include inline if … else).
# - In Python, a lambda cannot hold multiple statements.

# Important Note (confusion clarified):
# - You cannot write full if/else blocks inside a lambda.
# - Instead, use a single conditional expression:
#     lambda d: "Even" if d % 2 == 0 else "Odd"
# - If you need multiple statements (like printing before and after),
#   then use a normal def function.

# Syntax :-
# lambda arguments: expression
# - lambda → keyword to define the function
# - arguments → input parameters (like in a normal function)
# - expression → a single expression that gets evaluated and returned


# Note :-
# - A lambda function is just a quick way to write a function inline.
# - Often used when you don’t want to define a full def function.


# Difference :-
# - lambda → one expression only (can use inline if … else).
# - def → use when you need multiple statements before/after condition.


# Example Concept : -
# # Normal function
# def square(x):
#     return x * x
#
# # Lambda equivalent
# square = lambda x: x * x
# print(square_lambda(5))  # Output: 25



f = lambda x, y: x + y
print(f(3, 2)) # output:5
'''
Explanation:
→ f is defined as a lambda function.
    It takes two arguments (x, y) and returns their sum (x + y).

→ When we call f(3, 2):
     Internally Python substitutes x = 3, y = 2
     → evaluates 3 + 2
     → returns 5
  f(x, y) simply returns x + y.
  
→ Manual way: -
   def f(x, y):
     return x + y
'''


lst = ['4', '3', '2', '1']
f = map(lambda arg: int(arg), lst)
print(list(f))
'''
→ Manual way : -
def f(arg):
    return int(arg)   # convert each string to int

lst = ['4', '3', '2', '1']
t = map(f, lst)       # now f is applied to each element
print(list(t))        # Output: [4, 3, 2, 1]
'''




#########################################################################################
# ---------------- Code ----------------
num = [1, 2, 3, 4]
square = list(map(lambda x: x*x, num))
print(square)  # [1, 4, 9, 16]

# ---------------- Execution Flow (Hindi) ----------------
# 1. Sabse pehle ek list 'num' banayi gayi → [1, 2, 3, 4]
# 2. map() function call hota hai. Ye do cheez leta hai:
#    - ek function (yaha lambda x: x*x)
#    - ek iterable (yaha list 'num')
# 3. map() iterable ke elements ko ek ek karke function ke argument 'x' me bhejta hai.
# 4. Har iteration me lambda function execute hota hai:
#    - Pehla element 1 → x=1 → return 1*1 = 1
#    - Dusra element 2 → x=2 → return 2*2 = 4
#    - Teesra element 3 → x=3 → return 3*3 = 9
#    - Chautha element 4 → x=4 → return 4*4 = 16
# 5. Ye sab return values ek internal iterator (map object) me store hoti hain.
#    Iterator ek "lazy storage" hai jo values ko ek ek karke ready rakhta hai.
# 6. Jab hum list() lagate hain, to wo iterator ke andar ke results ko ek proper list me convert kar deta hai.
# 7. Final output milta hai → [1, 4, 9, 16]

# Note : -
# - map() ek iterator banata hai (lazy storage).
# - lambda har element par apply hota hai.
# - list() us iterator ko ek proper list me convert kar deta hai.



# ---------------- Execution Flow (English) ----------------
# 1. First, a list 'num' is created → [1, 2, 3, 4]
# 2. map() function is called. It takes two things:
#    - a function (here lambda x: x*x)
#    - an iterable (here the list 'num')
# 3. map() sends each element of the iterable one by one into the function’s argument 'x'.
# 4. On each iteration, the lambda function executes:
#    - First element 1 → x=1 → return 1*1 = 1
#    - Second element 2 → x=2 → return 2*2 = 4
#    - Third element 3 → x=3 → return 3*3 = 9
#    - Fourth element 4 → x=4 → return 4*4 = 16
# 5. All these return values are collected inside an internal iterator (map object).
#    The iterator is a "lazy storage" that keeps values ready one by one.
# 6. When we call list(), it converts the iterator results into a proper list.
# 7. Final output → [1, 4, 9, 16]

# Note : -
# - map() ek iterator banata hai (lazy storage).
# - lambda har element par apply hota hai.
# - list() us iterator ko ek proper list me convert kar deta hai.

#########################################################################################
p = (10, 20, 30)
# lambda function to check even number
s = lambda d: d % 2 == 0

# map() applies lambda on each element of tuple
# list() converts the map object (iterator) into a list
print(list(map(s, p)))  # [True, True, True]



# Lambda with conditional expression
check = lambda d: "Even" if d % 2 == 0 else "Odd"
print(check(10))  # Even
print(check(21))  # Odd


# lambda with conditional expression
tpl = ('wizard', 'provide', 'wrong', 'or', 'Write')
count = lambda c: "Correct" if len(c) == 5 else "Incorrect"
func_ = map(count, tpl)
print(list(func_))





# Definition :-
# filter() is used to select elements from a sequence based on a condition.
# It keeps only those elements for which the function returns True.

# Syntax :-
# filter(function, iterable)

# Important Note :-
# - function → should return True or False
# - iterable → list, tuple, etc.
# - Result → filter object (convert to list/tuple to see values)

# Difference :-
# - map() → transforms all elements
# - filter() → selects only elements that satisfy condition


# How it works :-
# 1. Takes each element from the iterable.
# 2. Passes it to the function.
# 3. If function returns True → element is kept.
# 4. If function returns False → element is discarded.
# 5. Returns a filter object (iterator).

# Example :-
tpl = ('wizard', 'provide', 'wrong', 'or', 'Write')
check = lambda c: len(c) == 5
result = filter(check, tpl)
print(list(result))   # ['wrong', 'Write']