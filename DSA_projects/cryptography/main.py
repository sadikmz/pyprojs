import  string

# alphabet = list(string.ascii_uppercase)
# print(alphabet)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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

from logo import logo
print(logo)
end_program = False
while not end_program:
    enc_dec = input("Type 'E' to encrypt or 'D' to decrypt:\n")
    message = input("Enter your message:\n").upper()
    shift_number = int(input("Enter the shift number:\n"))

    if enc_dec == 'E':
        encrypted_message = encrypt(message, shift_number)
        print(encrypted_message)
    else:
        decrypted_message = decrypt(message, shift_number)
        print(decrypted_message)
    restart  = input("Type 'Y' if you want to continue. Otherwise type 'N':\n")
    if restart == 'N':
        end_program = True
        print("See you next time!")
