# Exercise Conditions - 2

import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

# Compare the numbers to eachother 

x = number1
y= number2

if x > y:
    print(f'{x} is greater than {y}')
elif y > x:
    print(f'{y} is greater than {x}')
else:
    print(f'{x} is actually equal to {y}')
