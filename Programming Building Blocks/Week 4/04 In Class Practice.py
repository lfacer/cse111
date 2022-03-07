#drawing tutorial
from itertools import count
import random

def draw_cloud (canvas, width, x_min, x_max, y_min, y_max):
    for i in range[0,4]:
        x_start = random.randrange (x_min, x_max)
        y_start = random.randrange (y_min, y_max)
        count


#definitions
import math
def calculate_circle_area(radius):
    return radius**2 * math.pi

area = calculate_circle_area(5)
print(area)


#return
#str = input("Please enter your name: ")

#for i in range(0, len(str), 2):
#    print(str[i])

#str_length = len(str)
#print (str_length)


#lists
fruits = ["apple", "orange"]
your_fruits = ["banana", "pear"]
fruits.extend(your_fruits)
new_fruit = ["grape"]
fruits.extend(new_fruit)
print(fruits)

