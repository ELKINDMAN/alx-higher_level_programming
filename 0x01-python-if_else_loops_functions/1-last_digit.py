#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldig = abs(number) % 10
if number < 0:
    ldig = -ldig

if ldig > 5:
    print(f"Last digit of {number} is {ldig} and is greater than 5")
elif ldig == 0:
    print(f"Last digit of {number} is {ldig} and is 0")
else:
    print(f"Last digit of {number} is {ldig} and is less than 6 and not 0")
