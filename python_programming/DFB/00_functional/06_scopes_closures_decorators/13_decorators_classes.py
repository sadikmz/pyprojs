# Monkey patching: Add attribute at runtime
# We can use this to modify classes from outside while our code is running

from fractions import Fraction

f = Fraction(1, 2)
print(f.numerator)
print(f.denominator)

# it does not have speak method
Fraction.speak = 100

print(f.speak)

Fraction.speak = lambda self, message: 'Fraction says: {0}'.format(message)

print(f.speak("This is a late parrot"))

# Example: adding integral method in the fraction class

Fraction.is_integral = lambda self: self.denominator == 1

f1 = Fraction(2, 3)
f2 = Fraction(64,8)
print(f1,f2)
print(f1.is_integral())
print(f2.is_integral())

# Let's monkey patch this class but instead of writing directly writing this way
# let's use a function that we can call and decorate --modify the fraction class

def dec_speak(cls):
    # implement the class method
    cls.speak = lambda self, message: '{0} says: {1}'.format(self.__class__.__name__, message)
    return cls


Fraction = dec_speak(Fraction)

f1 = Fraction(2,3)
# f2 = Fraction(64,8)
# print(f1,f2)
print(f1.speak("Hello"))

class Person:
    pass

Person = dec_speak(Person)

p = Person()
print(p.speak("This works"))

# Let's see how we can add some debugging into to our class object

from datetime import datetime, timezone


def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    for k, v in vars(self).items():
        results.append('{0}: {1}'.format(k, v))

    return results

def debug_info(cls):
    cls.debug = info
    return cls


# class Person():
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year
#
#     def say_hi():
#         return 'Hello there'

# Long form of decorating
# Person = debug_infor(Person)

# short from: using decorator syntax
# del Person
# del p

@debug_info
class Person():
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return 'Hello there'


# p = Person('John',1939)
# print(p.debug())
# print(p.debug())

# using it in new class

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._spead = 0

    @property
    def spead(self):
        return self._spead

    @spead.setter
    def spead(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('speed must be lower than top speed')
        else:
            self._spead = new_speed


favorite = Automobile('Ford', 'Model T', 1989, 45)
print(favorite.debug())


