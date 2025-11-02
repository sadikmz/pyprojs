# Parsing CSV data
# Default parse dialect is excel but we can specify custom setting for delimiter and quotechar, etc
import csv

# csv.reader(f, delimiter=',', quotechar='"')
#
# # returns an iterator of parsed rows over the file
# with open('file_path', 'w') as f:
#     reader = csv.reader(f, delimiter=',', quotechar='"')
#     for row in reader:
#         # do this and that

# Dialect
print(csv.list_dialects())
# with open('file_path', 'w') as f:
#     reader = csv.reader(
#         f,
#         delimiter=',',
#         quotechar='|',
#         escapechar="\\",
#         skipinitialspace=True,
#     )
#     for row in reader:
#         print(row)

# Register dialect
csv.register_dialect(
    "pdv",
    delimiter=',',
    quotechar='|',
    escapechar="\\",
    skipinitialspace=True
)

print(csv.list_dialects())


with open('file_path', 'w') as f:
    reader = csv.reader(
        f,dialect='pdv'
    )
    for row in reader:
        print(row)

# Writing CSV file

with open('file_path', 'w') as f:
    writer = csv.writer(f, dialect='...')
    for row in data:
        writer.writerow(row)
