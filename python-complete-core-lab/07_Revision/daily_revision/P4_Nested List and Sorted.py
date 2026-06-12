x = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
print(sorted(x)) # sorted as per name


# If we want to sort by the second element, we need to tell Python explicitly using the key parameter:
print(sorted(x, key=lambda s: s[1]))  # sorted according to the second value (score)
# Meaning of sorted(x, key=lambda s: s[1]):
# - sorted() creates a new list that is sorted.
# - The key parameter tells Python what to use for sorting.
# - lambda s: s[1] means: for each sublist 's', take the second element (index 1 → score).
# - Therefore, the list is sorted in ascending order based on students' scores.
# - If two scores are the same, Python falls back to default lexicographic (alphabetical) comparison of names.



print(sorted(x, key= lambda p: (p[1], p[0])))   # sorted by score, then name
# Meaning of sorted(x, key=lambda p: (p[1], p[0])):
# - sorted() creates a new sorted list.
# - The key parameter tells Python what values to use for sorting.
# - lambda p: (p[1], p[0]) means: for each sublist 'p',
#     → first take the second element (index 1 → score),
#     → then take the first element (index 0 → name).
# - So the list is sorted primarily by score (ascending).
# - If two students have the same score, their names are compared alphabetically.
# - This ensures ties are broken in alphabetical order.




y = [i[1] for i in x] # we are extract the second element of list
z = sorted(set(y)) # now removing the duplicate
print(y, z, sep="_________")
# By default, sorted() always arranges values in ascending order (smallest → largest).


