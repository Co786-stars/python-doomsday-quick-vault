"""
>In this module we are going to Discuss___________________________ Decorators_______and________Type of Decorators______

------------------------------------------------------------------------------------------------------------------------
A decorator in Python is a design pattern or feature that allows you to modify or extend the behavior of a function,
method, or class without permanently changing its code. It is a form of metaprogramming.

A decorator is a callable (function or class) that takes another function or class as input and returns a new or
modified version of it.

It uses the @decorator_name syntax placed above the target function or class to apply the transformation dynamically,
without altering the original code structure.

Basic Syntax : -
@decorator_name
def function_name():
    pass

Decorators in Python are categorized based on the following criteria:-
Target – Refers to what the decorator is applied to:
functions, methods, or classes.

Implementation – Refers to how the decorator is constructed:
function-based or class-based.

Usage – Refers to how the decorator is utilized in code:
with arguments, chained, or built-in (e.g., @staticmethod, @classmethod).

In simple way :-
Decorators are just functions that take another function, wrap it, and return a new function.
They’re widely used for logging, access control, timing, caching, and more.
The @decorator_name syntax is syntactic sugar to make code cleaner.

------------------------------------------------------------------------------------------------------------------------

Types of Decorators in Python : -
Function Decorators – Target regular functions.
Class Decorators – Target entire classes.
Method Decorators – Target methods inside classes (e.g., @staticmethod, @property, @classmethod, Custom).
Built-in Decorators – Provided by Python itself (e.g., @staticmethod, @classmethod, @property).
Decorators with Arguments – Accept parameters to customize behavior.
Class-Based Decorators – Implemented using classes with __call__.
Chained Decorators – Multiple decorators applied to a single function or method


Now
# A Use case is a real-world situation or problem where something (like a decorator) is used to solve it or make it easier.
The Common Use Cases of Decorators in Python :-
Use Case	          Purpose	                                                    Decorator Type Used
Logging	              Track function calls, arguments, and return values	        Function Decorator
Authentication	      Restrict access based on user roles or permissions	        Parameterized Decorator
Timing Execution	  Measure how long a function takes to run	                    Function Decorator
Caching Results	      Store results to avoid repeated calculations	                Built-in Decorator (@lru_cache)
Validation	          Check input types or values before executing a function	    Function or Parameterized
Retry Logic	          Retry a function if it fails (e.g., network calls)	        Parameterized Decorator
Rate Limiting	      Limit how often a function can be called	                    Function Decorator
Memoization	          Cache results in recursive functions	                        Built-in Decorator (@lru_cache)
Access Control     	  Enforce user-level access to functions	                    Parameterized Decorator
Debugging	          Print detailed debug info during development	                Function Decorator
Monitoring	          Track usage metrics or errors in production	                Function or Class Decorator
Pre/Post Hooks	      Run code before or after a function	                        Function Decorator
Dependency Injection  Inject dependencies dynamically	                            Class-Based Decorator
Exception Handling	  Catch and log exceptions gracefully	                        Function Decorator

_______________________________________________________________________________________________________________________
🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏
PROPER CONCEPT OF PRACTICAL BASED CLEAR THE VISION OF DECORATOR IN PYTHON HOW IT's WORK IN DIFFERENT SITUATION
🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏
________________________________________________________________________________________________________________________
|SIMPLE CONCEPT OF CODING FOR DECORATOR ?|
🍎
Functional Programming Example: Passing a Function as an Argument
# ( create a base to understand decorator)
def function_name(arg1):
    '''This function receives another function and calls it.'''
    arg1()  # Call the function passed as argument

def new_function():
    print("3rd func")

new_function()  # Call the function directly
function_name(new_function)  # Pass the function as an argument to another function

# 🔍 How It Works:
# 1. Python reads all function definitions but doesn't execute them until called.
# 2. 'new_function()' is called directly and prints "3rd func".
# 3. 'function_name(new_function)' passes the function object 'new_function' to 'function_name'.
# 4. Inside 'function_name', 'arg1()' is executed — which is actually 'new_function()'.
# 5. So "3rd func" is printed again, this time from inside another function.
# 6. This demonstrates how functions can be passed and executed like any other variable.
# 7. This is a foundational concept in functional programming.
# 8. It's also the base idea behind decorators — modifying behavior by wrapping functions.



Functional Decorator (target regular function) ?
A functional decorator is a function that takes another function as input, wraps it with additional behavior
(adds some functionality to it), and returns a new function.

Syntax(1):-
# creating function decorator manually means without using @decorator_name
def outer_function(arg):
    '''representing functional decorator'''
    def inner_function():
        value = arg()  # calling the original function
        print(value)   #
    return inner_function

def unknown_func():
    return "This is unknown function"

# Direct call
obj1 = unknown_func()
print(obj1)

# Decorator applied manually
obj2 = outer_function(unknown_func)  # How we can say it is decorator because
obj2()  # it takes another function, wraps it, and returns a new function



Syntax(2):-
creating functional decorator manually means without using @decorator_name
def wizard(arg):
    def hacker():
       x = arg(2, 4)
       print(x)
    return hacker

# Decorator (manually decorate the python program)
def welcome(a, b):
    return a+b

# this is the original way to we 'x()()' initialize the nested function
wizard(welcome)() # call the manual decorator

obj1 = wizard(arg=welcome) # calling function
obj1()

obj2 = wizard
obj2(arg=welcome)() # calling function

'''
# Explanation : How it's works : -
1. Python is an interpreted language, so it reads the code from top to bottom. When it encounters function definitions,
   it stores them in memory but doesn't execute the code inside until the function is called.

2. When we write wizard(welcome), Python executes the wizard function and returns the nested function hacker
   However, hacker is not executed yet — only the function name(object) hacker is returned. To execute it, we must add parentheses: wizard(welcome)()
   which means hacker()

3. Now the interpreter enters the 'hacker' function and invokes 'arg(2, 4)'. (Technically, this means 'welcome(1, 4)' is invoked) —
   the decorated function is executed and returns the addition of `a` and `b`, to calling function and then stored in `x`.

4. 'print(x)' displays the value that stored in 'x' on the output screen. and interpreter directly encountered to calling
    function wizard(welcome)() that is technically hacker()

5.  Now the Question is why interpreter not read 'return hacker' ?
    Because interpreter does not re-read return hacker because that line was already executed earlier when wizard(welcome) was called.
    when we call hacker(), only the body of hacker is executed — it does not go back to wizard.

    Note : - When the inner function finishes, control goes back to the outer function or calling point
'''


Syntax(3):- DECORATE USING MANUALLY
def logging_case(func):
    def warpper(usr_input):
         ret_var = func(usr_input) # even_odd(usr_input)
         print(f'{usr_input} is an {ret_var}')
    return warpper

#MANUALLY DECORATED WITHOUT USING @decorator_name
def even_odd(num):
    #function body try to check the number is even or odd
    if num%2 == 0:
        return f"Even number "
    elif num%2 == 1:
        return f"Odd number "
    else:
        return f"Invalid input"

user_value = int(input("Enter the number to check even or odd : "))
obj = logging_case(func=even_odd)(usr_input=user_value)
print(obj) # None is shown because the 'warpper' function does not return anything.
           # It only prints the result, so 'obj' gets assigned None.



Syntax(4):- DECORATE using @decorator_name
def logging_example(value):
    def new_features(usrv):
        var = value(usrv)
        return f"The value that you gave {usrv} is {var}"
    return new_features

@logging_example
def check_sign(arg):
    if arg == 0:
        return "neutral"
    elif arg < 0:
        return "negative"
    else:
        return "positive"

# Very Important Concept (VVI)
# There are two ways to call the function:
# 1. Directly using the decorated function (with @decorator_name).
# 2. Manually by wrapping the function with the decorator.
# When we use the @decorator_name syntax, we call the decorated function directly,
# and the decorator logic is automatically applied.

# Calling the method
user = int(input("Enter the number: "))

# 1. Directly using the decorated function.
x = check_sign(user)  # Used when @decorator is applied
print(x)
'''
How its work :-
#------> To understand this read the concept of ⚔️⚔️Syntax(6)⚔️⚔️
# step1. Python (the interpreter) reads and stores all function definitions, but does not execute them until they are called.
# step2. When it encounters it first processes the @decorator_name above it — this means logging_example(check_sign) is executed.
#        The original check_sign function is replaced by the returned function (new_features)
# step3. After that, user input is taken and passed to the decorated function, which now includes the additional behavior defined in the decorator.
# step4. The decorated function is called (actually the wrapper).
# step5. Inside the wrapper, the original function is called.
# step6. The result is formatted and returned.
# step7. Output is printed.

How its work :- via digram
     Note :
     ->  At the @logging_example line, logging_example(check_sign) is called
     ->  At the def check_sign(arg): line, no call happens - only definition
     ->  So yes - both the function call and the override happen at the @logging_example line!
     ->  @logging_example  --> logging_example(check_sign) --> returns new_features --> new_features(arg)
            1. @logging_example
               ↓
            2. Python executes: logging_example(check_sign)
               ↓
            3. logging_example returns: new_features
               ↓
            4. So now: check_sign = new_features
               ↓
            5. When you call: check_sign(user)
               ↓
            6. You're actually calling: new_features(user)
               ↓
            7. Inside new_features:
                  var = value(user)  # value is the original check_sign
               ↓
            8. So the original check_sign(user) is executed

        @decorator_name replaces the original function with the wrapper.
        The wrapper still calls the original function inside it.
        That’s how the original logic (like checking positive/negative) still runs.
'''

# 2. Manually by wrapping the function with the decorator.
'''
obj = logging_example(check_sign)  # Used when @decorator is not applied
x = obj(user)
print(x)'''



Syntax(5):- DECORATOR USING @decorator_name
def logging_case(arg):
    '''class body try to display functional decorator'''
    def warpper(a, b):
        '''adding the new features'''
        x = arg(a, b)
        print(f"The addition of {a} and {b} is {x}")
    return warpper

@logging_case
def new_func(a, b):
    return a+b
# when interpreter encounter new_func() first time internally it read new function as a warpper()
new_func(20, 10)

# Explain : - How it's work
# Step1 : Interpreter reads the entire program but does not execute anything yet.
# step2 : When Python sees @logging_case, it looks at the function just below it — new_func.
#         Python first creates the new_func function and then gives it to logging_case.
#         So, logging_case gets the function itself (logging_case(new_func)), not the result of calling it.

# Step 3: Then Python immediately calls logging_case(new_func),
#         and passes the new_func function as an argument (not its result).

# Step 4: Inside logging_case, the warpper function is defined and returned.
#         So now, new_func is replaced by warpper — new_func now points to warpper.

# Step 5: Later, when new_func(20, 10) is called,
#         Python actually calls warpper(20, 10) because new_func refers to warpper.

# Step 6: Inside warpper, arg(20, 10) is called — this is the original new_func.
#         So the addition is performed and stored in variable x.

# Step 7: The result is printed on output screen is : "The addition of 20 and 10 is 30"

# step2 : - EXTRA IN HINDI
# Jab interpreter line 8 pe @logging_case dekhta hai, uske just neeche def new_func(a, b) likha hota hai.
# Python pehle new_func function ko define karta hai, fir uska reference logging_case ko pass karta hai.
# Yaani, logging_case(new_func) mein new_func ka function object pass hota hai — na ki uska execution.

⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️
⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️️⚔⚔⚔⚔⚔SYNTAX⚔⚔⚔⚔⚔⚔(6)⚔⚔⚔⚔⚔⚔CONCEPT️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️⚔️
⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️⚖️
#  CONCEPT TO UNDERSTAND THE FUNCTIONAL DECORATOR
# ———————————————————————————————————————————————————— SYNTAX(6)————————————————————————————————————————————————————————
'''
Syntax(6): -
⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔
# When Python encounters @example, it looks at the function just below it (func), and then gives it to example, which is
# equivalent to writing func = example(func)

def example():
    print("wizard")

@example    # here @example means @example(func), func is passed
def func(): # no parameter is given so error are generate.
    pass


def example(arg):
    print("wizard")

@example # now @example(func) pass the argument to arg so output is 'wizard'
def func():
    pass


def example(arg):
    def warpper():
        arg(),  # This calls the original func() function
        # print(arg)  # This would print the memory address of func
        # func() would give error because func is now warpper (circular reference)
    return warpper

@example  # This is equivalent to: func = example(func)
def func():
    print("Function is running")
func()  # Internally calls warpper(), which then calls arg() (the original func)

⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔⚔
'''
🍎
Class Decorators – (target entire classes)
A class decorator in Python is a function that modifies or enhances a class. It takes a class as input, adds functionality
(e.g., methods, attributes), or alters existing behavior, and returns the modified class.

A class decorator is a higher-order function that implements a specific metaprogramming pattern. It accepts a class
object (not an instance) as its input argument, performs transformations on that class (such as modifying, wrapping,
or registering it), and returns a new or the same mutated class object, which then replaces the original class definition.
There are three main ways to define class decorator
Function-Based Decorator
Class-Based Decorator
Parameterized Decorator

Syntax(7) : -
class MyDecorator:
    def __init__(self, func):
        self.func = func  # self.func store the reference of original greet function (means access the object of greet)

    def __call__(self, *args, **kwargs): #__call__() is a dunder method that is triggered when obj() is invoked.
        print("before function call")    # It is used to make the object behave like a function.
        result = self.func(*args, **kwargs)
        print("After function call")
        return result

@MyDecorator  # technically we create the object here greet = MyDirector(greet)
def greet(name): # so from (self <- memory reference is passed) and (func <- greet is passed)
    print(f"Hello, {name}")

greet("Aditya")

#Step1 : Class Definition Loaded
#      - The Python interpreter reads the MyDecorator class definition.
#      - It stores the class in memory but does not execute any methods yet.
#      - No object is created at this point.

#Step2 : Decorator Applied
#      - The @MyDecorator syntax is equivalent 'greet = MyDecorator(greet)'
#      - This means the original greet function is passed as an argument to the MyDecorator constructor.


#Step3 : Constructor (__init__) Invoked
#      - MyDecorator.__init__() is called with:
#      - self → reference to the new MyDecorator object
#      - func → reference to the original greet function
#      - Inside __init__, self.func = func stores the original function for later use

#Step4 : Function Definition Loaded
#      - The interpreter continues reading the greet function body:
#        def greet(name):
#            print(f"Hello, {name}")
#      - This function is now wrapped by the decorator and replaced by the MyDecorator object.

#Step5 : Function Call Triggers __call__()
#      - When greet("Aditya") is executed:
#      - greet is now an instance of MyDecorator
#      - So greet("Aditya") triggers the __call__() method of that instance


#Step6 : Inside __call__()
#      - print("before function call") is executed
#      - Then self.func(*args, **kwargs) calls the original greet function with "Aditya" as the argument
#      - Inside the original greet, print(f"Hello, {name}") outputs: Hello, Aditya

#Step7 : Final Output and Return
#      - print("After function call") is executed
#      - result is returned from __call__() (though nothing is printed since it's None)

#Output : -
         #--> before function call
         #--> Hello, Aditya
         #--> After function call


🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮

Function based decorator : -
- A regular function that takes a class as input and returns a modified class.
- Commonly used for adding attributes, wrapping methods, or injecting behavior.

def add_repr(cls):
    def __repr__(self):
        return f"{cls.__name__}({self.__dict__})"
    cls.__repr__ = __repr__
    return cls # to execute Person this we need to use cls()

@add_repr  # technically : - it is add_repr(Person)
class Person:
    def __init__(self, name):
        self.name = name
        print("Hello")


🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮

Class-Based Class Decorator
- A class with a __call__() method that takes a class and returns a modified version.
- Useful when we need to maintain state or configuration

class AddStr:
    def __call__(self, cls):
        def __str__(self):
            return f"{cls.__name__} instance"
        cls.__str__ = __str__
        return cls

@AddStr()  # technically : - it is AddStr(Product) --> cls() means Product()
class Product:
    pass

🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮🪮

Parameterized Class Decorator
- A decorator that takes arguments and returns a function or class that decorates the target class.
- Great for flexible, reusable logic

def tag(name):
    def decorator(cls):
        cls.tag = name
        return cls
    return decorator

@tag("DataModel")
class User:
    pass



🍎
# Method Decorators – target methods inside classes (e.g., @staticmethod, @property)

Method decorator is a special type of function decorator that is specifically designed to modify the behavior of a
method (defined inside a class) without changing its actual code. These decorators are commonly used for cross-cutting
concerns like logging, access control, memoization, and timing.

In built-in decorator we only use @classmethod, @property, @staticmethod. But in method decorator we have an extra
option to use custom decorator.

In simple way : - Difference b/w Built-in or Method decorator :
Method Decorator" is the general category. It includes ALL decorators that can be applied to methods, regardless of who created them.
"Built-in Decorator" is a specific type within that category. It refers only to the decorators provided by Python itself.

There are three primary ways to use method decorators:
Custom Method Decorators
   Created by developers to add custom behavior
   Example: @log_calls, @timer, @auth_required

Built-in Method Decorators # 💫💫💫💫 (Read in Built-in decorator)💫💫💫💫
   Provided by Python's standard library
   @staticmethod - Defines a method that doesn't receive self or cls
   @classmethod - Defines a method that receives the class (cls) as first argument
   @property - Allows methods to be accessed as attributes

Decorator Chaining  #💫💫💫💫 (Read as a last decorator)💫💫💫💫
   Multiple decorators applied to a single method
   Example: @staticmethod + @log_calls


Custom Method Decorator : -
Custom decorator is a user-defined function or class that modifies the behavior of instance methods
usually defined outside the class and applied inside the class—on instance methods using @decorator_name.

Custom decorators allow developers to add reusable logic—such as logging, validation, timing, or access
control—without changing the original method's code. these decorators are commonly written as
  - Functions (most common)
  - Classes (for more control, like maintaining state)
  - Inside another class (less common, but useful for encapsulation)

# Syntax(8) : - Custom method(Function based most common)
                # In function based decorator we Only function name with @ like : @function_name
def log_method_call(func_arg):
    def warpper(my_name):
        print(f"hello {my_name}")
        return func_arg(self="1", name="2")#--------------->>>> call new_func()
    print("wizard")
    return warpper("everyone")

class NewClass:
    @log_method_call # new_func = log_method_call(new_func)
    def new_func(self, name):
        print("hello")

obj = NewClass()
# obj.new_func("unknown") # new_function is technically call as warpper()-------------->
# def warpper(my_name):  # ❌ Missing 'self'
# return func_arg  # ❌ Should be func_arg(self, my_name)



#Syntax(9) : - Custom method(Function based example most common)
def log_method_call(func):
    '''Decorator that logs method calls with timing'''

    def wrapper(self, *args, **kwargs):
        print(f"Calling method: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(self, *args, **kwargs)
        print(f"Method {func.__name__} completed")
        return result
    return wrapper

def validate_age(func):
    '''Decorator that validates age parameter'''
    def wrapper(self, age, *args, **kwargs):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a positive integer")
        # return func(self, age, *args, **kwargs) # if we hide this line then set_age is not excute
    return wrapper

class Person:
    @log_method_call
    def greet(self, name):
        print(f"Hello, {name}!")

    @validate_age
    def set_age(self, age):
        self.age = age
        print(f"Age set to: {age}")

# Usage
person = Person()
person.greet("Alice")
person.set_age(25)


#Syntax(9) : - Custom method(Class based example most common)
                # class-based decorator, we use only the class name with @ like : @ClassName
class DecoratorClass:
    def __init__(self, func):
        self.var1 = func()
        # self.var1 = func("hello")

    def __call__(self, *args, **kwargs):
        for i in range(10):
            for j in range(10):
                print("*", end=" ")
            print()
        # return self.var1(self) # the memory reference

class MyClass:
    @DecoratorClass
    def new_function(self):
        print("Hello this is new pattern : - ")
obj = MyClass()    #@DecoratorClass = new_function = DecoratorClass(new_function)
obj.new_function() # it trigger the ___call__



#Syntax(10) : - Custom method(Class based example most common)
              # Custom class inside decorators used only inside the decorator
class Decorators:
    # Decorator defined inside a class
    @staticmethod
    def log_calls(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper

# Using the class-based decorator
class Calculator:
    @Decorators.log_calls  # add = Decorators.log_calls(add) --> add = wrapper
    def add(self, a, b):   # add(self, a, b) --> means wrapper(self, a, b) because add store the wrapper
        return a + b

    @Decorators.log_calls  # multiplay = Decorators.log_calls(multiply)
    def multiply(self, a, b):
        return a * b

# Test
calc = Calculator()
calc.add(5, 3) # wrapper(self, a, b)
calc.multiply(4, 6)



🍎
Built-in Decorators – Provided by Python itself (e.g., @staticmethod, @classmethod, @property).
Built-in Decorator is a special type of method decorator that is pre-defined by the Python language itself to modify the
behavior of a method in a specific, standardized way. These decorators provide fundamental object-oriented programming
features, such as defining static methods, class methods, and properties, without changing the method's actual code.

In simple way, while the general category of "Method Decorator" includes both custom and pre-defined tools,
"Built-in Decorator" refers exclusively to the official tools provided in Python's standard toolbox
There are three primary built-in decorators provided by Python @staticmethod, @classmethod, @property
   - @staticmethod - Defines a method that doesn't receive self or cls
   - @classmethod - Defines a method that receives the class (cls) as first argument
   - @property - Allows methods to be accessed as attributes

Difference b/w :- (Method and built-in decorator)
- Built-in decorators are a specific subset of method decorators that are provided by Python and have special language-level
  support. Method decorators is the broader category that includes both built-in and custom decorators.


#Syntax(11) : (@Staticmethod) :
class MyClass:
    '''class body is return the addition of a and b'''
    def __init__(self):
        pass

    @staticmethod           # __call__ = staticmethod(__call__)
    def __call__(a, b):    # __call__ now stores the static method wrapper
        return a+b

obj = MyClass()
value = obj(2, 3) # trigger the __call__ and return addition
# @staticmethod removes the automatic passing of the instance reference (for instance methods)
# or class reference (for class methods)
# It makes the method behave like a regular function that happens to be inside a class namespace
print(value)


print(MyClass().__call__(4,5))
print(MyClass.__call__(4,5))
# @staticmethod prevents the automatic passing of the instance/class reference, allowing your __call__
# method to work with just two parameters in all calling scenarios


#Syntax(11) : (@Staticmethod) :
class ClassNmae:
    def __init__(self, myname):
        self.name = myname

    @staticmethod
    def aboutme(age): # no need to use cls or self as a argument
        store = ClassNmae("wizard").name # access the attribute value from constructor
        return f"My name is {store} and age is {age}"

x = ClassNmae # correct way
print(x.aboutme(20))
print(ClassNmae.aboutme(30)) # correct way




#Syntax(12) : @classmethod :
# Let's check the class variables
class NewClass:
    '''class body is try to display addition'''
    def __init__(self):
        pass

    @classmethod
    def addition(cls, a, b):
        '''try to display the addition of a and b'''
        cls.var1st = a  # Sets CLASS variable var1st
        cls.var2nd = b  # Sets CLASS variable var2nd
        return f"The addition of ({cls.var1st}+{cls.var2nd}) is : {a+b}"

obj = NewClass()
x = obj.addition(10, 20)   # Access via instance
y = NewClass.addition(40, 40)  # Access via class
print(x, y, sep='\n')

# Let's check the class variables
# The attributes ARE accessible via both instance and class
print(f"Class variables: var1st = {NewClass.var1st}, var2nd = {NewClass.var2nd}") # accessible
print(f"Class variables: var1st = {obj.var1st}, var2nd = {obj.var2nd}") # accessible

# Explanation : -
# 🫴 Is it @classmethod decorator accessible using instance and class ?
#Ⓜ️ Yes, it's valid to access a @classmethod using both ClassName.method() and instance.method().
#Ⓜ️ Python internally binds the class (cls) to the method regardless of how it's called. Even if you use an instance,
#Ⓜ️ Python still passes the class as the first argument—not the instance. So obj.func() is just syntactic sugar for X.func().

#Ⓜ️ हाँ, आप @classmethod को दोनों तरीकों से कॉल कर सकते हैं — ClassName.method() और instance.method().
#Ⓜ️ Python अंदर ही अंदर class (cls) को method से bind कर देता है, चाहे आप उसे instance से कॉल करें या class से। जब आप obj.func()
#Ⓜ️ लिखते हैं, तब भी Python class को ही पहला argument के रूप में भेजता है — instance नहीं। यानी obj.func() सिर्फ X.func() का shortcut है

Syntax(13) : - @classmethod
class X:

    @classmethod
    def func(self):
        print("hello")

obj = X()
obj.func()
X().func()
X.func()

class X:
    def func(cls):  # Missing @classmethod
        print("hello")
X().func()  # ❌ TypeError: func() takes 1 positional argument but 2 were given




🍎
* The @property decorator in Python is a built-in feature that turns a method into a read-only attribute, making it
  a powerful tool for encapsulation.

* It allows a programmer to define getters, setters, and deleters for a class's attributes. This provides a clean interface
  for accessing data while controlling how that data is accessed and modified.

Syntax(14) : - Concept VVI (@property)
class Dog:
    def __init__(self, name):
        self._name = name

    @property
    def wark(self):
        '''This method now acts like a read-only attribute.'''
        return f"Wark, wark! My name is {self._name}!"

    def func(self):
        self.var1 = "Wizard"


# Create an instance of the Dog class
my_dog = Dog("Fido")

# Access 'wark' as an attribute, without parentheses
print(my_dog.wark)

# We cannot write (change) the value
try:
    my_dog.wark = "Woof!"
except AttributeError as e:
    print(e)  # This line will print an error message

# We can write(change) the attribute of regular attribute
my_dog.var1 = "Hello" # now the value is change from Wizard to Hello
                      # But in @property we can't change attribute value of wark
#we are checking wark is a attribute or not

# The wark attribute itself doesn't store anything. Because it's a read-only property, you can't tell
# it to store a different value directly. Its entire purpose is to be a function that gives you a computed
# value, not a container for a value.
print(type(my_dog.wark)) #output : <class 'str'> ---> if returned value is 10 then int is display
print(type(my_dog.func)) #output : <class 'method'>

# Explain : - Difference B/W wark and _name attribute : ----
# wark is a kind of attribute, but it's not a normal storage container.
# Instead, it's a special type of attribute that computes a value on the fly

# _name is a variable. It has a specific spot in the computer's memory to store a single value (e.g., "Fido").
#  we can change this value directly.

# wark is a method disguised as a variable. It has no place in memory to store a value. Its purpose is to run a small
# program (the code inside the wark method) and give you the result. The result it gives you might be based on other
# stored variables, like _name.




# Syntax(15) : - (@property)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.diameter)  # Output: 10



# Syntax(16) : (@property)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

c = Circle(5)
print(c.radius)  # Output: 5

c.radius = 10
print(c.radius)  # Output: 10

# c.radius = -1  # This will raise a ValueError



#Syntax(17) : - (@property)
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price  # stored as raw value

    @property
    def price(self):
        # Add logic: return price with tax
        return round(self._price * 1.18, 2)  # assuming 18% GST

    @property
    def name(self):
        return self._name.title()  # auto-format name

# Usage
# Wrap this method using the property() function so it behaves like an attribute.”
item = Product("herbal shampoo", 250)
print(item.name)   # Herbal Shampoo
print(item.price)  # 295.0


# Syntax(18) : - (@property)
# class rewritten without decorators, using property() directly
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return round(self._price * 1.18, 2)

    def get_name(self):
        return self._name.title()

    price = property(get_price)
    name = property(get_name)

🍎
# Class-Based Decorators – Implemented using classes with __call__.

Syntax(19) : Class based decorator
class MyDecorator:
    def __init__(self, func):
        # Store the decorated function
        self.func = func

    def __call__(self, *args, **kwargs):
        # This is the "wrapper" logic that runs before the original function
        print("Something is happening before the function is called.")

        # Call the original function with its arguments
        result = self.func(*args, **kwargs)

        # This is the "wrapper" logic that runs after the original function
        print("Something is happening after the function is called.")

        # Return the result of the original function
        return result

@MyDecorator
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Greetings, {name}!"

# Call the decorated function
output = say_hello("Alice")

print(f"The return value is: {output}")




Syntax(20) : Class based decorator
import time
class Timer:
    def __init__(self, func):
        # The function to be timed
        self.func = func

    def __call__(self, *args, **kwargs):
        # Start the timer
        start_time = time.time()

        # Call the original function
        result = self.func(*args, **kwargs)

        # Stop the timer and calculate the duration
        end_time = time.time()
        duration = end_time - start_time

        print(f"Function '{self.func.__name__}' took {duration:.4f} seconds to run.")

        # Return the result of the function
        return result

@Timer
def complex_calculation(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Call the decorated function
result = complex_calculation(10000000)
print(f"Result of the calculation: {result}")

🍎
# Chained Decorators – (Multiple decorators applied to a single function or method)
# A chained decorator is a Python programming concept where multiple decorators are applied to a single function or class.
# This is also known as "stacking decorators." The decorators are executed in a specific order: from the bottom up, with
# the decorator closest to the function definition being executed first, and the one farthest away being executed last.

# Decorator Chaining  #💫💫💫💫 (last decorator type)💫💫💫💫
#    Multiple decorators applied to a single method
#    Example: @staticmethod + @log_calls + @classmethod + @property


Syntax(21) :- Chain decorator
def log_it(func):
    def wrapper(*args, **kwargs):
        print("Starting function call...")
        result = func(*args, **kwargs)
        print("...Function call finished.")
        return result
    return wrapper

def add_prefix(func):
    def wrapper(*args, **kwargs):
        return "Hello, " + str(func(*args, **kwargs))
    return wrapper

@log_it
@add_prefix
def get_name(name):
    return name

print(get_name("Alice"))



Syntax(22) : -  Chain decorator
def log_call(func):
    '''A decorator to log function calls.'''

    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished.")
        return result

    return wrapper

class Calculator:

    @staticmethod
    @log_call
    def add(x, y):
        '''A static method to add two numbers.'''
        return x + y

    @classmethod
    @log_call
    def multiply_by_factor(cls, x, factor):
        '''A class method to multiply by a class-specific factor.'''
        return x * factor


# Usage
print("--- Calling static method ---")
result_add = Calculator.add(5, 3)
print(f"Result: {result_add}\n")

print("--- Calling class method ---")
result_multiply = Calculator.multiply_by_factor(10, 2)
print(f"Result: {result_multiply}")



"""



