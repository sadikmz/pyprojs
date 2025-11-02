from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(k,v)
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# print(htmlize.register(Integral))
# print(htmlize.registry)
# print(htmlize.dispatch(str))
# print(dir(htmlize))

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_integer_number(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))

# print(htmlize.registry)
# print(htmlize.dispatch)
print(type(10))
print(isinstance(10, int))
print(isinstance(10, Integral))
print(isinstance(True, Integral))
print(htmlize.dispatch(bool))
print(htmlize(True))

# @singledispatch
# def htmlize(a):
#     return escape(str(a))

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_integer_number(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# print(htmlize([1,2,3]))
# print(htmlize((1,2,3)))

print(htmlize('python'))

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_integer_number(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace('\n', '<br>\n')

print(htmlize('python 1 < 100'))

# handing tuple specifically
@htmlize.register(tuple)
def htmlize_tuple(t):
    items = (escape(str(item)) for item in t)
    return '({0})'.format(', '.join(items))

print(htmlize.registry)
print(htmlize([1,2,3]))
print(htmlize((1,2,3)))

# function names after @htmlize_registry will not be picked up - only representation and it does not have to be always named - can be named with dash "-" or "--"
# 
@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def _(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))


@htmlize.register(Sequence)
def _(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize.registry)

