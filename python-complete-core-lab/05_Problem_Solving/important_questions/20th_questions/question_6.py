''' Question 1
Write a Python function to find the second largest number in a list without using sorting.
Handle cases where:
list has less than 2 elements
all elements are equal'''

class Number:
    """try to display the 2nd largest number in list"""
    def __init__(self, n1):
        self.count_num = n1
        self.num = []
        for i in range(1, self.count_num+1):
            user_value = int(input("Enter integer : "))
            self.num.append(user_value) # add the number in list

    def largest2ndNumber(self):
        """try to display 2nd largest number in lst"""
        self.num.sort()
        if self.count_num > 1:
            return f"Arrangement of lst : {self.num} \nsecond largest number : {self.num[-2]}"
        else:
            return f"pls enter number more then two to compare."

    def max2ndNumber(self):
        """try to display using logical way Next time"""

try:
    n1 = int(input("Enter the count number : "))
    obj = Number(n1)
    second_max = obj.largestNumber()
    print(second_max)
except ValueError:
    print("pls enter correct value")


# for permanently changes
x = [1, 2, 10, 5]
x.sort(reverse=x)
print(x[1])


# for temporary changes
x = [1,3,5, 8, 9,2]
y  = sorted(x)
print(y[-2])

