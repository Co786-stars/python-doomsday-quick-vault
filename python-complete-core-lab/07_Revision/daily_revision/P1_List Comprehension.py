s = [i*i for i in range(3)]  # # list comprehension
print(s) # square of a number

# - Interpreter reads the statement
#   Python sees that you are creating a list using list comprehension. The structure is:
#   [expression for variable in iterable]

# - Range is prepared
#   range(3) generates the sequence of numbers: 0, 1, 2. (Remember: range(n) goes from 0 up to n-1.)


# - Iteration begins
# - The for i in range(3) part tells Python: “Take each value from the range one by one and assign it to i.”
# - So first i = 0, then i = 1, then i = 2

#   Note : -
    # When we write a list comprehension like:
    # s = [i*i for i in range(3)]
    # The Python interpreter automatically creates a new empty list in memory before starting the loop.
    # This list doesn’t have a “default variable name” that we can access — it’s just an internal object being built.
    # Once the comprehension finishes, that hidden list is assigned to our variable s.

    # Example : -
    # Behind the scenes (conceptual)
    # _temp_list = []          # hidden list created internally
    # for i in range(3):       # i = 0, then 1, then 2
    #     _temp_list.append(i*i)   # add result each time
    # s = _temp_list           # finally assign to s


# - Expression is evaluated for each i
# - When i = 0, Python calculates i*i → 0*0 = 0.
# - When i = 1, Python calculates i*i → 1*1 = 1.
# - When i = 2, Python calculates i*i → 2*2 = 4.


# - Values are collected into a list automatically
#   Unlike using .append() manually, list comprehension automatically builds the list as the loop runs.
# - After first iteration: [0]
# - After second iteration: [0, 1]
# - After third iteration: [0, 1, 4]


# - Final assignment
#   The completed list [0, 1, 4] is stored in variable s.


# - Printing the result
#   print(s) outputs: [0, 1, 4]


# Key Clarification
# - The interpreter does not try to evaluate i*i before i has a value.
# - The order is: loop assigns i → then expression i*i is calculated → result is added to the list.
# - That’s why there’s no “None” issue — i always has a value when the expression runs.




s = [i for i in range(3) if i%2==0]  # list comprehension with condition
print(s)  # even numbers

# - Interpreter reads the statement
#   Structure: [expression for variable in iterable if condition]

# - Range is prepared
#   range(3) generates: 0, 1, 2

# - Iteration begins
#   i takes values one by one → 0, then 1, then 2


# - Condition check (if i%2==0)
#   Only include i when it is divisible by 2 (i.e., even)

    #   Note : -
    #   When we write a list comprehension with a condition like:
    #   s = [i for i in range(3) if i%2==0]
    #   The Python interpreter automatically creates a new empty list in memory before starting the loop.
    #   This list doesn’t have a “default variable name” that we can access — it’s just an internal object being built.
    #   Once the comprehension finishes, that hidden list is assigned to our variable s.

    #   Example : -
    #   Behind the scenes (conceptual)
    #   _temp_list = []              # hidden list created internally
    #   for i in range(3):           # i = 0, then 1, then 2
    #       if i % 2 == 0:           # condition check → only even numbers
    #           _temp_list.append(i) # add result each time if condition is True
    #   s = _temp_list               # finally assign to s

# - Expression is evaluated
#   i = 0 → 0%2==0 → True → add 0
#   i = 1 → 1%2==0 → False → skip
#   i = 2 → 2%2==0 → True → add 2

# - Values collected into list automatically
#   After iteration → [0, 2]

# - Final assignment
#   s = [0, 2]

# - Printing the result
#   print(s) outputs: [0, 2]

# - Notice the difference:-
#   Here the if condition filters values before they are added to the list.




s = [(i, j) for i in range(3)
             for j in range(3)]
print(s)   # all pairs (i, j)

