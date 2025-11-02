# try:
#     10 / 2
# except ZeroDivisionError:
#     print('Zero division exception occurred')
# finally:
#     print('Finally run!')
#
#
# try:
#     10 / 0
# except ZeroDivisionError:
#     print('Zero division exception occurred')
# finally:
#     print('Finally run!')

def my_func():
    try:
        10 / 0
    except ZeroDivisionError:
        return
        # print('Zero division exception occurred')
    finally:
        print('Finally run!')

my_func()


try:
    print('Opening file ..')
    f = open('text.txt', 'w')
    a = 1 / 0
except:
    print('An exception occurred')
finally:
    print('Closing file ..')
    f.close()

# Context managers: enter and exit methods
# Enter methods: __enter__
# Exit methods: __exit__
#     - Closing file

# with open('test.txt', 'w') as file:
#     print('Inside: file close?', file.closed)
# print('After with: file close?', file.closed)

# def test():
#     with open('test.txt', 'w') as file:
#         print('Inside: file close?', file.closed)
#         return file
#     print('Here - will never run')

# file = test()

# with open('test.txt', 'w') as file:
#     print('Inside: file close?', file.closed)
#     raise ValueError

with open('test.txt', 'w') as f:
    f.writelines('this is a test')

with open('test.txt') as f:
    row = next(f)

print(f.closed)
print(row)

# Our own context manager

class MyContext:
    def __init__(self):
        self.obj = None

    def __enter__(self):
        print('Entering context...')
        self.obj = 'the Return object'
        return self.obj

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Exiting context...')
        if exc_type:
            print(f'*** Error occurred: {exc_type}, {exc_value}')
        return True

ctx = MyContext()
print('created context...')
with ctx as obj:
    print('inside context block', obj)
    raise ValueError('custom message')
# with MyContext() as obj:
#     print('Inside with block')
#     raise ValueError('custom message')

print('*************')
class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resources = None

    def __enter__(self):
        print('Entering context...')
        self.resources = Resource(self.name)
        self.resources.state = 'created'
        return self.resources

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Exiting context...')
        self.resources.state = 'destroyed'
        if exc_type:
            print('error occurred')
        return False

with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')

print(f'{res.name} = {res.state}')


class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('Opening file ...')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Closing file ...')
        self.file.close()
        return False

with File('test.txt', 'w') as f:
    f.write('this is a late parrot')

with File('test.txt', 'r') as f:
    print(f.readlines())

def test():
    with File('test.txt', 'w') as f:
            f.write('this is a late parrot')
            raise ValueError
# f = test()

#
class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('Opening file ...')
        self.file = open(self.name, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Closing file ...')
        self.file.close()
        return False

with File('test.txt', 'r') as file_ctx:
    print(next(file_ctx.file))
    print(file_ctx.name)
    print(file_ctx.mode)