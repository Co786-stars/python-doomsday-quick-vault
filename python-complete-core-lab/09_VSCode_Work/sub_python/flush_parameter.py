import time
for i in range(3):
    print(i , end=" ", flush=False)
    time.sleep(2)
print("over")
for i in range(3):
    print(i , end=" ", flush=True)
    time.sleep(2)
print("over")
