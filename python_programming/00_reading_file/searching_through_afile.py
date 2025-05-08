fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rsplit()
    if line.startswith("From:"):
        print(line)