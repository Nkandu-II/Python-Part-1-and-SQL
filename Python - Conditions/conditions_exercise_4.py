# Exercise Conditions - 4

import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)

x = abs(number1)
y = abs(number2)

if x > y :
    print(f"{x}'s absolute value greater than {y}'s absolute value")
else:
    print("X is less than Y")
