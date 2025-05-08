def factors(n):
    resuts = []
    for k in range(1,n+1):
        if  n % k == 0:
            resuts.append(k)
    return resuts

print(factors(100))
