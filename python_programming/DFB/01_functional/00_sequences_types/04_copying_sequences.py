s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(s[0])
print(id(s[0]))

print('\n-----original-----')
print(id(s[0][0]))
cp = s.copy()

print(cp)
print(cp[0])
print(id(cp[0]))
cp[0] = 'python'
print(cp)
print(cp[0])
print(id(cp[0]))
print(s)
cp = s.copy()
print(cp[0][0])

print('\n-----copy-----')
print(id(cp[0][0]))
cp[0][0] = 'python'
print(cp[0][0])

print('\n-------after replacing with python-----')
print(id(cp[0][0]))

print('\n----original-----')
print(s)
print(id(s[0][0]))