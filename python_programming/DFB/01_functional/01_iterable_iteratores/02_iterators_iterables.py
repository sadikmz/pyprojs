class Cities:
    def __init__(self):
        self._cities = ['Paris','Berlin','Rome','Madrid','London']
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item


cities = Cities()

print(type(cities))

print(list(enumerate(cities)))
# next(cities)
# Comprehension
#

class Cities:
    def __init__(self):
        self._cities = ['Paris','Berlin','Rome','Madrid','London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

cities = Cities()
print(len(cities))

# Write the iterator

class CityIterator:
    def __init__(self, city_obj):
        print('-----CityIterator new object-----')
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print('-----CityIterator __iter__ called-----')
        return self

    def __next__(self):
        print('-----CityIterator __next__ called-----')
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item

cities = Cities()

# for item in cities:
#     print(item)

# city_iterator = CityIterator(cities)
#
# for item in city_iterator:
#     print(item)
#
# for item in city_iterator:
#     print(item)
#
# city_iterator = CityIterator(cities)
#
# for item in city_iterator:
#     print(item)

# Avoid creating a city iterator everytime - use the iterable protcol --implement __iter__

class Cities:
    def __init__(self):
        self._cities = ['Paris','Berlin','Rome','Madrid','London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('----Cities __iter__ called')
        return CityIterator(self)

cities = Cities()

# for item in cities:
#     print(item)

# for item in cities:
#     # print('---here----')
#     print(item)

# for item in cities:
#     print(item)

# Clean-up and put it together

del CityIterator
del Cities

class Cities:
    def __init__(self):
        self._cities = ['Paris','Berlin','Rome','Madrid','London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('----Cities __iter__ called')
        return self.CityIterator(self)

    class CityIterator:
        def __init__(self, city_obj):
            print('-----CityIterator new object-----')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('-----CityIterator __iter__ called-----')
            return self

        def __next__(self):
            print('-----CityIterator __next__ called-----')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

cities = Cities()

# for city in cities:
#     print(city)

# print(list(enumerate(cities)))

# sorted(cities, key = lambda x: len(x))

# Recover the iterator ourselves by doing the following
city_iterator = cities.__iter__()
print(city_iterator)
# for city in city_iterator:
#     print(city)
#
# for city in city_iterator:
#     print(city)

s = {'a', 100, 'x', 'X'}
set_iterator = iter(s)
# for item in set_iterator:
#     print(item)
#
# for item in set_iterator:
#     print(item)

# Looking at sequences - sequence types mixing getitem

class Cities:
    def __init__(self):
        self._cities = ['Paris','Berlin','Rome','Madrid','London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('----Cities __iter__ called')
        return self.CityIterator(self)

    # make it to sequence class - by implementing a sequence protocol

    def __getitem__(self, index):
        print('getting item')
        return self._cities[index]

    class CityIterator:
        def __init__(self, city_obj):
            print('-----CityIterator new object-----')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('-----CityIterator __iter__ called-----')
            return self

        def __next__(self):
            print('-----CityIterator __next__ called-----')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

cities = Cities()
# print(cities[0])
# print(cities[1])
# for city in cities:
#     print(city)

l = [1,2,3,4,5]
# l.__iter__
# l.__getitem__
l_iter = iter(l)
for i in l_iter:
    print(i)
for i in l_iter:
    print(i)
# next(l_iter)

# set
s = {1,2,3,4,5}
s_iter = iter(s)
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)
next(s_iter)
# next(s_iter)
# print(s.__getitem__(0))