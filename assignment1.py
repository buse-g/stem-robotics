import random

n = random.randint(1,10)

for i in range(3):
    answer = input("guess the number i'm thinking of (1-10)\n")
    if answer == n:
        print("you won!")
        break
    else:
        continue
print("you lost!")
