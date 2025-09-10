from re import findall


def is_phone_number(p_string):
    if len (p_string) != 12:
        # Not phone number
        return False
    for i in range(0,3):
        if not p_string[i].isdecimal():
            # Area code is missing
            return False
    if p_string[3] !="-":
        # Missing first dash
        return False
    for i in range(4,7):
        if not p_string[i].isdecimal():
            # Missing first digit
            return False
    if p_string[7] != "-":
        # Missing second dash
        return False
    for i in range(8,12):
        if not p_string[i].isdecimal():
            # Missing second value
            return False
    return True

# print(is_phone_number("12a-123-8888"))
text = "This is my number: 555-333-4444 and the office is 666-777-8888"
is_pnumber = False
for i in range(len(text)):
    text_piece = text[i:i+12]
    if is_phone_number(text_piece):
        print(f"Phone number is found: {text_piece}")
        is_pnumber = True
if not is_pnumber:
    print(f"There is not any number")

# Using regular expression
import re

mo = re.search('\d+',text)
if mo == None:
    print(f"There is not any number")
else:
    print(mo.group())
print(mo.group())

mo = re.findall("\d\d\d-\d\d\d-\d\d\d\d",text)
print(mo)