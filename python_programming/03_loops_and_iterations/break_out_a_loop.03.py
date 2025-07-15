# def num_divisible_byfive(p_list):
#     for num in p_list:
#         if num%5 == 0:
#             if num > 130:
#                 print("Stop")
#                 break
#             print(num)
#
#
# list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
#
# num_divisible_byfive(list1)


def numbers_divisible_byfive(p_list):
    for num in p_list:
        # if num%5 == 0:
        if num > 130:
            break
        if (num%5 == 0):
            print(num)
    print("Stop")


list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]

numbers_divisible_byfive(list1)