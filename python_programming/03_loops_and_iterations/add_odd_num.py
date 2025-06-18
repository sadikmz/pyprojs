def add_odd_numbers(num):
    sum = 0

    if num%2==0:
        for odd_num in range(1,num,1):
            sum +=odd_num
    else:
        for odd_num in range(1,num,2):
            sum += odd_num
    return sum



# print(add_odd_numbers(6))

# 1,3,5
# 1,3,5,7

def add_even_numbers(start,end):
    sum = 0
    for i in range(start,end+1):
        if i%2==0:
            sum +=i
    return sum
print(add_even_numbers(1,4))
