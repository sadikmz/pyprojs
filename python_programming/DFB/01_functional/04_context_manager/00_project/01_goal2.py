import csv
from itertools import islice
from contextlib import contextmanager

f_names = 'cars.csv', 'personal_info.csv'



from collections import namedtuple

# A named tuple for each row
class FileParser:
    def __init__(self, f_name):
        self.f_name = f_name

    def __enter__(self):
        self._f = open(self.f_name, 'r')
        self._reader = csv.reader(self._f, get_dialect(self.f_name))
        headers = map(lambda s: s.lower(), next(self._reader))
        self._nt = namedtuple('Data', headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._reader))

# with FileParser('cars.csv') as data:
#     for row in islice(data, 10):
#         print(row)
#
# with FileParser('personal_info.csv') as data:
#     for row in islice(data, 10):
#         print(row)

# iterator



# Write context manager
@contextmanager
def parsed_data(f_name):

    # def get_dialect():
    #     with open(f_name) as f:
    #         return csv.Sniffer().sniff(f.read(1000))

    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        f.seek(0)
        reader = csv.reader(f, dialect)
        header = map(lambda s: s.lower(), next(reader))
        nt = namedtuple('Data', header)
        yield (nt(*row) for row in reader)
    finally:
        f.close()


# try it out

with parsed_data('personal_info.csv') as data:
    for row in islice(data, 10):
        print(row)
