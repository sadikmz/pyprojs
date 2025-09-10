import os


def top_down():
    for dirpath, dirnames, files, in os.walk("."):
        print("Directory: ", dirpath)
        print("------Includes these directories------")
        for dirname in dirnames:
            print(dirname)
        print("------Includes these files------")
        for filename in files:
            print(filename)
        print()

top_down()