**JSON**
- JavaScript Object Notation
  - text-based object serialization
  - open standard
  - human-readable 
- very common format for web API's and general data interchange between system 
- unlike pickling, it is considered safe
  - may vary based on teh JSON deserializer used 
- Limited data type
```aiignore
string  "python"    delimited_by_double_quotes  unicode
numbers 100 3.14 3.14e-05 3.14E+5   --> all floats
boolean true, false
array(lists) [1,3.1,"pthon"] delimted_by_brackets ordered
dictionaries    {"a": 1, "b":"python"} key-value_paris, unordered
empty_value     null

#non-standard, additional types:
integers    100
floats  3.14 100.0 NaN Infinity -Infinity
```
Example:
```aiignore

```

*Serialization and Deserialization*
- JSON is a natural fit for serializing and deserializing Python dicitonaries
- Python dictionaries are objects
- JSON is essentially a string
```aiignore
import json     dump,dumps
                load, loads
                
       serialize                   deserialize
dict -------------->{           }--------------->dict 
       dump,dumps    file string   load,loads
```
Problems
- JSON keys must be string
  - Python dictionary keys just need to be hashable
  - how to serialize 
- JSON keys must be string
  - Python dictionary values van be any data type
  - how to serialize
- Even if we can serialize a complex data types, such as a custom data, 
  - how do we deserialize back to the original type?

**Custom encoding**
- Any object can be serialized to JSON
  - cumbersome to call teh JSON serializer for every class
  - how do we do it for nested dictionaries and lists
  - dump, dumps
    - can provide custom callable 
    - uses a default instance of JSONEncoder 

**Specifying a custom encoding function**
- one of the arguments of the dump/dumps function is *default* 
  - when provided, python will call *default* if it encounters a type it cannot serialize
  - argument must have be a callable 
    - callable must have a single argument 
    - that argument will receive the object python cannot serialize 
    - can include logic in our callable to differentiate between different types
      - or we can use a single dispatch generic function 
        - [use the @singledispatch decorator from the functools module]

**Using JSONEncoder - dump**
- beyond the *default* argument, *dump* has many other arguments that allow us to control serialization
```aiignore
skipkeys    bool    default is false    --> If dictionary keys are not basic types 
                                            (string, int, etc) and skipkeys is set to False
                                            we will get a TypeError, otherwise it just skips the key.

indent      int    default is None      --> useful for human redability

separators tuple  defaults to (' , ', ',: ') -> customizes how the JSON is rendered

sort_keys  boolean  default is False    --> if True, dictionary keys will be sorted
and more ... cls  
```
*The JSONEncoder Class*
- Python uses an instance of the JSONEncoder class in the json module to serializer data
- The JSONEncoder class shares many arguments with the *dump/dumps* functions
  - defaults
  - skipkeys
  - sort_keys
  - indent
  - separator, ...
- The *dump/dumps* functions have a *cls* argument 
  - allows to specify our own version of JSONEncoder

*Why use JSONEncoder at all?*
- If dump has all same arguments as JSONEncoder, why use it all?
  - to remain consistent in our app, every time we call dump we need to use the same argument vaues
  - easy to make a mistake, or forget to specify an argument
    - instead use a custom class JSONEncoder 
    - and just remember to specify it visa the *cls* argument of dump/dumps

*How to create a custom JSONEncoder*
- subclass JSONEncoder 
- custom initialize parent class if we want to
- override the default method
  - handle what we want to handle ourselves 
  - otherwise delegate back to the parent class

```aiignore
class CustomeEncoder(JSONEncoder):                              # inherit from JSONEncoder 
    def __init__(self):
        super().__init__(skipkeys=True, allow_nan==False        # custom init parent
                        indent=='--', separators=('',' = ')     
    def default(self, arg):
        if isinstance(arg,datetime):                            # override default method
            return arg.isoformat()                              # handle what we want to handle (return the string serialization of arg)
        else:                                                   
            return super().default(self, arg)
```

