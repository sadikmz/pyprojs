import csv


class Squares:
    def __init__(self, length):
        self.squares = [i ** 2 for i in range(length) ]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, s):
        return self.squares[s]

# for number in Squares(5):
#     print(number)
#
# for number in reversed(Squares(5)):
#     print(number)

# The reverse function returns iterator

# override the reversed method in sequence types - we can specify ourselves

class Squares:
    def __init__(self, length):
        self.squares = [i ** 2 for i in range(length) ]

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, s):
        return self.squares[s]

    def __reversed__(self):
        print('__reversed__ called')
        return 'Hello python'

for number in reversed(Squares(5)):
    print(number)


# reversed_iter = reversed(Squares(5))
#
# print(type(reversed_iter))

def parse_data_row(row):
    row = row.strip('\n').split(';')
    return row[0], float(row[1])

def max_mpg(data):
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg
        return max_mpg

# f = open('cars.csv')
# next(f)
# next(f)
# print(max_mpg(f))
# f.close()

def list_data(data,max_mpg):
    for row in data:
        car, mgp = parse_data_row(row)
        mpg_perc = (mgp / max_mpg) * 100
        print(f'{car}: {mpg_perc:.2f}%')

# f = open('cars.csv')
# next(f), next(f)
# list_data(f,18.0 )
# f.close()


# combine all
# with open('cars.csv') as f:
#     next(f)
#     next(f)
#     max_ = max_mpg(f)
#     print(max_)

# with open('cars.csv') as f:
#     next(f), next(f)
#     max_ = max_mpg(f)
#
# with open('cars.csv') as f:
#     next(f), next(f)
#     list_data(f,max_)

# with open('cars.csv') as f:
#     cars = f.readlines()[2:]
# print(cars)

print('-----here-----')
def list_data(data):
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg
        # return max_mpg

    for row in data:
        car, mgp = parse_data_row(row)
        mpg_perc = (mgp / max_mpg) * 100
        print(f'{car}: {mpg_perc:.2f}%')

with open('cars.csv') as f:
    next(f), next(f)
    list_data(f)


# print('-----here add iterator -----')
# def list_data(data):
#     if iter(data) is data:
#         raise ValueError('Data cannot be iterator')
#     max_mpg = 0
#     for row in data:
#         _, mpg = parse_data_row(row)
#         if mpg > max_mpg:
#             max_mpg = mpg
#         return max_mpg
#
#     for row in data:
#         car, mgp = parse_data_row(row)
#         mpg_perc = (mgp / max_mpg) * 100
#         print(f'{car}: {mpg_perc:.2f}%')
#
# with open('cars.csv') as f:
#     next(f), next(f)
#     list_data(f)


print('-----here add iterator -----')
def list_data(data):
    if iter(data) is data:
        data = list(data)
        # raise ValueError('Data cannot be iterator')
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg
        # return max_mpg

    for row in data:
        car, mgp = parse_data_row(row)
        mpg_perc = mgp / max_mpg * 100
        print(f'{car}: {mpg_perc:.2f}%')

with (open('cars.csv') as f):
    next(f)
    next(f)
    list_data(f)

# print(ld)