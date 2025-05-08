# Using re.search() and startswith

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
# with regular expression

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search("^From:",line):
        print(line)
