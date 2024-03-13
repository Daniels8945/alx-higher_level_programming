#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
end = abs(number) % 10
if number < 0:
    print("Last digit of {} is {} and is grater than 5".format(number. end))
elif end == 0:
    print("Last digit of {} is {} and is )".format(number, end))
else:
    print(f"Last digit of {number:d} is {end:d} and is less  than 6 and not 0")

