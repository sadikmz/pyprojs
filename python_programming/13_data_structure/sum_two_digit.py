def sum_of_two_digits():
    two_digit_num = input("Enter two digit number: ")
    sum_of_digits = int(two_digit_num[0]) + int(two_digit_num[1])
    return sum_of_digits

print(sum_of_two_digits())

# or

number = input("Enter an integer number: ")
sum_digits = 0
for num in number:
    sum_digits += int(num)

print(sum_digits)