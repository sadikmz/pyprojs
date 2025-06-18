custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

# for item in custom_list:
#     # print(item)
#     if item == int(item):
#         print(int(item))
# # print(int("10.1"))
#
# for item in custom_list:
#     if type(item)==int:
#         print(item)

for item in custom_list:
    if isinstance(item,int):
        print(item)