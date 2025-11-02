# print(int(True))
# print(int(False))
# print(int(123))
# print(int("1010", base=10))
# print(int("A12F", base=16))
# print(int("5346", base=7))
# print(int("B", base=12))

# Reverse Process: Changing an integer from base 10 to another base
# built-in functions
# bin(): a binary representation of base 2
# oct(): a binary representation of base 8
# hex(): a binary representation of base 6

# print(hex(10))
# print(0xA)

# other bases?: You need custom code
def base_change(n,b):
    if b < 2 or n < 0:
        raise ValueError('b >=2')
    if n < 0:
        raise ValueError('n must be positive')
    if n == 0:
        return [0]

    digits = []

    while n > 0:
        # m = n % b
        # n = n // b
        # m, n = n % b, n // b
        n, m = divmod(n, b) # use python's default divmod function
        digits.insert(0, m)
    return digits

# print(base_change(5,232))
# print(base_change(16,1485))

# encodings
def encode(digits,digits_map):
    if max(digits) >= len(digits_map):
        raise ValueError('digits map is not long enough to encode the digits')

    encoding = ''
    # for d in digits:
    #     encoding += digits_map[d]
    return ''.join([digits_map[d] for d in digits])

# print(encode([10,15],'0123456789ABCDEF'))


def rebase_from10(number,base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base < 36')

    sign = -1 if number < 0 else 1
    number *= sign

    digits = base_change(number,base)
    encoding = encode(digits,digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

# e=rebase_from10(-314,2)
# print(e)
# print(int(e,base=2))

e=rebase_from10(-3451,16)
print(e)
print(int(e,base=16))



# digits_encodings = ''
# digits_list=[]
# map_string=''
# for d in digits_list:
#     digits_encodings += map_string[d]
# # The above not very efficient: it creates a new object 'digits_encoding' everytime and not appending
# # The following is more efficient way: List comprehension
# encoding = ''.join([map_string[d] for d in digits_encodings])
#


# import fractions
#
# a = fractions.Fraction(22,7)
# print(a)
# print(float(a))
# # print(help(fractions.Fraction))
# print(help(divmod))