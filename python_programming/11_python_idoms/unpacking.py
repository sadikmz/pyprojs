result = {}
result.items()
for x, y in [(7,2),(5,8),(6,4)]:
    result[x] = y

print(list(result.items()))