**Custom JSON Decoding**
- We have seen how to serialize Python objects to JSON
- Now we need to look at deserializing JSON to python objects ---> load, loads
```aiignore
import json
j = '{"a": a, "b": {"sub1": [2,3]}}'
d = json.loads(j)   d --->{
                            "a": a, 
                            "b": {"sub1": [2,3]
                                  }
                            
                            } 

```
- works out-of-the-box with the standard JSON data types --> numbers, booleans, lists, dictionaries (key:value pairs)
- does not work with other types
```aiignore
j = '{"createAt": "2020-12-31T23:59:59"}'
            ---> interpreted as a string
```

*One approach*
- Use some custom encoding scheme to define both the value and the type of some entry in the JSON file.
- For example, when encoding a timestamp, we could do it as follows:
```aiignore
j = '''
    { "createdAt": 
        {   "objecttype": "isodatetime"
            "value": "2020-12-31T23:59:59"
        }
    } 
'''
```
- load the json string into a Python dictionary 
  - iterate through dictionary (recursively), to find objects with an objecttype==isodatetime
    - replace createAt with the converted timestamp
- tedious 
  - load JSON
  - iterate recursively through dictionary, and
  - convert as needed

*A slight improvement*
- *load* and *loads* have an argument named *object_hook*
  - loads(j_stirng, object_hook=my_func)
    - my_func is called for every object in the JSON
- for example
```aiignore
j = '''                               ---> loads first parses JSON into a dictionary
    { "a":1,                          ---> object_hook will call for every dictionary (object) in the dictionary
      "b": {                                --> b dictionary
            "sub1": [1,2,3],
            "sub2": {                       --> sub2 dictionary 
                "x": 100,
                "y": 200                    --> root dictionary (callled last)
            }                               --> dictionary is replaced by return
        }                                       value of my_func
    } 
'''
```
*Schema*
- Deserializing custom JSON types and object is difficult 
  - in general we need to know the structure of the JSOn data in order to custom deserilize 
  - this is referred to as the schema
    - pre-defined agreement on how the JSON is going to be structured or serilzied
  - If JSON has a pre-determined schem, then we can handle custom deserialization
  - schema might be for the entire JSON, or for sub-components only 
```aiignore
    { "createdAt": 
        {   "objecttype": "isodatetime"     ---> if we see objectype, replace the dict with the 
            "value": "2020-12-31T23:59:59"       custom object / value
        }
    } 
```
*Overriding basic type serializations*
- Notice that object-hook only allows us to customize deserialization of objects
- what about numbers? --> by default floats for real numbers, and ints for whole numbers
- what if we want Decimal instead of float? or binary representations for integers?
- we can override the way these data types are handled by using some extra arguments in *load/loads* 
  - parse_float ----> provide a custom callable 
  - parse_int  -----> callable has a single argument 
  - parse_constant --> argument value will be the original string in the JSON

*Another argument: obejct_pairs_hook*
- related to object_hook
- cannot use both at the same time (if both are specified, the object_hook is ignored)
  - object_hook passes the deserialized dictionary to the callable
    - there is no guarantee of the order of elements in the dictionary 
  - What if orders of elements in the JSON is important ---> list preserve order
    - instead of callable receiving a dictionary it receives a list of the key/value pairs
    - key/value paris are provided as a tuple with two elements 

*Mixing basic types override and object hooks*
- can specify both parse_... and object_hook
- Remember that object_hook (and object_pairs_hook) callables receive a parsed object
- this means ....(if specified) is used first, before we receive the parsed object in the hooks.

**Using JSONDecoder class**
- working with the serialization, we could use dump, or JSONEncoder
- similarly, we can create a custom JSONDecoder class and specify it with the cls argument 
  - json.loads(j, cls=CustomDecoder )
- Just a different way of doing it -> it might help making sure we use our custom decoder consistent
- works differently than JSONEncoder
  - inherit from JSONDecoder
  - override the decode function
  - decode function receives entire JSON string 
  - we have to fully parse and return whatever object we want 