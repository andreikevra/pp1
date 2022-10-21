import random

print("Dice Game: try to roll a bigger number than the computer! Good luck!")

print("Try to guess the dice number from 1 to 6")
pcNumber = random.randint(1,6)


guess_Number = int(input())
print(pcNumber)

if guess_Number == pcNumber:
    print("True")

