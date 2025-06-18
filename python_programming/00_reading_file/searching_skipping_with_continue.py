fhand = open("python_programming/code3/code3/mbox-short.txt")
for line in fhand:
    line = line.rsplit()
    if not '@uct.ac.za' in line:
        continue
    print(line)