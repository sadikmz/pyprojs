def factorial(p_num):
    value = 1
    if abs(p_num) != p_num:
        print(f"Factorial does not exist for negative numbers")
    elif p_num==0:
        print(f"The factorial of {p_num} is 1")
    else:
        for num in range(1, p_num+1):
            value = value*num
        print(f"The factorial of {p_num} is {value}")

factorial(4)
