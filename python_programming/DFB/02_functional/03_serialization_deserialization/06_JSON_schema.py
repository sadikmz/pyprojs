person_schema = {
    "type": "object",
    "properties": {
        "firstName": {"type": "string",
                      "minLength": 1
                      },
        "middleName": {"type": "string",
                       "minLength": 1,
                       "maxLength": 1
                        },
        "lastName": {"type": "string",
                     "minLength": 1
                     },
        "age": {"type": "number",
                "minimum": 0
                },
        "eyeColor": {"type": "string",
                     "enum": ["amber","blue","brown","gray",
                              "green","hazel","red","violet"]
                     }
    },
    "required": ["firstName", "lastName"]
}

p1 = '''
{
    "firstName": "John",
    "middleName": "M",
    "lastName": "Doe",
    "age": 22
}
'''

p2 ='''
{
    "firstName": "John",
    "middleName": 100,
    "lastName": "Doe",
    "age": "Unknown"   
}
'''

'''
pip install jsonschema
'''

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError

json_doc = p2

print(json_doc)

try:
    validate(loads(json_doc), person_schema)
except JSONDecodeError as e:
    print(f'Invalid JSON : {e}')
except ValidationError as e:
    print(f'Validation Error: {e}')
else:
    print('JSON is valid and conforms to schema')


from jsonschema import Draft4Validator
validator = Draft4Validator(person_schema)

json_doc = p2

for error in validator.iter_errors(loads(json_doc)):
    print(error,end='\n--------------------------------\n')

p4 = '''
{
    "firstName": "John",
    "middleName": null,
    "lastName": "Doe",
    "eyeColor": "blue-gray"
}
'''

json_doc = p4

print('-------new----')
for error in validator.iter_errors(loads(json_doc)):
    print(error,end='\n--------------------------------\n')


#
p4 = '''
{
    "firstName": "John",
    "lastName": "Doe",
    "eyeColor": "blue"
}
'''

json_doc = p4

for error in validator.iter_errors(loads(json_doc)):
    print(error,end='\n--------------------------------\n')