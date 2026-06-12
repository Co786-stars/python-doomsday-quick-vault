# Definition :-
# .split() is a string method used to break a string into parts (substrings).
# It returns a list of words or pieces.

# Syntax :-
# string.split(separator, maxsplit)

# Parameters :-
# - separator → character(s) where the split happens (default is whitespace).
# - maxsplit → optional, number of splits to do (default is all).

# Important Note :-
# - Works only on strings.
# - Result is always a list.
# - Default split is by spaces if no separator is given.

# Note:
# if we try to split numeric/integer then it got an error.



# split by space:
text = "Python is powerful"
print(text.split())
'''
Explanation:
- No separator given → default is whitespace.
- String is cut at spaces.
- Result is a list of words.
'''

# split by comma
data = "apple,banana,cherry"
print(data.split(","))
'''
Explanation:
- Separator is explicitly ",".
- String is cut wherever a comma appears.
- Result is a list of items separated by commas.
'''

# limit splits by max split:
line = "one two three four"
print(line.split(" ", 2))
'''
Explanation:
- Separator is space " ".
- maxsplit = 2 → only 2 splits allowed.
- First split → 'one' and the rest.
- Second split → 'two' and the rest.
- After 2 splits, stop → remaining part stays together as 'three four'.
'''




# Definition :-
# max() is a built-in Python function used to determine the largest element.
# It can compare numbers, strings, or items within an iterable (list, tuple, set).

# Syntax :-
# max(arg1, arg2, ..., argN)
# max(iterable, key=function, default=value)

# Parameters :-
# - arg1, arg2, ..., argN → multiple values to compare directly.
# - iterable → a sequence of elements (list, tuple, set, string).
# - key → optional function to customize comparison (e.g., length of word).
# - default → optional value returned if iterable is empty.

# Important Notes :-
# - Elements must be comparable (all numbers, or all strings).
# - Raises ValueError if iterable is empty and no default is provided.
# - String comparison is lexicographic (alphabetical order).
# - The result is always the maximum element according to comparison rules.


# Example 1: Numbers
print(max(12, 45, 7))
'''
Explanation:
- Compares 12, 45, and 7.
- Largest value is 45.
- Result: 45
'''


# Example 2: Iterable (list)
values = [3, 18, 9, 27]
print(max(values))
'''
Explanation:
- Compares all elements in the list.
- Largest value is 27.
- Result: 27
'''


# Example 3: Strings
words = ["natural", "disaster", "grievance"]
print(max(words))
'''
Explanation:
- Compares strings alphabetically.
- "natural" comes last in lexicographic order.
- Result: "natural"
'''


# Example 4: Using key function
print(max(words, key=len))
'''
Explanation:
- key=len → comparison based on word length.
- "grievance" is longest (9 characters).
- Result: "grievance"
'''


# Example 5: Tuples with key
# records = [(1, 5), (3, 2), (2, 9)]
records = [[1, 5], [3, 2], [2, 9]]
print(max(records, key=lambda x: x[1]))
'''
Explanation:
- key=lambda x: x[1] → compare by second element of tuple.
- (2, 9) has largest second value (9).
- Result: (2, 9)
'''