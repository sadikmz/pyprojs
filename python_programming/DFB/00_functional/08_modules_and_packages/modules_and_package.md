Modules
- What are modules 
- How does python load modules
- How to import without import statement 
- Reload modules - why we should not do it. 
- Import variant 
- Misconceptions
- \_\_main__
- zip archives 
  - import from a zip archive
  - zipping an entire pyton app
  - creating an executable Python app in bash
- Packages 
  - What is a package
  - why use them
  - how is it different from module?
  - the role f \_\_init__.py files in packages 
Implicite Namespace Packagtes 
  - what are they
  - how do we create and use them
  - vs standard packages 
  
...........
Modules can be imported using 
- the import statement or 
- importlib.import_module 
When a module is imported:
- system cache is checked first sys.module. 
- if in caches, just returns cached reference
- otherwise, 
  - module has to be located (found) somewhere > finders eg. sys.meta_path
  - module code has to be retrieved (loaded) > loaders eg. returned by finders > ModuleSpec
  - "empty" module type object is created
  - a reference to the module is added to the system cache > sys.module 
  - module is compiled
  - module is executed > sets up teh module's namespace (module.\_\_dict__ is module.globals())
Module finder
  - sys.meta_path > _frozen_importlib.BuiltinImporter > finds built-ins, such as math
                  > _frozen_importlib.FrozenImporter > finds frozen modules 
                  > _frozen_importlib_external.PathFinder > file-based modules 
Path-finder
  - finds file-based modules based on sys.path and package \_\_path__
    - sys.path > eg of sys.path from 01_module.py
                  ['/Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming/DFB/00_functional/08_modules_and_packages', 
                  '/Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming', 
                  '/Library/Frameworks/Python.framework/Versions/3.13/lib/python313.zip', 
                  '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13', 
                  '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload', 
                  '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages']
    - collections.\_\_path__
                  ['/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/collections']
Module properties
    - built-in > eg. import math 
    - type(math) > module
    - math.\_\_spec__
              ModuleSpec(name='math', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x104ecccd0>, 
              origin='/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload/math.cpython-313-darwin.so')
    - math.\_\_name__ > math
    - math.\_\_package__ > ""
    - \_\_file__ is not an attribute of math (built-ins only)
    
    - standard library > eg. import fractions 
    - type(fractions) > module 
    - fractions.\_\_spec__
              ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x102d646b0>, 
              origin='/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/fractions.py')
    - fractions.\_\_name__ > fractions 
    - fractions.\_\_package__ > ""
    - fractions.\_\_file__
              /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/fractions.py
    - Note that fractions.\_\_file__ was found by Pathfinder in one of the paths listed in sys.path
    
    - custom module  > eg. import module1 
    - type(module) > module 
    - module1.\_\_spec__
              ModuleSpec(name='module1', loader=<_frozen_importlib_external.SourceFileLoader object at 0x1054c57f0>, 
              origin='/Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming/DFB/00_functional/08_modules_and_packages/03_exmaple/module1.py')
    - module1.\_\_name__ > module1 
    - module1.\_\_package__ > ""
    - module1.\_\_file__
              /Users/sadik/projects/github_prj/python_projects/pyprojs/python_programming/DFB/00_functional/08_modules_and_packages/03_exmaple/module1.py
    - Note that module.\_\_file__ was found by Pathfinder in one of the paths listed in sys.path

Some note:
- Python moduels may reside
  - in hte built-ins
  - in file on disk
  - they can even be pre-compiled, frozen, or even inside zip archives anywhere else that can be accessed by a finder and a loader
  - custom finders/loades can be developed to fetch and load data from > databases, https, etc
  - for file based modules (Pathfinder):
    - they must exist in path specified in sys.path
    - or in a path specified by <package>.__path__
References:
    - https://docs.python.org/3/tutorial/modules.html#
    - https://docs.python.org/3/reference/import.html#
    - PEP 302




