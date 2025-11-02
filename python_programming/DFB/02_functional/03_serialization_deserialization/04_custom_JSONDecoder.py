import json
j = '''
{
"name": "Python",
"age": 27,
"version": ["2.x", "3.x"]

}


'''

print(json.loads(j))

# other data type - date

p = '''
{
"time": "2018-10-21T09:30:00",
"message": "created this jons string"
}

'''

print(json.loads(p))

p = '''
{
"time": {
    "objecttype": "datetime",
    "value": "2018-10-21T09:30:00"
    },
"message": "created this jons string"
}

'''
d = json.loads(p)
print(d)
from pprint import pprint
pprint(d)

from datetime import datetime

for key, value in d.items():
    if(isinstance(value, dict) and
    'objecttype' in value and
    value['objecttype'] == 'datetime'):
        d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

print(d)

j = '''
{
    "cake": "yummy chocolate cake",
    "myShare": {
        "objecttype": "fraction",
        "numerator": 1,
        "denominator": 8
    }
}
'''
d = json.loads(j)
print(d)

from fractions import Fraction

for key, value in d.items():
    if(isinstance(value, dict) and
    'objecttype' in value and
    value['objecttype'] == 'fraction'):
        numerator = value['numerator']
        denominator = value['denominator']
        d[key] = Fraction(numerator, denominator)
print(d)

# Alternative option using arguments in load and loads - such as object_hook

# write a dummy decoder
def custom_decoder(arg):
    print('decoding,: ', arg, type(arg))
    return arg

j = '''
{
    "a": 1,
    "b": 2,
    "c": {
        "c.1": 1, 
        "c.2": 2, 
        "c.3": {
            "c.3.1": 1, 
            "c.3.2": 2 
        }
    }
}
'''

d = json.loads(j, object_hook=custom_decoder)
print(d)

# working with the datetime decoder

j = '''
    {
        "time": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:30:00"
            },
        "message": "created this jons string"
    }
'''

def custom_decoder(arg):
    # print(arg)
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg

# print(custom_decoder(dict(objecttype='datetime', value='2018-10-21T09:30:00')))
# print(custom_decoder({'a':1}))
print(json.loads(j, object_hook=custom_decoder))

# more with json containing nested dictionary
j = '''
    {
        "times": {
            "created": {
                "objecttype": "datetime",
                "value": "2018-10-21T09:14:15"
                },
            "updated": {
                "objecttype": "datetime",
                "value": "2018-10-22T10:00:05"
                }
            },
        "message": "log message here..."
    }
'''

j_dec = json.loads(j, object_hook=custom_decoder)
print(j_dec)

# custom decoder

def custom_decoder(arg):
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            return Fraction(arg['numerator'], arg['denominator'])
        return arg
    return  arg

# new json
j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        },
        "eaten": {
            "at": {
                "objecttype": "datetime",
                "value": "2018-10-21T21:30:00"
                },
            "time_taken": "30 seconds"
        }
    }
'''

j_dec = json.loads(j, object_hook=custom_decoder)
print(j_dec)

# Doing the same for a custom class

class Person(object):
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'

# extending the custom decoder
def custom_decoder(arg):
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            return Fraction(arg['numerator'], arg['denominator'])
        elif arg['objecttype'] == 'person':
            return Person(arg['name'], arg['ssn'])
        return arg
    return  arg

#
j = '''
    {
        "accountHolder": {
            "objecttype": "person",
            "name": "Eric Idle",
            "ssn": 100
        },
        "created": {
            "objecttype": "datetime",
            "value": "2018-10-21T03:00:00"
        }
    }
'''

d = json.loads(j, object_hook=custom_decoder)
print(d)

#

class Person(object):
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'

    def toJSON(self):
        return dict(objecttype='person', name=self.name, ssn=self.ssn)

# decoding to different data type: parse_int, parse_...?
from decimal import Decimal
def make_decimal(arg):
    print('Float Received: ', type(arg), arg)
    return Decimal(arg)

j = '''
{
    "a": 100,
    "b": 0.2,
    "c": 0.5
     
}
'''
d = json.loads(j, parse_float=make_decimal)
print(d)


# parse_int

def make_int_binary(arg):
    print('Int Received: ', type(arg), arg)
    return bin(int(arg))

d = json.loads(j, parse_int=make_int_binary, parse_float=make_decimal)
print(d)

# parse_constant

def make_constant_num(arg):
    print('Constant Received: ', type(arg), arg)
    return None

j = '''
    {
        "a": Infinity,
        "b": true,
        "c": null
    }
'''

d = json.loads(j, parse_float=make_decimal, parse_constant=make_constant_num)
print(d)
# help(json.loads)

# object_pairs_hook


def custom_decoder(arg):
    print('decoding,: ', arg, type(arg))
    return arg

j = '''
    {
        "a": 1,
        "b": 2,
        "c": {
            "c.1": 1, 
            "c.2": 2, 
            "c.3": {
                "c.3.1": 1, 
                "c.3.2": 2 
            }
        }
    }
    '''
print(json.loads(j, object_hook=custom_decoder))

def custom_pairs_decoder(arg):
    print('decoding: ', arg, type(arg))
    return arg

d = json.loads(j, object_pairs_hook=custom_pairs_decoder)
print(d)

def custom_pairs_decoder(arg):
    print('decoding: ', arg, type(arg))
    return {k: v for k, v in arg}

d = json.loads(j, object_pairs_hook=custom_pairs_decoder)
print(d)

# combine all together

j = '''
    {
        "a": [1,2,3,4,5],
        "b": 100,
        "c": 10.5,
        "d": NaN,
        "e": null,
        "f": "Python"
    }
'''

def float_handler(arg):
    print('float handler: ', type(arg), arg)
    return float(arg)

def int_handler(arg):
    print('Int handler: ', type(arg), arg)
    return int(arg)

def const_handler(arg):
    print('constant handler: ', type(arg), arg)
    return None

def obj_hook(arg):
    print('obj hook: ', arg)
    return arg


print(json.loads(j))

d = json.loads(j,
               object_hook=obj_hook,
               parse_float=float_handler,
               parse_int=int_handler,
               parse_constant=const_handler)
# print(d)


j = '''
    {
        "a": [1,2],
        "b": {
                "c": 10.5,
             "d": NaN
            }
    }
'''

d = json.loads(j,
               object_hook=obj_hook,
               parse_float=float_handler,
               parse_int=int_handler,
               parse_constant=const_handler)
print(d)
