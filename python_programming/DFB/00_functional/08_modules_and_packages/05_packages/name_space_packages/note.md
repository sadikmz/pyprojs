**What are implicit Namespace Packages**
- Namespace packages are package-line direcotires
  - may contain modules 
  - may contain nested regular packages
  - may contain namespace packates
  - but cannot contain \_\_init__.py
- These directories are implicitly made into three special types of packages 
- PEP 420 for details


**Mechanics**

utils/                      ---> utils/ does not contain __init__.py ---> namespace package
    validators/             ---> validators/ does not contain __init__.py ---> namespace package
        boolean.py          ---> boolean.py is a file with a .py extension ---> a module
        date.py             
        json/               ---> json/ contains __init__.py ---> regular package
            __init__.py
            serializers.py  ---> serializers is a file with .py extension ---> module
            validators.py

**Regular vs Namespace packages**

|  Description  |                         Regular packages                          | Namespace packages
|:-------------:|:-----------------------------------------------------------------:| :--: |
|     type      |                              module                               | module 
| \_\_init__.py |                                yes                                | no
| \_\_file__.py |                         package \_\_initt                         | not set
| path | breaks if parent directories change and absolute imports are used | dynamic path computaiton so OK if parent directories change. (Your import statement will still need to be changed) |
| | single packages lives in single directory | Single packages can live in multiple (non-listed) directories. In fact, part of the namespace may even be in a zip file. |

**Example: import**

utils/             
    validators/         
        boolean.py              -----> import utili.validators.boolean
        date.py                 -----> import utili.validators.date
        json/  
            __init__.py
            serializers.py      -----> import utili.json.serializers
            validators.py


**Importing from Zip archives** 

- append the zipepd packages into sys.path 
  - eg. import sys
    - sys.path.append("rel_path_to_zipped_pack")