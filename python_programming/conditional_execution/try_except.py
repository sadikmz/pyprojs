# traceback error - it is not defined.
astr = "Hello Bob"
try:
     istr = int(astr)
except:
     istr = -1
print("First", istr)

astr = "1234"
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)