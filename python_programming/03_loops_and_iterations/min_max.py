def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False

input1 = input("Enter a number")
if input1 == "done":
    quit()
number = check_for_float(input1)
if not number:
    print("The entered has to be number to continue...")
    quit()

min = number
max = number

while True:
    input_num = input("enter a number: ")
    if input_num == "done":
        break

    number = check_for_float(input_num)
    if not number:
        continue

    # num_list = num_list.append(number)

    # num_list.
    if number > max:
        max = number

    if number < min:
        min = number

print(f"Maximum number: {max}, Minimum number: {min}")