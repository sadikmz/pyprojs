# input_string = input("Enter a string")
# input_string = input_string[::-1]
# index = 0
# while index < len(input_string):
#     letter = input_string[index]
#     print(letter)
#     index +=1


input_string = input("Enter a string")
index = -1
length = -1 * len(input_string)
while index > length:
    letter = input_string[index]
    print(letter)
    index -=1