# - Interpreter reads the statement
#   Python sees that you are creating a list using list comprehension with two loops.
#   The structure is: [expression for variable1 in iterable1 for variable2 in iterable2]

# - Range is prepared
#   range(3) generates the sequence: 0, 1, 2

# - Iteration begins
#   Outer loop: i = 0, then 1, then 2
#   Inner loop: for each i, j = 0, then 1, then 2

    #   Note : -
    #   When we write a nested list comprehension like:
    #   s = [(i, j) for i in range(3) for j in range(3)]
    #   The Python interpreter automatically creates a new empty list in memory before starting the loops.
    #   This hidden list is filled step by step with tuple values (i, j).
    #   Once the comprehension finishes, that hidden list is assigned to our variable s.

    #   Example : -
    #   Behind the scenes (conceptual)
    #   _temp_list = []                     # hidden list created internally
    #   for i in range(3):                  # outer loop → i = 0, 1, 2
    #       for j in range(3):              # inner loop → j = 0, 1, 2
    #           _temp_list.append((i, j))   # add tuple (i, j) each time
    #   s = _temp_list                      # finally assign to s

# - Expression is evaluated for each pair (i, j)
#   i = 0 → j = 0 → (0,0), j = 1 → (0,1), j = 2 → (0,2)
#   i = 1 → j = 0 → (1,0), j = 1 → (1,1), j = 2 → (1,2)
#   i = 2 → j = 0 → (2,0), j = 1 → (2,1), j = 2 → (2,2)

# - Values are collected into a list automatically
#   After all iterations: [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# - Final assignment
#   The completed list is stored in variable s.

# - Printing the result
#   print(s) outputs: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]




# Loop Examples:-
# Without condition
s = [(i, j) for i in range(3)
             for j in range(3)]
print(s) # Output: [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]


# With condition on inner loop
s = [(i, j) for i in range(3)
             for j in range(3) if j % 2 == 0]
print(s) # Output: [(0,0), (0,2), (1,0), (1,2), (2,0), (2,2)]


# With condition on outer loop
s = [(i, j) for i in range(3) if i % 2 == 0
             for j in range(3)]
print(s) # Output: [(0,0), (0,1), (0,2), (2,0), (2,1), (2,2)]


""" 
------------------- List Comprehension Quick Notes -------------------

Definition:
    A concise way to create lists in Python using a single line of code.
    It combines loop + condition + append into one expression.

Syntax :
    # Basic list comprehension
        [expression for variable in iterable]
    
    # With condition (filtering values)
        [expression for variable in iterable if condition]
    
    # Nested loops (outer + inner)
        [expression for outer_var in outer_iterable
                     for inner_var in inner_iterable]
    
    # Nested loops with conditions
        [expression for outer_var in outer_iterable if <condition_on_outer>
                     for inner_var in inner_iterable if <condition_on_inner>]

Parts:
    - expression → what to store in the list
    - for item in iterable → loop over values
    - if condition → optional filter (can be skipped)

Examples:
    1. Squares of numbers
       squares = [i*i for i in range(5)]
       Output: [0, 1, 4, 9, 16]

    2. Even numbers only
       evens = [i for i in range(10) if i % 2 == 0]
       Output: [0, 2, 4, 6, 8]

    3. Nested loops
       pairs = [(i, j) for i in range(2) for j in range(2)]
       Output: [(0,0), (0,1), (1,0), (1,1)]

Key Idea:
    Think of it as:
        Loop → Filter → Result
    All in one line.


List Comprehension:
    - Works only with 'for' loops over iterables (like range, list, set).
    - Cannot use 'while' directly inside list comprehension.

Tip:
    - Use for simple logic (readability).
    - Avoid very complex nesting (can be confusing).
    - Always compare with normal loops if unsure.
    - Use list comprehension for fixed ranges or sequences.
    - Use while loops when the stopping condition is dynamic.

----------------------------------------------------------------------
"""