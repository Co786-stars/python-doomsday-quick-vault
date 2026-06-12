# Write a program to generate the Random Number ?
# ______________________________________________________________________________#

import random
x = random.randint(1, 10) # .randint() generate the random int number b/w given range
print(x)


# ______________________________________________________________________________#

def temporynumber():
    """function is use to choose random number"""
    y = random.random() # .random() generate the random float number b/w 0 and 1
    print(f"Random Number between 0 and 1") # generate random number between 0 and 1
temporynumber() # function call


# ______________________________________________________________________________#

class RandomNumbers:
    """class body interface with random function"""
    def random_num():
        num1 = random.randrange(1, 10) # random int from 1 to 10(exclisive)
        num2 = random.randint(1, 10) # random int from 1 to 10(inclusive)
        print(num1)
    
    def list_num():
        l1 = [1, 2, 3, 4, 5, 6] 
        num1 = random.sample(l1, 3) # simply choose any 3 item from list
        num2 = random.shuffle(l1)  # None is show
        num3 = random.choice(l1) # choose single random element from list l1
        print(num1, num2, num3)

rand = RandomNumbers
rand.random_num()
rand.list_num()

#_____________________________________________________________________________________#
