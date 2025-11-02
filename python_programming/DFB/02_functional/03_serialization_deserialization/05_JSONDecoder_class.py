# Using JSONDecoder class
import json

j = '''
    {
        "a": 100,
        "b": [1, 2, 3],
        "c": "python",
        "d": {
            "e": 4,
            "f": 5.5
        }
    }
'''

class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, arg):
        print('decode:', type(arg), arg)
        return 'A simple string object'

print(json.loads(j, cls=CustomJSONDecoder))


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


j_points = '''
{
    "points": [
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
}
'''

j_other = '''
{
    "a": 1,
    "b": 2
}
'''

class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return 'parsing object for points'
        else:
            return super().decode(arg)

print(json.loads(j_points, cls=CustomJSONDecoder))
print(json.loads(j_other, cls=CustomJSONDecoder))


class CustomDecoder(json.JSONEncoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if 'points' in obj:
            obj['points'] = [Point(x,y)
                             for x, y in obj['points']]
        return obj

print(json.loads(j_points, cls=CustomDecoder))
print(json.loads(j_other, cls=CustomDecoder))

# schema for a point object
# define underscore type
"""
"_type": "point", "x": "x-coord", "y": "y-coord"

# http://regexr.com
"""

import re

patter = r'"_type"\s*:\s*"point'

# r is a raw string
print('word\tword')
print(r'word\tword')

regexp = re.compile(patter)

print(regexp.search('"_type":"point"'))

# re.search('"_type":"point"', '"_type":"point"')

class CustomJSONDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        pattern = r'"_type"\s*:\s*"point'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            # if obj.get('_type', None) == 'point':
            if '_type' in obj and obj['_type'] == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj

j = '''
{
    "a": 100,
    "b": 0.5,
    "rectangle": {
        "corners": {
            "b_left": {"_type": "point", "x": -1, "y": -1},
            "b_right": {"_type": "point", "x": 1, "y": -1},
            "t_left": {"_type": "point", "x": -1, "y": 1},
            "t_right": {"_type": "point", "x": 1, "y": 1}
        },
        "rotate": {"_type" : "point", "x": 0, "y": 0},
        "interior_pts": [
            {"_type": "point", "x": 0, "y": 0},
            {"_type": "point", "x": 0.5, "y": 0.5}
        ]
    }
}
'''
from pprint import pprint
# d = json.loads(j)
# pprint(d)


d = json.loads(j, cls=CustomJSONDecoder)
# pprint(d)

# override data types - parse_int, parse_float

from decimal import Decimal

CustomDecoder = json.JSONDecoder(parse_float=Decimal)

d = CustomDecoder.decode(j)
pprint(d)


#
class CustomDecoder(json.JSONDecoder):
    base_decoder = json.JSONDecoder(parse_float=Decimal)

    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        pattern = r'"_type"\s*:\s*"point'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            # if obj.get('_type', None) == 'point':
            if '_type' in obj and obj['_type'] == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj

# result = json.loads(j, cls=CustomDecoder)
# pprint(result)
#
# pt = result['rectangle']['interior_pts'][1]
# print(type(pt.y))

# with init
class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kw):
        super().__init__(parse_float=Decimal)

    def decode(self, arg):
        obj = super().decode(arg)
        pattern = r'"_type"\s*:\s*"point'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            # if obj.get('_type', None) == 'point':
            if '_type' in obj and obj['_type'] == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj

result = json.loads(j, cls=CustomDecoder)
pprint(result)

pt = result['rectangle']['interior_pts'][1]
print(type(pt.y))

