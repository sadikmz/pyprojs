import itertools

with open("cars_2014.csv") as f:
    for row in itertools.islice(f, 20):
        print(row,end='')

# How many model exist for each make

from collections import defaultdict

makes = defaultdict(int)

# if I request a value of a key it doesn't exist it will return 0

print(makes['abcd'])

# if I want to count something
makes['BMW'] = makes['BMW'] + 1
print(makes['BMW'])

makes['abcd'] = 0
makes['abcd'] = 1
makes['abcd'] += 1
print(makes['abcd'])

# continuing with example file
with open("cars_2014.csv") as f:
    next(f)
    for row in f:
        make, _ = row.strip('\n').split(',')
        makes[make] += 1
        # print(makes)

# for key, value in makes.items():
#     print(f'{key}: {value}')

# Using groupby

data = (1,2,2,3)
print(list(itertools.groupby(data)))
it = itertools.groupby(data)

for group in it:
    print(group[0], list(group[1]))

# or
it = itertools.groupby(data)

for group_key, sub_iter in it:
    print(group_key, list(sub_iter))

# different example

data = (
    (1,'abc'),
    (1,'bcd'),

    (2,'pyt'),
    (2,'pyt'),
    (2,'tho'),

    (3,'hon')
)

groups = itertools.groupby(data, key=lambda x: x[0])

# print(list(groups))

groups = itertools.groupby(data, key=lambda x: x[0])
for group_key, sub_iter in groups:
    print(group_key, list(sub_iter))

#

def gen_groups():
    # key 1
    for key in range(1,4):
        for i in range(3):
            yield(key,i)

g = gen_groups()

# print(list(g))

groups = itertools.groupby(g, key=lambda x: x[0])

for group in groups:
    print(group[0], list(group[1]))

# groups = itertools.groupby(g, key=lambda x: x[0])
# for group_key, sub_iter in groups:
#     print(group_key, list(sub_iter))


# continuing with example file
with open("cars_2014.csv") as f:
    make_groups = itertools.groupby(f, key=lambda x: x.split(',')[0])
    make_counts = ((key, len(models)) for key, models in make_groups)

# custom len function

def squares(n):
    for i in range(n):
        yield i**2
sq = squares(5)

# print(len(sq))
# Custom len func1:
i = 0
for item in sq:
    i +=1
print(i)

# Custom len func2
def len_iterable(iterable):
    i = 0
    for item in iterable:
        i += 1
    return i
sq = squares(5)
print(len_iterable(sq))

# Custom len func3: replace each element by 1 and sum up all
sq = squares(5)
print(sum(1 for i in sq))

# final solution
with open("cars_2014.csv") as f:
    next(f)
    make_groups = itertools.groupby(f, key=lambda x: x.split(',')[0])
    make_counts = ((key, sum(1 for i in make_groups))
                   for key, make_groups in make_groups)
    print(list(make_counts))