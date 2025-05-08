def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield k/n
        k += 1
        if k * k == n:
            yield k

factors(100)