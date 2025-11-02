**Packages are modules** 

- Packages are modules but modules are not necessarily packages 
- they can contain
  - modules 
  - packages (also called sub-packages) 
- if a module is a package, it must have a value set for __path__
- After you've imported a module, you can easily see if that module is a package by inspecting the __path__ attribute (empty --> module, non-empty --> package)

**Packages vs File systems** 

- Remember that modules do not have to be entities in a file system (loaders, finders)
- By the same token, packages do not have to be entities in the files system 
- Typically they are - just as typically modules are file system entities 
- But packages represent a hierarchy of modules / packages 
  - pack1.mod1
  - pack1.pack1_1.mod_1
  - dotted notation indicates the path hierarchy of modules / packages 
  - and is usually found in __path__

**Importing nested packages**

- If you've a statement in your top-level program such as import pack1.pack1_1.module_1
- the import system will perform
  - import pack1
  - import pack1.pack1_1
  - import pack1.pack1_1.module1
- The sys.module cache will contain entries for 
  - pack1
  - pack1.pack1_1
  - pack1.pack1_1.module1
- The namespace where the import was run contains: pack1
- Although modules and packages can be far more generic than file system based entities, it gest complicated.
- Look at PEP 302 for detail 

**File based packages** 

- Packages path are created by using file system directories and files
- Remember: a package is simply a module that can contain other modules / packages 
- On a file system we therefore have to use directories for packages
- The directory name becomes the package name
- So where does the code goes for the package (since it is a module) \_\_init__.py

**\_\_init__py**

- To define a package in out file system, we must:
  - create a directory whose name will be the package name
  - create a \_\_init__.py inside that directory 
- That \_\_init__.py file is what tells python that the directory is a package as opposed to a standard directory
- (if we don't have and \_\_init__.py file, then python creates an implicit namespace package)

**What happens when a file-based package is imported?**

- app/
  - /pack1
    - \_\_init__.py
    - module1.py
    - module2.py
- import pack1
  - the code for pack1 is in \_\_init__.py
  - that code is loaded, executed and cached in sys.modules with a key of pack1 - just a module 
  - The symbol pack1 is added to out namespace referencing the same object - just a module 
  - but, it has a \_\_path__ property --> file system directory path (absolute)
  - also has a \_\_file__ property --> a path to \_\_init__.py (absolute)

**Nested packages**

- packages can contain modules as well as packages 
- app\
  - pack1\               ------------> pack1
    - \_\_init__.py
    - module1a.py        ------------> pack1.module1
    - module1b.py
    - pack1_1            ------------> pack1.pack1_1
      - \_\_init__.py
      - module1_1a.py    ------------> pack1.pack1_1.module1_1a
      - module1_1b.py

**\_\_file__, \_\_path__, and \_\_package__ properties**

- modules have \_\_file__ and \_\_package__ properties
- \_\_file__ is the location of module code in the file system 
- \_\_package__ is the package the module is located in (an empty string if the module is located in the application root)
- if the module is a package, then it also has a \_\_path__ properties
- \_\_path__ is the location of the package (directly) in the file system

**Why packages**

- Example: api package
- api/
  - api.py
  - dbutilities.py
  - jsonutilities.py
  - typeconversions.py
  - validations.py
  - authentitications.py
  - authorizations.py
  - users.py
  - blogposts.py
  - logging.py
  - unittests.py

- to import them
  - import dbutilities
  - import jsonutilities
  - import typeconversion 
  - import validations
  - ....
  - Certain modules can be broken down further:
    - dbutilities --> connections, queries 
    - users ---> User, Users, UserProfile
  - Certain modules belong together 
    - authentication, authorization ----> security
  

  
  - api/
    - utilities/
      - \_\_init__.py
      - connection.py
      - queries.py
    - security
      - \_\_init__.py
      - authentication.py
      - authorization.py
    - models
      - \_\_init__.py
      - users/
        - \_\_init__.py
        - user.py
        - userprofile.py

**Another use case**

- You have a module that implements 2 functions / classes for users of the module
- Those two objects require 20 different helper functions and 2 addtional helps classes 
- from module developer's perspective 
  - much easier to break the code down into multiple modules 
- from module user's perspective
  - They just want a single import for the function and the class

**Module user's perspective**

- mylib/
  - \_\_init__.py
  - submod1.py       ------------> function to be exported to users lives here.
  - submod2.py
  - subpack1
    - \_\_init__.py
    - pack1mod1.py
    - pack1mod2.py  --------------> functions classes to be exported to user lives here.

- Users should not have to write:
  - from mylib.submod1 import my_func
  - from mylib.subpack1.pack1mod2 import MyClass
- Much easier for users if they could write 
  - from mylib import my_func, MyClass
  - import mylib
  - then mylib.my_func(), mylib.MyClass()
- Using __init__.py 
  - We can use packages's __init__.py code to export (expose) just what's needed by our users 
  - Example
    - mylib/
    - \_\_init__.py
    - submod1.py       ------------> function to be exported to users lives here.
    - submod2.py
    - subpack1
      - \_\_init__.py
      - pack1mod1.py
      - pack1mod2.py  -------------->
  - under __init__.py add 
    - from mylib.submod1 import my_func 
    - from mylib.subpack1.pack1mod2 import MyClass
  - User use it this way:
    - import mylib
      - mylib.my_func()
      - mylib.My_Class()
    - our internal implementation is hidden

- So, why packages
  - ability to break codes up to smaller chunks, makes our code:
    - easier to write
    - easier to test and debug
    - easier to read/understand
    - easier to document 
    - but they can still be stitched together 
      - hides implementation from users