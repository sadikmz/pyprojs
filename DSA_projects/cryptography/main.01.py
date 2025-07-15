alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def refacto_position(p_position, p_cipher_type):
    if p_cipher_type == "E":
        while p_position > 25:
            p_position = p_position - 26
    else:
        while p_position < 0:
            p_position = p_position + 26
    return p_position

def caesar_cipher(p_initial_text, p_shift_number, p_cipher_type):
    final_text = ""
    if p_cipher_type == "D":
        p_shift_number *= -1
    for char in p_initial_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + p_shift_number
            new_position = refacto_position(new_position, p_cipher_type)
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"Here is the {'decode' if p_cipher_type == 'D' else 'encode'}d result: {final_text}")

from logo import logo
print(logo)
end_program = False
while not end_program:
    enc_dec = input("Type 'E' to encrypt or 'D' to decrypt:\n")
    message = input("Enter your message:\n").upper()
    shift_number = int(input("Enter the shift number:\n"))
    caesar_cipher(message, shift_number, enc_dec)
    restart  = input("Type 'Y' if you want to continue. Otherwise type 'N':\n")
    if restart == 'N':
        end_program = True
        print(logo)
        print("See you next time!")
