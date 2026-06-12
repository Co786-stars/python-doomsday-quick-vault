'''
if __name__ == '__main__':
    students = []  # Step 1: Empty list to store [name, score]

    # Step 2: Input student data
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Step 3: Extract scores, remove duplicates, sort
    scores = sorted(set([s[1] for s in students]))

    # Step 4: Find second lowest score
    second_lowest = scores[1]

    # Step 5: Collect names with second lowest score
    result = [s[0] for s in students if s[1] == second_lowest]

    # Step 6: Sort names alphabetically and print
    for name in sorted(result):
        print(name)
'''



# Task/Question
# Given the names and grades for each student in a class of N students, store them in a nested list and print the
# name(s) of any student(s) having the second lowest grade.

# Note:
# If there are multiple students with the second lowest grade, order their names
# alphabetically and print each name on a new line.

# Example:
# record = [["chi",20.0], ["beta", 50.0], ["alpha", 50.0]]

# The ordered list of scores is [20.0, 50.0], so the second lowest score is [50.0]. There are two students with that
# score: ["beta", "alpha"] Ordered alphabetically, the names are printed as:
# alpha
# beta


# Input Format
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order
# their names alphabetically and print each one on a new line.

# Constraints
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Input 0
# Berry
# Harry

# Explanation 0
# There are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.21 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and
# Berry, so we order their names alphabetically and print each name on a new line.



# Program 1: Find students with the second lowest score (static list)
# Program  : Using a Predefined Lis
if __name__ == '__main__':
    # Predefined list of students with scores
    lst = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

    # Step 1: Extract scores, remove duplicates, sort ascending
    sorted_scores = sorted(set(score for _, score in lst))

    # Step 2: Identify the second lowest score
    second_lowest_score = sorted_scores[1]

    # Step 3: Collect names of students with that score
    second_lowest_students = [name for name, score in lst if score == second_lowest_score]

    # Step 4: Print names alphabetically
    for student in sorted(second_lowest_students):
        print(student)




# Program 2: Find students with the second lowest score (user input)
# Program  : Taking Input from Use
if __name__ == '__main__':
    lst = []
    total_students = int(input("Enter the total number of students: "))

    # Step 1: Collect student names and scores
    for _ in range(total_students):
        name = input("Enter the Name: ")
        score = float(input(f"Enter the score of {name}: "))
        lst.append([name, score])

    # Step 2: Extract scores, remove duplicates, sort ascending
    sorted_scores = sorted(set(score for _, score in lst))

    # Step 3: Identify the second lowest score
    second_lowest_score = sorted_scores[1]

    # Step 4: Collect names of students with that score
    second_lowest_students = [name for name, score in lst if score == second_lowest_score]

    # Step 5: Print names alphabetically with message
    for student in sorted(second_lowest_students):
        print(f"{student} has the second lowest score")






# Extra revise 
class TreeChain:
    """class body is display name"""
    def __init__(self, s):
        """constructor initialize the attribute"""
        self.total_s = s

    def student_data(self):
        """methods display the data"""
        self.lst = []
        for i in range(self.total_s):
            """store the data using loop"""
            self.s_name = input("Name   : ")
            self.s_score = int(input("Score : "))
            self.single_data = [self.s_name, self.s_score]
            self.lst.append(self.single_data)
        print(self.lst) # display the data in lst

        self.student_grade = [score for _, score in self.lst ]
        print(self.student_grade)   # store the grade

        self.no_duplicate = set(self.student_grade)
        print(self.no_duplicate) # remove the duplicate

        self.sort_a_to_d = sorted(self.no_duplicate)
        print(self.sort_a_to_d) # value are sorted in asc order low to high we
                                # want second highest
        self.second_highest =  [name for name, score in self.lst if score == self.sort_a_to_d[1]]
        print(self.second_highest)  #display th second_highest data

        for i in sorted(self.second_highest):
            print(i)


obj = TreeChain(3)
obj.student_data()



