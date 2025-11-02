import itertools

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} + {j} = {i*j}'

print(list(itertools.islice(matrix(10), 10,20)))

l1 = ['x1', 'x2', 'x3', 'x4']
l2 = ['y1', 'y2', 'y3']

for x in l1:
    for y in l2:
        print((x,y), end=' ')
    print(end=' ')

# itertoosl product

print(list(itertools.product(l1, l2)))

#

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield (i, j, i*j)

print(list(matrix(5)))

# rewrite using itertools product function

def matrix(n):
    yield from itertools.product(range(1, n+1), range(1, n+1))

print(list(matrix(4)))

def matrix(n):
    for i, j in itertools.product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

print(list(matrix(4)))

# return a generator expression

def matrix(n):
    return ((i,j, i*j)
            for i, j in itertools.product(range(1, n+1), range(1, n+1)))

print(list(matrix(4)))

#

from itertools import tee

def matrix(n):
    return ((i,j, i*j)
            for i, j in itertools.product(*tee(range(1, n+1), 2)))

print(list(matrix(4)))

# Generate a grid of coordinate

def grid(min_val, max_val, steps,*,num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                        itertools.count(min_val, steps))
    axes = itertools.tee(axis, num_dimensions)

    return itertools.product(*axes)

print(list(grid(min_val=-1, max_val=1, steps=0.5, num_dimensions=3)))

# Determining the odd of rolling a pair of dice

sample_space = list(itertools.product(range(1, 7), range(1, 7)))
# print(list(sample))
outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample_space))
# print(list(outcomes))
# len(outcomes) / len(sample_space)

from fractions import Fraction
odds = Fraction(len(outcomes), len(sample_space))
print(odds)

# Permutation
# l1 = 'abc'
# print(list(itertools.permutations(l1)))
# print(list(itertools.permutations(l1,2)))

l1 = 'abca'
# print(list(itertools.permutations(l1)))
# print(list(itertools.permutations(l1,2)))

# Combination
print(list(itertools.combinations([1,2,3,4],2)))
print(list(itertools.combinations([4,3,2,1],2)))

# with replacement
print(list(itertools.combinations_with_replacement([1,2,3,4],2)))
print(list(itertools.combinations_with_replacement([4,3,2,1],2)))

# The odds of pulling 4 consecutive aceses from deck card

SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')
print(RANKS)
dec = [rank + suit for suit in SUITS for rank in RANKS]
# print(dec)
# using a cartesian product
print(list(rank + suit for suit, rank in itertools.product(SUITS, RANKS)))

from collections import namedtuple
Card = namedtuple('Card', 'rank suit')
deck = (Card(rank,suit)
        for suit in SUITS for rank in RANKS)

# sample space: Use combination without replacement
# sample_space = itertools.combinations(deck, 4)

# deck = (Card(rank,suit)
#         for suit in SUITS for rank in RANKS)

sample_space = itertools.combinations(deck, 4)
total = 0
acceptable = 0
for outcome in sample_space:
    total += 1
    for card in outcome:
        if card.rank != 'A':
            break
    else:
        acceptable += 1

print(f'total = {total}, acceptable={acceptable}')
print(f'odds = {Fraction(acceptable,total)}')
print(f'odds = {acceptable/total:.10f}')

# simplify a lit bit using all function whether the outcome is Ace or not
deck = (Card(rank,suit)
        for suit in SUITS for rank in RANKS)

sample_space = itertools.combinations(deck, 4)
total = 0
acceptable = 0
for outcome in sample_space:
    total += 1
    if all(map(lambda x: x.rank == 'A', outcome)):
        acceptable += 1

print(f'total = {total}, acceptable={acceptable}')
print(f'odds = {Fraction(acceptable,total)}')
print(f'odds = {acceptable/total:.10f}')