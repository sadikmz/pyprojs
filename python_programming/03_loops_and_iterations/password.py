import random
import string

letters =  string.ascii_letters
nums = string.digits
symbols = string.punctuation

number_of_letters = int(input("How many letters do you want in your password? "))
number_of_nums = int(input("How many numbers do you want in your password? "))
number_of_symbol = int(input("How many symbols do you  want in your password? "))

password = ""

for letter in range(1, number_of_letters + 1):
    password += random.choice(letters)

for num in range(1, number_of_nums+1):
    password += random.choice(nums)

for symbol in range(1, number_of_symbol+1):
    password += random.choice(symbols)

print(f"Your password is: {password}")

password_list = list(password)
random.shuffle(password_list)

password_reshufled = ""

for pas in password_list:
   password_reshufled +=pas

print(f"Your updated password is {password_reshufled}")

