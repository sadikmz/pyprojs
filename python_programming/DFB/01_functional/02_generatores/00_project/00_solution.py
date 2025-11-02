#### Goal1

file_name = 'nyc_parking_tickets_extract.csv'

# with open(file_name) as f:
#     for _ in range(10):
#         print(next(f))


with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')
print(column_headers)
print(sample_data)

column_names = [header.replace(" ","_").lower() for header in column_headers]
print(column_headers)
print(list(zip(column_headers, sample_data)))

# create namedtuple

from collections import namedtuple
Ticket = namedtuple('Ticket', column_names)

with open(file_name) as f:
    next(f)
    raw_data_row = next(f)

print(raw_data_row)

def read_data():
    with open(file_name) as f:
        next(f)
        yield from f

raw_data = read_data()
for _ in range(5):
    print(next(raw_data))

def parse_int(value, *, default=None):
    try:
        return int(value)
    except:
        return default

# print(parse_int('test', default='Not an integer'))

from datetime import datetime

def parse_date(value, *, default=None):
    data_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, data_format).date()
    except ValueError:
        return default

# print(parse_int('hello', default='N/A'))
print(parse_date('01/01/2022'))

def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        return cleaned
    except:
        return default

print(parse_string('   hello world   '))

# Column parser

from functools import partial

column_parser = (parse_int,
                 parse_string,
                 lambda x: parse_string(x,default=''),
                 partial(parse_string,default=''),
                 parse_date,
                 parse_int,
                 partial(parse_string,default=''),
                 parse_string,
                 lambda x: parse_string(x,default=''))


def parse_row(row):
    fields = row.strip().split(',')
    parse_data = (func(field)
                  for func, field in zip(column_parser, fields))
    return parse_data

rows = read_data()

for _ in range(5):
    row = next(rows)
    parse_data = parse_row(row)
    print(list(parse_data))

# help(all)

# print(all([10,0,""]))
# print(all([10,0]))
# print(all([10,"hello world"]))
# print(all([10,None]))

# using all
l = [10,'',0,None]
print(all(item is not None for item in l))

# Modifying parse_row
def parse_row(row,*,default=None):
    fields = row.strip().split(',')
    parse_data = [func(field)
                  for func, field in zip(column_parser, fields)]
    if all(item is not None for item in parse_data):
        return Ticket(*parse_data)
    else:
        return default
    # return parse_data

#
# rows = read_data()
# for _ in range(5):
#     row = next(rows)
#     parse_data = parse_row(row)
#     print(parse_data)

for row in read_data():
    parsed_row = parse_row(row)
    if parsed_row is None:
        print(list(zip(column_names,row.strip('\n').split(','))), end='\n\n')
    # print(parse_data)


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

parsed_rows = parsed_data()

for _ in range(5):
    print(next(parsed_rows))