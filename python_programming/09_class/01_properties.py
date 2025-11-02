# Properties also called modifiers that helps to control attribute properties - how we read and write attributes
# they are basically going through methods
import math
class Circle:
    def __init__(self, radius):
        if not(isinstance(radius, float) or isinstance(radius, int)):
            raise ValueError('radius must be a float or int.')
        if radius < 0:
            raise ValueError('radius must be a positive number.')
        self.radius = radius


    def area(self):
        return math.pi * self.radius ** 2

    def radius(self):
        print('radius getter called..')
        return self._radius

c = Circle(5)

c.radius = "test"
print(c.__dict__.items())
# print(c.area())