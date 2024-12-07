fhand = open("romeo.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, value in counts.items():
    newtup = (key,value)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]
    print(key,val)


# sorter version with list comprehension

c = {'b':1,'c':22,'a':10}

print(sorted([(v,k) for k, v in c.items()]))