counts = dict()
names = ['csev', 'cwen', 'csev', 'cwen','zqian']

for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)