# custom JSON Encoder using JSONEncoder

import json

default_encoder = json.JSONEncoder()
print(default_encoder.encode((1,2,3)))

cn = 1+1j

# print(default_encoder.encode(cn))
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)

custom_encoder = CustomJSONEncoder()

print(custom_encoder.encode(True))
# print(custom_encoder.encode([1,2,3]))
# print(custom_encoder.encode({1,2,3}))

print(json.dumps(dict(name='test', time=datetime.now()), cls=CustomJSONEncoder))

# We can encapsulate future modification to
# specifying floats
a = float('nan')
print(type(a))
print(a)

a = float('infinity')
print(type(a))
print(a)

d = {'a': float('nan'), 'b': float('infinity')}
d_json = json.dumps(d)
print(d_json)
d_ser = json.loads(d_json)
print(d_ser)

# restricting specific value types
# json.dumps({'a': float('infinity')}, allow_nan=False)

# skipkey argument
d = {10:'int', 10.5: 'float'}
d_json = json.dumps(d)
print(d_json)

d_ser = json.loads(d_json)
print(d_ser)

# modiying

# d = {10:'int', 10.5: 'float', (1,1): 'complex'}
# d_json = json.dumps(d)
# print(d_json)
#
# d_ser = json.loads(d_json)
# print(d_ser)

d = {10:'int', 10.5: 'float', (1,1): 'complex'}
d_json = json.dumps(d, skipkeys=True)
print(d_json)

d_ser = json.loads(d_json)
print(d_ser)


# separator argument

d = {
    'name': 'Python',
    'age': 27,
    'created_by': 'Guido van Rossum',
    'list': [1,2,3]
}

print(json.dumps(d,indent='***'))

# Separators
# print(json.dumps(d,indent=2, separators=(' - ',' = ')))
print(json.dumps(d, separators=(',',':')))

print(json.dumps(d, separators=(',',':'), allow_nan=False, skipkeys=True))

# package all updates in the custom JOSONEncoder

class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        # print(kwargs)
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent='---',
                         separators=('',' = ')
                         )

    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)

d = {
    'time': datetime.now(),
    1+1j:'complex',
    'name': 'Python'
}

print(json.dumps(d, cls=CustomEncoder))

# generating dictionary and more data

class CustomEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype = 'datetime',
                iso = arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minute=arg.minute,
                second=arg.second,
            )
            return obj
        else:
            return super().default(arg)


d = {'time':datetime.now()}
print(d)
print(json.dumps(d, cls=CustomEncoder))
