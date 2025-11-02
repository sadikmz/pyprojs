_SUITS = ('Spades','Hearts', 'Diamonds', 'Clubs')
_RANKS = tuple(range(2, 11)) + tuple('JQKA')

from collections import namedtuple
Card = namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    class CardDeckIterator:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                suit = _SUITS[self.i // len(_RANKS)]
                rank = _RANKS[self.i % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)

deck = CardDeck()

for card in deck:
    print(card)

# get the last x item of the carddecs
# deck = CardDeck()
deck_list = list(deck)
print(deck_list[:-8:-1])


l = [1,2,3,4]
l_rev_it=reversed(l)
print(list(l_rev_it))
for i in l_rev_it:
    print(i)

# trying it on deck

# reversed_deck = reversed(deck)
# print(list(reversed_deck))

# It needs to find a special method to reverse when the revered is called __reverse__

class CardDeck:
    def __init__(self):
        self.length = len(_SUITS) * len(_RANKS)

    def __len__(self):
        return self.length

    def __reversed__(self):
        print('reversed')
        return self.CardDeckIterator(self.length, reverse=True)

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.reverse = reverse
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1  - self.i
                else:
                    index = self.i
                suit = _SUITS[index // len(_RANKS)]
                rank = _RANKS[index % len(_RANKS)]
                self.i += 1
                return Card(rank, suit)

deck = reversed(CardDeck())

for card in deck:
    print(card)

