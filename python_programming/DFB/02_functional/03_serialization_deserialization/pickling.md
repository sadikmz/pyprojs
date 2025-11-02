**The pickle module**
- Python specific 
- A way to represent an object in a persistent way ----> disk, transimission 
  - create an objects's representation -> serializing 
  - reload object from representation  -=> deserializing 
    - both called data marshalling 
      - Obj ---serialization--->0001010100101...---deserialization---->obj
- pickle is a binary serialization (by default)
- focus on dictionaries 

*Danger zone*
- Unpickling (deserializing) can execute code
  - note safe

*Usage*
```
import pickle 
dump --> pickle to file 
load --> unpickle from a file 
dumps --> returns a (string) pickled representation ---> store in a varialble 
loads --> 
```

*Equality and identity*
- equality -> == 
- identity -> is
```aiignore
dict1 ---pickle--->010101010-----unpickle---->dict2
id=100                                      id=200

dict1 == dict2 True --> Custom object will need to implement __eq__ method
dict1 is dict2 False
```
- while pickling, Python will not re-serialize on object it has already serialized 
  - recursive objects can be pickled
  - shared objects are deserialized as shared object as well