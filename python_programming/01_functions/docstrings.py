# Docstrings
# from python_programming.code3.code3.xml3 import result
# from python_programming.code3.code3.xml3 import result
from multiprocessing.connection import answer_challenge


# def formate_name (f_name, l_name):
#     """This function formats first and last name"""
#     if f_name == "" or l_name == "":
#         return "Name of last name cannot be empty!"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name}, {formated_l_name}"
#     print("This will not be executed")
#     # print(f_name.title())
#     # print(l_name.title())
# first_name = input("Enter Name: ")
# last_name  = input("Enter SName: ")
# output = formate_name(first_name, last_name)
# print(output)

# def pick_operation(n1,n2,operator):
#     n1 = int(n1)
#     n2 = int(n2)
#     operator = operator
#     if operator == "*":
#         result = n1*n2
#     elif operator == "/":
#         result = n1/n2
#     elif operator == "+":
#         result = n1+n2
#     else:
#         result = n1-n2
#
#     return f"{n1} {operator} {n2} = {result}"
#
# n1 = input("What's the first number? ")
# n2 = input("What is the second number?: ")
# operator = input("Pick operation from this list (+,-,*./): ")
#
# output = pick_operation(n1, n2, operator)
# print(output)

# define function for each operation
def add(n1,n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

n1 = input("What's the first number? ")
n2 = input("What is the second number?: ")
operator = input("Pick operation from this list (+,-,*./): ")

if operator == "*":
    result = add(n1,n2)
elif operator == "/":
    result = add(n1, n2)
elif operator == "+":
    result = add(n1, n2)
elif operator == "-":
    result = subtract(n1,n2)

print(f"{n1} {operator} {n2} = {result}")

# n1 = input("What's the first number? ")
# n2 = input("What is the second number?: ")
# operator = input("Pick operation from this list (+,-,*./): ")
#
# output = pick_operation(n1, n2, operator)
# print(output)

# return vs print statement
# define function for each operation
def add(n1,n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

n1 = input("What's the first number? ")
n2 = input("What is the second number?: ")
operator = input("Pick operation from this list (+,-,*./): ")

def calculate(n1, n2, operator):
    if operator == "*":
        result = add(n1,n2)
    elif operator == "/":
        result = add(n1, n2)
    elif operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1,n2)
    return result

output = calculate(n1,n2,operator)
print(f"{n1} {operator} {n2} = {output}")

new_operation = input("Pick another operation from this list (+,-,*./): ")
n3 = input("What's the third number? ")

new_output = calculate(n3,new_operation)
print(f"{n3} {new_operation} {output} = {new_output}")