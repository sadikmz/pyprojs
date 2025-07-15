# # input_num = "done"
# num_list = [1]
# # counter = len(num_list)
# input_num = input("Enter a number: ")
#
# sum = 0
# while input_num != "done":
#     try:
#         # input_num = input("Enter a number: ")
#         num_list = num_list.append(input_num)
#     except:
#         if type(input_num) == str():
#             print("Error, please enter numeric number")
#             continue
# for num in num_list:
#     sum +=num
#     # counter += 1
# average = sum/len(num_list)
#
#
# print(f"{sum} {len(num_list)} {average}")
#
#
#
#

def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter number input")
        return False

count = 0
total = 0.0
average = 0.0
while True:
    input_num = input("Enter a number: ")
    if input_num == "done":
        break

    number = check_for_float(input_num)
    if not number:
        continue

    count += 1
    total = total + number
#
# if count !=0:
#     count = count

average = total / count
print(total, count, average)

# check_for_float()