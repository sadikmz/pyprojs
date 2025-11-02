from collections import namedtuple

Card = namedtuple('Card', 'rank suit')
SUITS = ('Spade', 'Heart', 'Diamond', 'Club')
RANKS = tuple(range(2,11)) + tuple('JQKA')

# suit_index = card_index // len(RANKS)
# rank_index = card_index % len(RANKS)

def card_gen():
    for i in range(len(SUITS) * len(RANKS)):
        suit = SUITS[i // len(RANKS)]
        rank = RANKS[i % len(RANKS)]
        card = Card(rank, suit)
        yield card

# for card in card_gen():
#     print(card)


# rewrite the generator function

def card_gen():
    for suite in SUITS:
        for rank in RANKS:
            yield Card(rank, suite)

# for card in card_gen():
#     print(card)

# make it iterable


class CardDec:
    # encapsulate everything into this class
    # Card = namedtuple('Card', 'rank suit')
    SUITS = ('Spade', 'Heart', 'Diamond', 'Club')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDec.card_gen()

    # This is a static method - it does not require to look at the instances
    @staticmethod
    def card_gen():
        for suite in CardDec.SUITS:
            for rank in CardDec.RANKS:
                yield Card(rank, suite)

deck = CardDec()

print(list(deck))
print(list(deck))

# reversed(CardDec)
# Implement the reversed method for Cardec

class CardDec:
    # encapsulate everything into this class
    # Card = namedtuple('Card', 'rank suit')
    SUITS = ('Spade', 'Heart', 'Diamond', 'Club')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDec.card_gen()

    # Implemented the reversed method
    def __reversed__(self):
        return CardDec.reversed_card_gen()

    # This is a static method - it does not require to look at the instances
    @staticmethod
    def card_gen():
        for suite in CardDec.SUITS:
            for rank in CardDec.RANKS:
                yield Card(rank, suite)

    @staticmethod
    def reversed_card_gen():
        for suite in reversed(CardDec.SUITS):
            for rank in reversed(CardDec.RANKS):
                yield Card(rank, suite)

rev = CardDec.reversed_card_gen()

print(list(rev))