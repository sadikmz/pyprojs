import csv

# def read_data():
#     with open('nyc_parking_tickets_extract.csv') as f:
#         return csv.reader(f, delimiter=',', quotechar='"')

# solution 1
def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        yield from csv.reader(f, delimiter=',', quotechar='"')

# yield from: iterates until finishing the iteration

reader = read_data()
print(type(reader))

for row in reader:
    print(row)

# solution 2:
print('\n\n')
print('-------solution #2--------')
def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        return list(csv.reader(f, delimiter=',', quotechar='"')) # loads data into memory
reader = read_data()
for row in reader:
    print(row)