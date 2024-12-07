d = {'b':1,'c':22,'a':10}
tmp = list()
for k, v in d.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp)
print(tmp)
print(dir(tmp))
print(sorted(tmp,reverse=True))
tmp = sorted(tmp,reverse=True)
print(tmp)