# Methods and properties of open object
# readlines
# closed
# close

# handling exception while the file is open
# Option 1
f = open('file_path', 'w')
try:
    # write to file
finally:
    f.close()

# Option2
with open('file_path', 'w') as f:
    # write to file
