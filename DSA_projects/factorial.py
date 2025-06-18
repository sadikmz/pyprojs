fact  = int(input("Enter a number: "))

res = 1
for i in range(fact, 0, -1):
    res = res * i
print(f"The factorial of {fact} is : {res}")
