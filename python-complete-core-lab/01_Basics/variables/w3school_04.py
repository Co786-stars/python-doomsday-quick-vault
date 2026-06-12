def full_pyramid(value):
    """ fun body use to print the pattern of numaric full pyramid """
    i = 1
    while i < value+1:
        print(" "*(value-i), end="")
        for j in range(1, 2*i):
            print(j, end="")
        print()
        i +=1 
value = 5 
full_pyramid(value) 

# >> i = 1  2  3  4  5
#----1
#---123
#--123456
#--1234567
#-123456789

