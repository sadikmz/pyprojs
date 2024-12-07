fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # print('*w*')
        # print('**',w,di.get(w,-99))
        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount +1
        # di[w] = newcount
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w,'new',di[w])

        # print(w,'new',newcount)

        # if w in di :
        #     di[w] = di[w] + 1
            # print('**Exisiting**')
        # else:
        #     di[w] = 1
            # print('***New***')
        # print(w,di[w])
# print(di)

# generate list of key-value pairs
# x = sorted(di.items())
# print(x[:5])

tmp = list()
for k, v in di.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)
print('Flipped', tmp)

tmp = sorted(tmp, reverse=True)
print(tmp[:5])

# Reverse key value order

for v,k in tmp[:5]:
    print(k,v)