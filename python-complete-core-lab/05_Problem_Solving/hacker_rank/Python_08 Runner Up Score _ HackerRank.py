'''
if __name__ == '__main__':
    # n = int(input())  # number of scores
    arr = list(map(int, input().split()))  # convert input to a list of integers

    # Remove duplicates by converting to a set
    unique_scores = set(arr)

    # Find the highest score
    max_score = max(unique_scores)

    # Remove the highest score
    unique_scores.remove(max_score)

    # Runner-up is now the maximum of the remaining scores
    runner_up = max(unique_scores)

    print(runner_up)

'''
# Task/Question
# Given the participants' Scoresheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up(means second highest number).

# Input Format
# The first line contains n . The second line contains an array A[] of n  integers each separated by a space.

# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100

# Output Format
# Print the runner-up score

# Sample Input
# 5
# 2 3 6 6 5

# Sample Output
# 5

# Explanation
# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5.
# Hence, we print 5 as the runner-up score.

class Score:
    """
    Class to calculate and display the runner-up score
    from a given list of participant scores.
    """
    def __init__(self, scores):
        self.scores = scores

    def runner_up_score(self):
        numeric_scores = list(map(int, self.scores))
        unique_scores = set(numeric_scores)
        if len(unique_scores) < 2:
            return "Runner-up score does not exist"
        highest_score = max(unique_scores)
        unique_scores.remove(highest_score)
        runner_up = max(unique_scores)
        return str(runner_up)


if __name__ == "__main__":
    try:
        n = int(input().strip())
        scores_input = input().split()
        score_obj = Score(scores_input)
        result = score_obj.runner_up_score()
        print(result)
    except ValueError:
        print("Please enter valid integer values for scores.")
'''
Explanation:

The program defines a class `Score` which is responsible for calculating the runner-up score.
- Runner-up means the second highest score in the list.

Inside the class:
- The constructor `__init__` stores the scores provided by the user.
- The method `runner_up_score` converts the scores into integers, removes duplicates using a set,
  and checks if there are at least two unique scores.
- It finds the highest score, removes it, and then finds the maximum of the remaining scores,
  which is the runner-up.

In the main block:
- The program first reads the number of scores (n).
- Then it reads the scores themselves as space-separated values.
- A `Score` object is created with these scores.
- The `runner_up_score` method is called to compute the runner-up.
- The result is printed.

Error handling:
   - If the user enters invalid values (non-integers), the program catches the `ValueError`
     and prints a friendly message.

Example:
   Input:
   5
   2 3 6 6 5

   Output: 5
   
Note:
Explanation: The highest score is 6, the second highest (runner-up) is 5. 
'''


