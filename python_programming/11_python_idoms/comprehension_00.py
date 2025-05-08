# [expression for value in iterable if condition]

# Equivalant form

# result = []
# for value in iterable:
#     if condition:
#         result.append(expression)

# a list of the squares of the number from 1 to n
n = 100
# squares = []
# for k in range(1,n+1):
#     squares.append(k*k)
# print(squares)


# Option2

# squares = [k*k for k in range(1,n+1)]
# print(squares)

# Option3
factors = [k for k in range(1,n+1) if n % k == 0]

print(factors)

# [ k k for k in range(1, n+1) ] list comprehension
# { k k for k in range(1, n+1) } set comprehension
# ( k k for k in range(1, n+1) ) generator comprehension
# { k:k k for k in range(1, n+1) } dictionary comprehension