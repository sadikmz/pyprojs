def squares(n):
    for i in range(n):
        yield i**2

print(list(squares(5)))
print(min(squares(5)))
print(max(squares(5)))
print(sum(squares(5)))

# caution
sq = squares(5)
print(min(sq))
# print(max(sq))

# boolean
print(bool(10))
print(bool([]))
print(bool([None]))
print(bool({}))

sq = squares(5)

print(min(sq))
# print(max(sq))
sq_l = list(sq)
print(dir(sq_l))
print(bool(sq)) # it the iterable object does not implement __len__ or / and __bool__ method, bool return True

# Example
class Person:
    pass

person = Person()
print(bool(person))

# overriding that method
class Person:
    def __bool__(self):
        return False

person = Person()
print(bool(person))

class Person:
    def __len__(self):
        return 0

person = Person()
print(bool(person))


# combined
class Person:
    def __len__(self):
        return 0

    def __bool__(self):
        return True

person = Person()
print(bool(person))


class MySeq:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self):
        pass

my_seq = MySeq(0)
print(bool(my_seq))
my_seq = MySeq(10)
print(bool(my_seq))

# Using any

print(any([0,'',None]))
print(any([10,'',None]))
print(any([0,'',None,(10,29)]))

# using all

print(all([10,'hello']))
print(all([10,None,'hello']))

# testing comparison
print('------testing comparison-------')
from numbers import Number
print(isinstance(5, Number))
print(isinstance(10, Number))
# print(isinstance(Decimal('10.5'), Number))

l = [10,20,30,40,'hello']

is_all_numbers = True
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break

print(is_all_numbers)

# alternative option: use all option

l = [10,20,30,40]

print(all(l))

def is_numeric(v):
    return isinstance(v, Number)

pred_l = map(is_numeric, l)
print(list(pred_l))
# or

pred_l = (is_numeric(item) for item in l)
print(list(pred_l))

# or using lambda
pred_l = map(lambda x: isinstance(x,Number), l)
print(list(pred_l))

l = [10,20,30,40,'hello']

# Much more pythonic way to test all the elements of the l are numbers
print(all(map(lambda x: isinstance(x, Number), l)))

# Another example

# with open('car-brands.txt') as f:
#     for row in f:
#         print(row)

# with open('car-brands.txt') as f:
#     for row in f:
#         print(len(row), row, end='')

with open('car-brands.txt', encoding='utf8', errors='ignore') as f:
    for row in f:
        print(len(row), row, end='')

with open('car-brands.txt', encoding='utf8', errors='ignore') as f:
    result = all(map(lambda row: len(row) >= 4, f))
print(result)

with open('car-brands.txt', encoding='utf8', errors='ignore') as f:
    result = any(map(lambda row: len(row) >10, f))
print(result)

with open('car-brands.txt', encoding='utf8', errors='ignore') as f:
    result = any(map(lambda row: len(row) >= 13, f))
print(result)

with open('car-brands.txt', encoding='utf8', errors='ignore') as f:
    result = all((len(row) >= 4 for row in f))
print(result)