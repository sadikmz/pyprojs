# setup
# def gen(args):
#     # set up happens here, or inside try
#     try:
#         yield obj # whatever normally gets returned by __enter__
#     finally:
#         # Perform the clean up code here

def open_file(fname,mode):
    print('opening file.....')
    f = open(fname,mode)
    try:
        yield f
    finally:
        print('closing file.....')
        f.close()

class GenContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        print('calling next to get the yielded value from generator')
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing next to perform clean up in generator.....')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False

file_gen = open_file('test.txt','w')
with GenContextManager(file_gen) as f:
    f.writelines('Sir Spamalot')

# Create a decorator
def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

# open_file = context_manager_dec(open_file)
print('---------------------------')

# @context_manager_dec
# def open_file(fname,mode='r'):
#     print('opening file.....')
#     f = open(fname, mode)
#     try:
#         yield f
#     finally:
#         print('closing file.....')
#         f.close()
#
# with open_file('test.txt') as f:
#     print(f.readlines())

# using context manager decorator of the standard library
from contextlib import contextmanager
@contextmanager
def open_file(fname,mode='r'):
    print('opening file.....')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file.....')
        f.close()

with open_file('test.txt') as f:
    print(f.readlines())

# More examples
from time import perf_counter, sleep

@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['start'] = start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end'] = end
        stats['elapsed'] = end - start

with timer() as stats:
    sleep(2)

print(stats)

# Redirect stdout
import sys

@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout

with out_to_file('test.txt') as f:
    print('line 1')
    print('line 2')
print('line 3')

with open('test.txt', 'r') as f:
    print(f.readlines())

from contextlib import redirect_stdout

with open('test.txt', 'w') as f:
    with redirect_stdout(f):
        print('-----------------\n')
        print('Look on the bright side of life')
        print('line 2')
        print('line 3')

with open('test.txt', 'r') as f:
    print(f.readlines())
