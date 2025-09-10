import glob

# *: matches zero or more characters
# ?: matches exactly one character

def search_file():
    identify_files = glob.glob("*l*.py")
    print(identify_files)


search_file()