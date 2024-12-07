from reading_file.read_bad_name import count

name = input("Enter file: ")
handle = open(name)

counts = dict()
for line in handle:
    words = line.rsplit()
    for word in words:
        count[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)