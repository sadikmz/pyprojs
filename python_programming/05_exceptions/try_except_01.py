try:
    fp = open("sample.txt")
except IOError as e:
    print("Unable to open the file: ", e)
