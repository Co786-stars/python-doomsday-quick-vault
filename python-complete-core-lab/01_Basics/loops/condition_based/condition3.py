user_name = ["usr1", "usr2", "usr_admin", "usr4", "usr5", "usr6"]
if user_name == "usr_admin":
    print("hello admin would you like to see a status report")
else:
    print(f"hello {user_name} thank you for login again")

# 5.10  finish
current_users = ["Rahul", "Aniket", "Sahil", "Mohan", "Ankit"]
new_users = ["Rohan", "Ramesh", "sahil", "Mohan", "Suman"]
for users in current_users:
    if users in new_users:
        print(f"my name is {users}")
    else:
        print(f"user {users} is avliable")
    

# 5.11 finish

ordinal = [num1 for num1 in range(1, 10)]
print(ordinal)
for ordinal_num in ordinal:
    if ordinal_num == 1:
        print( end=" " f"{ordinal_num}st")
    elif ordinal_num == 2:
        print( end=" " f"{ordinal_num}nd")
    elif ordinal_num == 3:
        print( end=" " f"{ordinal_num}rd")
    else:
        print(f"{ordinal_num}th")

