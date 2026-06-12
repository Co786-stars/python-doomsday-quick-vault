# WAPP  to find the ASCII value of all cheacter
value = input("Enter the value : ")
if len(value) == 1:
    print(f"The Ascii value of {value} is {ord(value)}")
else:
    print("pls enter single chracter")