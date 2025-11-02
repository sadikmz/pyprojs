from random import randint, random
from collections import namedtuple


def random_color():
    red = randint(0,255)
    blue = randint(0,255)
    green = randint(0,255)
    alpha = round(random(),2)
    return red, blue, green, alpha

color = random_color()

print(color)

red, blue, green, alpha = color
print(red, blue, green, alpha)


# create a namedtuple

Color = namedtuple('Color', 'red green blue alpha')

def random_color():
    red = randint(0,255)
    blue = randint(0,255)
    green = randint(0,255)
    alpha = round(random(),2)
    return Color(red, blue, green, alpha)

color = random_color()
print(color.alpha)
print(color.red)
print(color.green)
print(color.blue)
# print(color.red)
print()