from itertools import repeat, count, cycle, islice

# Count

g = count(10)
print(list(islice(g, 10)))

g = count(1, 0.5)
print(list(islice(g, 10)))

g = count(1_1j, 1+2j)
print(list(islice(g, 5)))

from decimal import Decimal

g = count(Decimal('0'),Decimal('1'))
print(list(islice(g, 10)))

# Cycle
g = cycle(('red', 'green', 'blue'))
print(list(islice(g, 2)))

def colors():
    yield 'red'
    yield 'green'
    yield 'blue'

cols = colors()
print(list(cols))
print(list(cols))

# using cycle function

g = cycle(colors())
print(list(islice(g, 9)))

# example

from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
def card_deck():
    randks = tuple(str(num) for num in range(2, 11)) + tuple("JQKA")
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in randks:
            yield Card(rank, suit)

# print(list(islice(card_deck(), 10)))

hands = [list() for _ in range(4)]
# print(hands)
index = 0
for card in card_deck():
    index = index % 4
    hands[index].append(card)
    index += 1
print(hands)

hands = [list() for _ in range(4)]

index_cycle = cycle([0,1,2,3])

print(list(islice(index_cycle,8)))
print(list(islice(index_cycle,9)))
print(list(islice(index_cycle,8)))
print(list(islice(index_cycle,9)))
print(list(islice(index_cycle,8)))

# index_cycle = cycle([0,1,2,3])
#
# for card in card_deck():
#     hands[next(index_cycle)].append(card)
# print(hands)


# hands = [list() for _ in range(4)]
#
# hands_cycle = cycle(hands)
# for card in card_deck():
#     hands = next(hands_cycle)
#     hands.append(card)

hands = [list() for _ in range(4)]

hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)


# Repeat function

g = repeat('Python')

for i in range(5):
    print(next(g))

g = repeat('Python', 4)
print(list(g))

hands = [[]] * 4

hands[0].append(4)
print(hands)

hands = [list() for _ in range(4)]
hands[0].append(4)
print(hands)

g = repeat([], 4)
g_l = list(g)
g_l[0].append(4)
print(g_l)
