# Wap to display all the prime number  ? (number which have exectly two factor 1 and itself)

class Numbers:
    """class body use to manuplate numbers"""
    def __init__(self, num): # self is contain memory reference or num is contain argument
        self.number = num # __init__ constructor is use to initilize variable(attribute)

    def primenumber(self): # self is use to pass value 
        i = 2
        while i <= self.number:
            if i%2 == 1 or i//2 == 1: # logic is use to display the number is prime or not 
                print(i, end = " ")
            i += 1
    
    @classmethod 
    def random(cls): # cls contain memory referance
        import random 
        lst = ["laptop", "mobilephone", "telephone", "router"]
        tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        x = random.randint(10, 20) # radiant take two argument
        y = random.choice(lst) # use to choose random number from datatype
        print(x, y)
    

# prime = Numbers(10)
# prime.primenumber()


