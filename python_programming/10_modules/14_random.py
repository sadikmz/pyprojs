import random

for _ in range(5):
    print(random.random())

random.seed(0)

for _ in range(5):
    print(random.random())

print("""New""")

random.seed(0)

for _ in range(5):
    print(random.random())

print("""randrange""")

random.seed(0)

for _ in range(5):
    print(random.randrange(1, 6))

print("""randint""")

random.seed(0)

# for _ in range(5):
#     print(random.randint(1,6))
#     print(random.randrange(1,6))
#
# for _ in range(3):
#     print(random.randint(1,3))
#
# for _ in range(3):
#     print(random.random())


data = [
    ('a', 12.3),
    ('b', 30.7),
    ('c', 20.4),
    ('d', 36.1),
]

# data01 = [
#     ('abcd', 12.3),
#     ('abc', 30.7),
#     ('bc', 20.4),
#     ('d', 36.1),
# ]

# for k, v in data:
#     print(f'{k}| {'*' * round(v)}')


def chart_freq(data: object):
    pad = max([len(str(el[0])) for el in data])
    for k, v in data:
        print(f'{str(k).rjust(pad)}| {'*' * round(v)}')


# chart_freq(data01)

random.seed(0)

# data = [random.randint(1, 10) for _ in range(5)]
# print(data)

# freq = {}
#
# for el in data:
#     freq[el] = freq.get(el, 0) + 1

# print(freq)

def freq_distribution(data):
    freq = {}
    for el in data:
        freq[el] = freq.get(el, 0) + 1
    return freq

# freq = freq_distribution(data)
freq = freq_distribution(data)

# relative frequency
sum_freq = sum(freq.values())
# print(sum_freq)
# relative_freq = freq.copy()

# for k in relative_freq:
#     relative_freq[k] = relative_freq[k] / sum_freq * 100
# print(relative_freq)

# dictionary comprehension
relative_freq = {k: v / sum_freq * 100 for k, v in freq.items()}
# print(relative_freq)
chart_freq(relative_freq.items())
sorted_items = sorted(relative_freq.items(), key=lambda x: x[0], reverse=False)
# print(sorted_items)
# chart_freq(sorted_items)

def analyse_randint(n, a, b):
    data = [random.randint(a, b) for _ in range(n)]

    freq = freq_distribution(data)
    rel = relative_freq(freq)
    sorted_rel = sorted(rel.items(), key=lambda x: x[0])
    chart_freq(sorted_rel)

random.seed(0)
print("""analyze randint""")
analyse_randint(10,1,10)
