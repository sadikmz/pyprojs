import  string

# alphabet = list(string.ascii_uppercase)
# print(alphabet)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))

def encrypt(p_message,p_shift_number):
    cipher_message = ""
    for char in p_message:
        # checkin for letters
        # print(char)
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_shift_number
            # if the index is >25
            while new_position > 25:
                new_position = new_position - 26
            new_char = alphabet[new_position]
            cipher_message += new_char
        else:
            cipher_message += char
    return f"The encoded message is {cipher_message}"

        # print(position, new_position)
        # print(position)
encoded_message = encrypt(message,shift_number)
# encrypt(message,shift_number)

print(encoded_message)
