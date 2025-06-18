def find_max(n1, n2, n3):
    max = 0
    if n1 > n2:
        max = n1
    else:
        max = n2
    if max > n3:
        max = max
    else:
        max = n3
    return max

# n1 = int(input("Enter the first number : "))
# n2 = int(input("Enter the second number : "))
# n3 = int(input("Enter the third number : "))

# print(find_max(n1, n2, n3))

# or

def max_of_two(n1, n2):
    if n1 > n2:
        return n1
    return n2

def max_of_three(n1, n2, n3):
    max_two = max_of_two(n1, n2)
    max_of_three = max_of_two(max_two, n3)
    return max_of_three

# print(max_of_two(n1, n2))
print(max_of_three(1, 2, 10))