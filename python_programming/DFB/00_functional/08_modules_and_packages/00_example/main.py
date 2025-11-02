import sys


print('==========================================')
print('Running main.py - module name: {0}'.format(__name__))

import module_00

# print(module_00)

# module_00.pprint_dict('main.globals',globals())

print(sys.path)

print(sys.modules['module_00'])

# removing the module from the global namespace

# del globals()['module_00']

print('=====================================')

# print(dir(module_00))