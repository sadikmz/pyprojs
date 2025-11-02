# with open("cars.csv") as file:
#     row_index = 0
#     for line in file:
#         if row_index == 0:
#             headers = line.strip('\n').split(';')
#             print('headers', headers)
#         elif row_index == 1:
#             # data types row
#             data_types = line.strip('\n').split(';')
#             print('types', data_types)
#         else:
#             # data row
#             data = line.strip('\n').split(';')
#             print('data', data)
#         row_index += 1

# do some processing

from collections import namedtuple

cars = []

with open("cars.csv") as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            headers = line.strip('\n').split(';')
            Car = namedtuple('Car', headers)
            print('headers', headers)
        elif row_index == 1:
            # data types row
            data_types = line.strip('\n').split(';')
            print('types', data_types)
        else:
            # data row
            data = line.strip('\n').split(';')
            car = Car(*data)
            cars.append(car)
            # print('data', data)
        row_index += 1

# print(cars)


def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return float(value)
    else:
        return str(value)

# list(zip(data_types,data_))

def cast_row(data_type, data_row):
    return [cast(data_type, value)
            for data_type, value in zip(data_type, data_row)]

# update

from collections import namedtuple

cars = []

with open("cars.csv") as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            headers = line.strip('\n').split(';')
            Car = namedtuple('Car', headers)
            # print('headers', headers)
        elif row_index == 1:
            # data types row
            data_types = line.strip('\n').split(';')
            # print('types', data_types)
        else:
            # data row
            data = line.strip('\n').split(';')
            data = cast_row(data_types, data)
            car = Car(*data)
            cars.append(car)
            # print('data', data)
        row_index += 1

# print(cars)

# update

# from collections import namedtuple
#
# cars = []
#
# with open("cars.csv") as file:
#     file_iter = iter(file)
#     headers = next(file_iter).strip('\n').split(';')
#     Car = namedtuple('Car', headers)
#     data_types = next(file_iter).strip('\n').split(';')
#
#     for line in file_iter:
#         data = line.strip('\n').split(';')
#         data = cast_row(data_types, data)
#         car = Car(*data)
#         cars.append(car)
#
# print(cars)

# clean-up more using comprehension
del cars

from collections import namedtuple

with open("cars.csv") as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n').split(';')
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')

    cars_data = [cast_row(data_types, line.strip('\n').split(';')) for line in file_iter]

    cars = [Car(*car) for car in cars_data]

print(cars)