#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new_number = (-1) * number % 10
else:
    new_number = number % 10
    if new_number > 5:
        print(f'Last digit of {number} is {new_number} and is greator than 5')
        if new_number == 0:
            print(f'The last digit of {number} is {new_number} and is 0')
            if new_number < 6 and new_number != 0:
                print(f'Last digit of {number} is {new_number} and is less than 6 and not 0')
