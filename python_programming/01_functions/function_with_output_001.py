# def formate_name (f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
#
# formate_name("test", "this")


# def formate_name (f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name}, {formated_l_name}"
#     print("This will not be executed")
#     # print(f_name.title())
#     # print(l_name.title())
# output = formate_name("test", "this")
# print(output)


# Multiple outout

# def formate_name (f_name, l_name):
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


def password_controller(password):
    if len(password) > 8:
        return  True
    else:
        return False

result = password_controller("faljf")
print(result)