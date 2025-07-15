import string

# alphabet = list(string.ascii_uppercase)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(alphabet)
cipher_message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))


def decrypt(p_message, p_shift_number):
    message = ""
    for char in p_message:
        position = alphabet.index(char)
        # calculate based on the old position:
        # print(char, position)
        old_position = position - p_shift_number
        letter = alphabet[old_position]
        message += letter
    return f"The decoded message is {message}"
    # alphabet = list(string.ascii_uppercase)

print(decrypt(cipher_message, shift_number))

# print(alphabet)