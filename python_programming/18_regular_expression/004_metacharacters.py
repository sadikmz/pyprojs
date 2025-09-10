import re
# s = 'Hi \nhow are you'
# print (s)
#
# sraw =r'Hi \nhow are you?'
# print(sraw)

# phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phone_num_regex.search("This is my number: 555-444-7777")
# print(mo.group())

# Creating group

# phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
# mo = phone_num_regex.search("This is my number: 555-444-7777")
# print(mo.group(0))

# 555 444-7777
# scapping
# phone_num_regex = re.compile(r"\(\d\d\d\) (\d\d\d-\d\d\d\d)")
# mo = phone_num_regex.search("This is my number: (555) 444-7777")
# print(mo.group(1))

# Pipe character

dis_regex = re.compile(r'dis(agree|allow|array|connect)')
text = "I disagree with the following statement. disconnect and disallow"
print(dis_regex.search(text))