count = 0
total = 0
print("Count before", count)
print("Total before", total)
for value in [9,41,12,3,74,15]:
    # zork = zork + 1
    count += 1
    total = total + value
    print(count,value, total)
print("Count after", count)
print("Total after", total)
print(total/count)