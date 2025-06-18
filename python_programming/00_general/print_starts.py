n = 5
star = 0
for x in range(1,6):
    for y in range(n):
        space = n-1
        print(" "*space, end="")
        star += 1
        print("*"*star, end="")
        n -=1
        print()
