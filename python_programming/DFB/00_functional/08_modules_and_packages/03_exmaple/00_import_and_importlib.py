import sys
print(sys)

import collections
print(collections)

#
mod_name = 'math'
import importlib
import importlib.util
print(importlib)

# importing mod_name
importlib.import_module(mod_name)

print('math' in sys.modules)
print('math' in globals())
print('fractions' in sys.modules)

# import math as math2
# math2 = sys.modules['math']
math2 = importlib.import_module(mod_name)
print('math2' in globals())


# mem location
print(id(math2))
print(id(sys.modules['math']))

# module importing mechanism
# finders
# loaders
# finder loader === importer

import math
import fractions

# How to build our own finder and loader function or module
# print(fractions.__spec__)
# print(dir(fractions))
#
# sys.meta_path contains the finder object
# print(sys.meta_path)
import math
print(math.__spec__)

# using importlib
print(importlib.util.find_spec('decimal'))
print(dir(importlib))

# creating a module file

# with open('module1.py', 'w') as code_file:
#     code_file.write("print('Running module1.py')\n")
#     code_file.write("a=100")

print(importlib.util.find_spec('module1'))

import module1
print('module1' in globals())
# 'module2' in sys.modules

import os
# ext_module_path = os.environ.get('/Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming/')
# ext_module_path = os.environ['/Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming/']
ext_module_path= os.path.abspath('/Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming')
print(ext_module_path)
file_abs_path = os.path.join(ext_module_path, 'module2.py')

with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write('x = "python"\n')

print(importlib.util.find_spec('module2'))

print(sys.path)

# append the path to module to sys.module
sys.path.append(ext_module_path)
print(importlib.util.find_spec('module2'))
import module2
print(module2.x)

print(".......note")
print(module1.__spec__)
print(module1.__name__)
# print(module2.__package__)
print(module1.__file__)
