"""
In this project our goal is to validate one dictionary structure against a template dictionary.

A typical example of this might be working with J|SON data input in an API.
You are trying to validate this received JSON against some kind of template to make sure that
the received JSON conforms to that template (i.e. all the keys and structures are identical - value type
being important, but not the value itself - so just the structure, and the type of the value.

To keep things simple we'll assume that values can be either single value (like an integer, strings, etc),
or a dictionary, itself only containing single values or other dictionaries, recursively.
In other words, we're not going to deal with lists as possible values.  Also to keep things simple,
we'll assume that all keys are required, and that no extra keys are permitted.

In practice, we would not have these simplified assumptions, and although we could definitely write this ourselves,
there ar  many 3rd party libraries that already exist to do this (such as jsonschema, marshmallow, and many more,
some of which will be covered lightly.

"""

# For example you might have this template:
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

# So, a JSON document such as this would match the template:
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}

# But this one would **not** match the template (missing key):
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}

# And neither would this one (wrong data type):
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}



# Create an exception error type

class SchemaError(Exception):
    pass

# create new error type: inherit from SchemaError
class SchemaKeyMismatch(SchemaError):
    pass

class SchemaTypeMismatch(SchemaError, TypeError):
    pass


def validate(data, template):
    is_ok, err_msg = recursive_validate(data, template, '')
    if not is_ok:
        raise SchemaError(err_msg)

# Rewrite match keys function

def match_keys(data, valid, path):
    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys

    if missing_keys or extra_keys:
        missing_msg = ('missing keys: ' +
                       ', '.join({path + "." + str(key)
                                 for key in missing_keys})
                       ) if missing_keys else ""
        extra_msg = ('extra keys: ' +
                     ', '.join({path + "." + str(key)
                               for key in extra_keys})
                     ) if extra_keys else ""
        raise SchemaKeyMismatch(' '.join((missing_msg, extra_msg)))


# Rewrite match types

def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
            # print(value)
            # print(key)
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + "." + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)


# Rewrite recurse validate

def recursive_validate(data, template, path):

    # Check key matching of the top level elements
    match_keys(data, template, path)

    # Check the data types of the top level elements
    match_types(data, template, path)

    # check nested dictionary and validate the key and value types
    # identify the keys whose values are dictionaries
    dictionary_type_keys = {key for key, value in template.items()
                            if isinstance(value, dict)}

    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        recursive_validate(sub_data, sub_template, sub_path)

# validate
def validate(data, template):
    recursive_validate(data, template, '')


try:
    validate(michael, template)
except SchemaKeyMismatch as e:
    print('Handling a key mismatch exception', str(e))
except SchemaTypeMismatch as e:
    print('Handling a type mismatch exception', str(e))
except SchemaError as e:
    print('Handling some general schema exception', str(e))