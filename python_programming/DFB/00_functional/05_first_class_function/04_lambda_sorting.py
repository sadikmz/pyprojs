import random

l = [1,2,3,4,5,6,7,8,9,10]

rand_func=lambda :random.random()
print(sorted(l,key=lambda x: random.random()))
