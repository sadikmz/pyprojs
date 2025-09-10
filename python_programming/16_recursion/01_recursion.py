# Ways to write recursion
# 1. Identify the recursive case - the flow.
# Example factorial: n! = n*(n-1)*(n-2)*...2*1
# 2. Establish a base case - the stopping criterion
# 3. Unitentional case - the constraint

# import sys
# sys.setrecursionlimit(1000000)
def factorial(n):
    assert n >= 0 and int(n) == n, "n must be a positive integer"
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))