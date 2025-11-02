# shuffling - it doesn't return shuffled list
# choice: choosing a single random element and return the random selected element
# choices: returns k random elements with replacement
# sample: sampling population, without replacement and returns a list of the randomly selected elements - uniformly distributed
# wighted choices: weight assigned to each element in the list

import random

random.seed(0)
l = [1,2,3,4,5]
random.shuffle(l)
print(l)
random.shuffle(l)
print(l)

l = [1,2,3,4,5]
for _ in range(5):
    print(random.choice(l))


s = sorted(set('abcdef'))
# print(s)
# random.seed(0)
print("Default randomization 0")
for _ in range(5):
    print(random.sample(s,3))

print("Default randomization 1")

for _ in range(5):
    print(random.sample(s,3))

print("After setting random seed to 1")
random.seed(0)
for _ in range(5):
    print(random.sample(s,3))

print("After setting random seed to 1")
random.seed(0)
for _ in range(5):
    print(random.sample(s,3))


try:
    random.sample(s, 9)
except ValueError as e:
    print(e)



random.seed(0)
for _ in range(5):
    print(random.randrange(2,100,2))
random.seed(0)
print([random.randrange(2,100,2) for _ in range(5)])
random.seed(0)
print([random.randrange(2,100,2) for _ in range(5)])
random.seed(0)
print([random.randrange(2,100,2) for _ in range(5)])