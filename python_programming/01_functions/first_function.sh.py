
# Defining functions
def my_first_function():
    print("Hello World")
    print("This is my First Function")
    print("Bye for now.")

#  Calling functions
# my_first_function()

def greet():
    print("Hello")
    print("How are you?")

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

# greet_with_name("Test")

def area_of_square(side):
    area = side * side
    print(area)

# area_of_square(6)

# consider multiple parameters
def greet_withNC(name, city):
    print(f"Hello {name}")
    print(f"What is the weather looks like in {city}")

greet_withNC("A", "B")
greet_withNC( city="B", name="A")

# import math
# test = 2.5
# print(math.ceil(test))
# print(math.ceil(2.5))

import math
def painting_wall(height, width):
    area_wall = height * width
    no_can = area_wall/4
    print(math.ceil(no_can))

painting_wall(2,5)


# import math
def calculate_can_number(height, width, coverage):
    area = height * width
    number_of_can = math.ceil(area/coverage)
    print(number_of_can)

height = int(input("Inpute height: "))
width = int(input("Inpute width: "))

calculate_can_number(height,width,4)