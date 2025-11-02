def my_gene():
    try:
        print('Creating context and yielding object')
        yield (1,2,3,4)
    finally:
        print('Exiting context and cleaning up')
#
# gen = my_gene()
#
# lst = next(gen)
# print(lst)
# print(next(gen))

# gen = my_gene()
# lst = next(gen)
# print(list)
# try:
#     next(gen)
# except StopIteration:
#     pass

class GenContextManager:
    def __init__(self, gen_func):
        self._gen = gen_func()

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def my_gen():
    try:
        print('Creating context and yielding object')
        yield (1,2,3,4)
    finally:
        print('Exiting context and cleaning up')

with GenContextManager(my_gen) as gen:
    print(gen)

# custom file opening generator - context manager

class GenCxtManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def open_file(fname,mode):
    f = open(fname,mode)
    try:
        print('Opening file....')
        yield f
    finally:
        print('Closing file....')
        f.close()

with GenCxtManager(open_file, 'text.txt', 'w') as f:
    f.writelines('testing...')

with GenCxtManager(open_file, 'text.txt', 'r') as f:
    print(f.readlines())