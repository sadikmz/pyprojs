def matrix(n):
    gen = ( (i * j for j in range(1, n+1))
           for i in range(1, n+1)
    )
    return gen

# m = list(matrix(5))

# generator function using yield
# def matrix_iterator(n):
#     for row in matrix(n):
#         for item in row:
#             yield item

# for item in matrix_iterator(3):
    # print(item)

# change generator function using yield from

def matrix_iterator(n):
    for row in matrix(n):
        yield from row

for item in matrix_iterator(3):
    print(item)

# another example
file_1 = 'car1.txt'
file_2 = 'car2.txt'
file_3 = 'car3.txt'
files = file_1, file_2, file_3

brands = []

# with open('car1.txt') as f:
#     for brand in f:
#         brands.append(brand.strip('\n'))
#
# with open('car2.txt') as f:
#     for brand in f:
#         brands.append(brand.strip('\n'))
#
# with open('car3.txt') as f:
#     for brand in f:
#         brands.append(brand.strip('\n'))

cars = open('car1.txt')
for car in cars:
    brands.append(car.strip('\n'))

# cars = open('car2.txt', 'r')
# for car in cars:
#     brands.append(car.strip('\n'))
#
# cars = open('car3.txt', 'r')
# for car in cars:
#     brands.append(car.strip('\n'))
cars.close()
# with open(file_1) as f:
#     for brand in f:
#         print(brand)
        # brands.append(brand.strip('\n'))
# with open(file_2) as f:
    # for brand in f:
    #     brands.append(brand.strip('\n'))
# with open(file_3) as f:
#     for brand in f:
#         brands.append(brand.strip('\n'))

# print(brands)
