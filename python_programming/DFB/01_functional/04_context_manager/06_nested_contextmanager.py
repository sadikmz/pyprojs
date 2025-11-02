# with open('file1.txt') as f1, open('file2.txt') as f2:
#     print(f1.readlines())
#     print(f2.readlines())
#
# with open('file1.txt') as f1:
#     with open('file2.txt') as f2:
#         with open('file3.txt') as f3:
#             print(f1.readlines())
#             print(f2.readlines())
#             print(f3.readlines())

from contextlib import contextmanager
@contextmanager
def open_file(fname):
    print(f'opening {fname}')
    f = open(fname)
    try:
        yield f
    finally:
        print(f'closing {fname}')
        f.close()

# fnames = 'file1.txt', 'file2.txt', 'file3.txt'
#
# # Creating the context managers
# exits = []
# enters = []
#
# for f_name in fnames:
#     ctx = open_file(f_name)
#     enters.append(ctx.__enter__)
#     exits.append(ctx.__exit__)
#
# # Entering the context managers
# files = [enter() for enter in enters]
#
# while True:
#     try:
#         rows = [next(f).strip('\n') for f in files]
#     except StopIteration:
#         break
#     else:
#         row = ','.join(rows)
#         print(row)

# Exit context manager
# for exit in exits[::-1]:
#     exit(None, None, None)

#
class NestedContexts:
    def __init__(self,*contexts):
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in contexts:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_val, exc_tb)
        return False

with NestedContexts(open_file('file1.txt'),
                    open_file('file2.txt'),
                    open_file('file3.txt')) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)

print('------reifne------')
# Refine

class NestedContexts:
    def __init__(self,*contexts):
        self._exits = []

    def __enter__(self):
        return self

    def enter_context(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_val, exc_tb)
        return False
#
# f_names = 'file1.txt', 'file2.txt', 'file3.txt'
#
# with NestedContexts() as stack:
#     files = [stack.enter_context(open_file(f)) for f in f_names]
#     # print(list(files))
#     print('do work')

from contextlib import ExitStack

f_names = 'file1.txt', 'file2.txt', 'file3.txt'

with ExitStack() as stack:
    files = [stack.enter_context(open_file(f)) for f in f_names]
    # print('do the work')
    # print(files)
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ','.join(rows)
            print(row)



