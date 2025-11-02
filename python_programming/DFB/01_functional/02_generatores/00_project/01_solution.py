from collections import namedtuple, defaultdict
from datetime import datetime
from functools import partial

file_name = 'nyc_parking_tickets_extract.csv'

with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')

column_names = [header.replace(" ", "_").lower() for header in column_headers]

Ticket = namedtuple('Ticket', column_names)


def read_data():
    with open(file_name) as f:
        next(f)
        yield from f


def parse_int(value, *, default=None):
    try:
        return int(value)
    except:
        return default


def parse_date(value, *, default=None):
    data_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, data_format).date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        return cleaned
    except:
        return default


# Column parser

column_parser = (parse_int,
                 parse_string,
                 lambda x: parse_string(x, default=''),
                 partial(parse_string, default=''),
                 parse_date,
                 parse_int,
                 partial(parse_string, default=''),
                 parse_string,
                 lambda x: parse_string(x, default=''))


def parse_row(row, *, default=None):
    fields = row.strip().split(',')
    parse_data = [func(field)
                  for func, field in zip(column_parser, fields)]
    if all(item is not None for item in parse_data):
        return Ticket(*parse_data)
    else:
        return default


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed

#### Goal2

# Number of violation by car make

def violation_count_by_make():
    makes_count = defaultdict(int)
    for data in parsed_data():
        makes_count[data.vehicle_make] += 1

    return {make: count
            for make, count in sorted(makes_count.items(),
                                      key=lambda x: x[1],
                                      reverse=True)
            }

print(violation_count_by_make())



# makes_count = {}
#
# for data in parsed_data():
#     # print(data)
#     if data.vehicle_make in makes_count:
#         makes_count[data.vehicle_make] += 1
#     else:
#         makes_count[data.vehicle_make] = 1
# # sort
# sorted_makes_count = sorted(makes_count.items(),
#                             key=lambda x: x[1],
#                             reverse=True)
# for make, count in sorted(makes_count.items(),
#                           key=lambda x: x[1],
#                           reverse=True):
#     print(make, count)
# print(sorted_makes_count)

# other option using defaultdict
# from collections import defaultdict
#
# makes_count = defaultdict(int)
#
# for data in parsed_data():
#     makes_count[data.vehicle_make] += 1
#
# for make, count in sorted(makes_count.items(),
#                           key=lambda x: x[1],
#                           reverse=True):
#     print(make, count)

#