# Quantifier metacharacters
# * matches zero or more repetition
# + matches one or more repetition
# ? matches zero or one repetition
# ? Specifies the non-greedy version of *, + and ?
# ? Introduces a lookahead or lookbehind assertion
# ? Creates a named group
# {} Matches an explicitly specified number of repetitions

import re

# regex = re.compile(r'bana?na')
# mo = regex.search("banaana")
# print(mo)

# iron_regex = re.compile(r'Iron(wo)?man')
# mo = iron_regex.search("I adventure of Ironwooman")
# print(mo)

# phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phone_regex.search("This is my phone number: 777-8888")
# print(mo)