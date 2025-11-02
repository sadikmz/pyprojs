# lazy evaluation
# This is ofter used in class properties
# properties of classes may not always be populated when the object is creatd.
# Value of a property only becomes known when the property is requested - deferred.
# Example

# class Actor:
#     def __init__(self, actor_id):
#         self.id = actor_id
#         self.bio = lookup_actor_in_db(actor_id)
#         self.movies = None
#
#         @property
#         def movies(self):
#             if self.movies is None:
#                 self.movies = lookup_movies_in_db(self.actor_id)
#             return self.movies

# A

import math
class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self.area = math.pi * (r **2)

# c = Circle(1)
#
# print(c.area)
# print(c.area)

# print(c.radius)
# c.radius = 2
# print(c.area)

# Delay calculating the area until requested
class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    @property
    def area(self):
        print('Calculating area')
        return math.pi * (self.radius ** 2)


# c = Circle(1)
#
# print(c.area)
# print(c.area)
# print(c.radius)
# c.radius = 2
# print(c.area)


# I dont want to calculate the area everytime the radius is updated -
# I want to know the area needs to be calculated or I store the area and used the stored value
# It almost going to be like a cache

class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)
            print('Calculating area')
        return self._area


# c = Circle(1)
#
# print(c.area)
# print(c.area)
# # print(c.radius)
# c.radius = 2
# print(c.area)
# print(c.area)

# using iterator

class Factorials:
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        return self.FactIter(self.length)

    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result


# facts = Factorials(5)
#
# print(list(facts))

# it doesn't have to be finite

class Factorials:

    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result

facts = Factorials()
fact_iter = iter(facts)
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))
print(next(fact_iter))

# print(list(facts))